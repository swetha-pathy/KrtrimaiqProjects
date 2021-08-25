import uuid
import psycopg2
import psycopg2.extras
import random
from random import randint
import string
import pyqrcode
import base64


class write_into_db:
    psycopg2.extras.register_uuid()
    hostName = "164.52.202.154"
    dbName = "rasa_insurance"
    userName = "rasa_insurance"
    password = "rasa"

    @staticmethod
    def insert_generic_code(insert_query, data_tuple):
        conn = psycopg2.connect(host=write_into_db.hostName, database=write_into_db.dbName, user=write_into_db.userName,
                                password=write_into_db.password)
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(insert_query, data_tuple)
            # commit the changes to the database
            conn.commit()
            # close the communication with the PostgresQL database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    @staticmethod
    def select_generic_code(select_query):
        conn = psycopg2.connect(host=write_into_db.hostName, database=write_into_db.dbName, user=write_into_db.userName,
                                password=write_into_db.password)

        # create a new cursor object
        cur = conn.cursor()
        # execute the INSERT statement

        cur.execute(select_query)
        records = cur.fetchall()
        # commit the changes to the databas
        conn.commit()
        # close the communication with the PostgresQL database
        cur.close()
        return records

    @staticmethod
    def update_generic_code(update_query, data_tuple):
        conn = psycopg2.connect(host=write_into_db.hostName, database=write_into_db.dbName, user=write_into_db.userName,
                                password=write_into_db.password)
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(update_query, data_tuple)
            # commit the changes to the database
            conn.commit()
            # close the communication with the PostgresQL database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    @staticmethod
    def create_policy_number_and_qrcode():
        policyNum = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        policyNumber = ' '.join([policyNum[i:i + 4] for i in range(0, len(policyNum), 4)])

        # Generate QR code
        url = pyqrcode.create(policyNumber)
        qrcode_base64_str = url.png_as_base64_str()
        print(policyNumber)
        return qrcode_base64_str, policyNumber

    @staticmethod
    def get_qrcode():
        # connect to the PostgresQL database
        conn = psycopg2.connect(host=write_into_db.hostName, database=write_into_db.dbName, user=write_into_db.userName,
                                password=write_into_db.password)
        # create a new cursor object
        cur = conn.cursor()
        # execute the SELECT statement
        cur.execute(" SELECT QR_Code FROM documentdetails WHERE customer_id = '69ab8635-58ae-44b7-b5e6-85d0b226e0dd'")
        blob = cur.fetchone()
        mv = blob[0]
        img_bytes = bytes(mv)
        base64EncodedStr = base64.b64encode(img_bytes)
        # close the communication with the PostgresQL database
        cur.close()
        return base64EncodedStr

    @classmethod
    def select_new_customer(self):
        new_customer = self.select_generic_code(
            "select * from customerdetails where customer_id = '69ab8635-58ae-44b7-b5e6-85d0b226e0dd'")
        print(len(new_customer))

    @classmethod
    def insert_new_customer(self, customer_name, phone_no, email_id, age_slot, profession_slot, address_slot):
        print("in new customer")
        try:
            self.insert_generic_code("insert into customerdetails(customer_id, name, email, phoneno, age, profession, address)" +
                                     "VALUES(%s, %s, %s, %s, %s, %s, %s)",
                                     (uuid.uuid4(), customer_name, email_id, phone_no, age_slot, profession_slot, address_slot))
            print("row inserted")
        except:
            print("Duplicate error")


    @classmethod
    def insert_document_details(self, phone_no, image_base64_str):
        customer = self.select_generic_code("select customer_id from customerdetails where phoneno = %s" % (phone_no))
        print(customer)
        length = len(customer)
        print(length)
        if length == 1:
            print("inside insert documents")
            self.insert_generic_code("insert into documentdetails(document_id, customer_id, pan_aadhar)" +
                                     "VALUES(%s, %s, %s)", (
                                         uuid.uuid4(), customer[0][0], image_base64_str))
            return "Row inserted"
        else:
            return "Customer does not exist"

    @classmethod
    def find_existing_customer_phone(self, phone_no):
        existing_customer_name = self.select_generic_code(
            'select * from customerdetails where phoneno = %s' % (phone_no))
        if len(existing_customer_name) >= 1:
            return existing_customer_name
        else:
            return "Customer not found"

    @classmethod
    def find_existing_customer_policy_number(self, policy_number):
        customer_id = self.select_generic_code(
            'select customer_id from policydetails where policy_number = %s' % ("'" + policy_number + "'"))
        length = len(customer_id)
        if length == 1:
            customer_id = str(customer_id[0][0])
            existing_customer_policy_number_details = self.select_generic_code(
                'select * from customerdetails where customer_id = %s' % ("'" + customer_id + "'"))
            return existing_customer_policy_number_details
        else:
            return "Customer not found"


    @classmethod
    def insert_product_details(self, product_description, product_template, tariff, tax, total_tariff, product_name):
        self.insert_generic_code(
            "insert into productdetails(product_id, description, product_template, tariff, tax, totaltariff, product_name)" +
            "VALUES(%s, %s, %s, %s, %s, %s, %s)",
            (uuid.uuid4(), product_description, product_template, tariff, tax, total_tariff, product_name))

    @classmethod
    def get_product_column_values(self, column):
        column_values = self.select_generic_code("select %s from productdetails" % (column))
        return column_values

    @classmethod
    def get_product_details(self, column_name, product_name):
        product_id = self.select_generic_code(
            "select product_id from productdetails where product_name = %s" % ("'" + product_name + "'"))
        product_id = str(product_id[0][0])
        product_details = self.select_generic_code(
            "select %s from productdetails where product_id = %s;" % (column_name, "'" + product_id + "'"))
        if len(product_details) >= 1:
            return product_details
        else:
            return "Product not found"

    @classmethod
    def insert_otp(self, phone_no):
        otp = ''.join(str(randint(100000, 999999)))
        print("insert otp db operations function")
        print(otp)
        self.insert_generic_code("insert into otp(otp_id, phoneno, otp) values(%s, %s, %s)",
                                 (uuid.uuid4(), phone_no, otp))

    @classmethod
    def get_otp(self, phone_no):
        otp_obj = self.select_generic_code(
            "select otp from otp where phoneno = %s ORDER BY created_at DESC" % (phone_no))
        otp = otp_obj[0][0]
        # print(otp)
        return otp

    @classmethod
    def update_customer_phone_no(self, old_phone_no, new_phone_no):
        customer_id = self.select_generic_code(
            "select customer_id from customerdetails where phoneno = %s" % (old_phone_no))
        customerid = customer_id[0][0]
        print(customerid)
        self.update_generic_code(
            "UPDATE customerdetails SET phoneno = %s" + "WHERE customer_id = %s;", (new_phone_no, customerid))

    @classmethod
    def update_customer_email_id(self, phone_no, new_email_id):
        print("in the update customer mail id")
        print(new_email_id)
        customer_id = self.select_generic_code("select customer_id from customerdetails where phoneno = %s" % (phone_no))
        customerid = customer_id[0][0]
        self.update_generic_code(
            "UPDATE customerdetails SET email = %s" +
            "WHERE customer_id = %s;",
            (new_email_id, customerid))

    @classmethod
    def insert_quotation_details(self, phone_no, product_name, pdf_blob_quotation):
        customer = self.select_generic_code("select customer_id from customerdetails where phoneno = %s" % (phone_no))
        print(customer)
        customerId = customer[0][0]
        print(customerId)
        product = self.select_generic_code(
            "select product_id from productdetails where product_name = %s" % ("'" + product_name + "'"))
        productId = product[0][0]
        self.insert_generic_code(
            "insert into quotationdetails(quotation_id, customer_id, product_id, payment_done, payment_id, quotation_document)" +
            "VALUES(%s, %s, %s, %s, %s, %s)",
            (uuid.uuid4(), customerId, productId, 'no', 'NULL', pdf_blob_quotation))
        print("row inserted inside quotation details table")

    @classmethod
    def insert_policy_details(self, phone_no, start_date, end_date, policy_number, qr_code, pdf_blob_policy):
        #policy_number, qr_code = create_policy_number_and_qrcode()
        customer = self.select_generic_code("select customer_id from customerdetails where phoneno = %s" % (phone_no))
        customerId = customer[0][0]
        self.insert_generic_code(
            "insert into policydetails(customer_id, policy_number, payment_id, startdate, enddate, policy_document, qr_code)" +
            "VALUES(%s, %s, %s, %s, %s, %s, %s)",
            (customerId, policy_number, 'NULL', start_date, end_date, pdf_blob_policy, qr_code))
        print("row inserted inside policy details table")


# write_into_db.insert_new_customer("Kushal", "917876787578", "kush@gm.com", "34", "engineer")
# write_into_db.insert_document_details(write_into_db.create_policy_number())
# write_into_db.find_existing_customer()
# write_into_db.get_qrcode()

# url = pyqrcode.create(8976543210)
# qrcode_base64_str = url.png_as_base64_str()

# insert_product_details(self, product_description, product_template, tariff, tax, total_tariff, product_name)
# write_into_db.insert_product_details("",qrcode_base64_str, "15000", "960", "15960", "Fire Accident Policy")
