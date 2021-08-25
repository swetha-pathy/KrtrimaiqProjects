from typing import Dict, Text, Any, List, Union
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet, UserUtteranceReverted, FollowupAction, Restarted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
# from rasa.core.events import UserUttered
import re
import smtplib
import keyboard
import psycopg2
import base64
import cv2
import pdfkit
from bs4 import BeautifulSoup
import os
from db.db_operations import write_into_db
from utils.send_whatsapp_pdf import whatsapp
from utils.capture_document import CaptureWebcam
from utils.intent_mapping import Intents
from datetime import date
import datetime

#os.environ['PATH'] = "C:/Program Files/wkhtmltopdf/bin"

class SendMail(Action):
    def name(self) -> Text:
        return "action_send_mail"

    # Retrieve QR code image from the database
    def read_blob(self):
        global base64EncodedStr
        # connect to the PostgresQL database
        conn = psycopg2.connect(host="164.52.202.154", database="rasa_insurance", user="rasa_insurance", password="rasa")
        # create a new cursor object
        cur = conn.cursor()
        # execute the SELECT statement
        cur.execute(""" SELECT QR_Code
                               FROM documentdetailsnew
                               WHERE customer_id = %s""", [1002])
        blob = cur.fetchone()
        mv = blob[0]
        img_bytes = bytes(mv)
        base64EncodedStr = base64.b64encode(img_bytes)
        # close the communication with the PostgresQL database
        cur.close()
        return base64EncodedStr

    @classmethod
    def create_quotation_pdf(self, senderName, senderEmail, senderPhone, productName, address, premium, startDate,
                             endDate):
        with open("data/logo.png", "rb") as img_file:
            logo = base64.b64encode(img_file.read())
            decoded_logo = logo.decode()
        with open("templates/quotation.html", "r") as f:
            contents = f.read()
            soup = BeautifulSoup(contents, 'lxml')
            ids = ['name', 'phone_no', 'policy_type', 'email', 'address', 'premium', 'total_premium', 'start_date',
                   'end_date']
            details = [senderName, senderPhone, productName, senderEmail, address, premium, premium, startDate, endDate]
            with open('output/output.html', "wb+") as myFile:
                for (i, item) in zip(ids, details):
                    myFile.seek(0)
                    soup.find(id=i).string.replace_with(item)
                    html = soup.prettify("utf-8")
                    myFile.write(html)
                    myFile.truncate()
                    img_src = "data:image/png;base64,"
                    img_read_str_logo = str(decoded_logo)
                    concat_str_logo = img_src + img_read_str_logo
                    soup.find(id='logo')['src'] = concat_str_logo
            myFile.close()
        f.close()

        with open('output/output.html', 'r') as b:
            pdf = pdfkit.from_file(b, False)
            pdf_blob_quotation = base64.b64encode(pdf)
        return pdf, pdf_blob_quotation

    @classmethod
    def create_policy_doc_pdf(self, senderName, senderEmail, senderPhone, productName, policyNumber, startDate, endDate,
                              qrcode_base64_str, address, premium):
        with open("data/logo.png", "rb") as img_file:
            logo = base64.b64encode(img_file.read())
            decoded_logo = logo.decode()
        with open("templates/policy_document.html", "r") as fp:
            contents = fp.read()
            soup = BeautifulSoup(contents, 'lxml')
            ids = ['name', 'phone_no', 'policy_type', 'email', 'policy_number', 'start_date', 'end_date', 'address',
                   'premium', 'total_premium', 'issuance_date', 'payment_date']
            details = [senderName, senderPhone, productName, senderEmail, policyNumber, startDate, endDate, address,
                       premium, premium, startDate, startDate]
            with open('output/output.html', "wb+") as myFile:
                for (i, item) in zip(ids, details):
                    myFile.seek(0)
                    soup.find(id=i).string.replace_with(item)
                    html = soup.prettify("utf-8")
                    myFile.write(html)
                    myFile.truncate()
                    img_src = "data:image/png;base64,"
                    img_read_str = str(qrcode_base64_str)
                    concat_str = img_src + img_read_str
                    soup.find(id='qrcode_img')['src'] = concat_str
                    img_read_str_logo = str(decoded_logo)
                    concat_str_logo = img_src + img_read_str_logo
                    soup.find(id='logo')['src'] = concat_str_logo
            myFile.close()

        with open('output/output.html', 'r') as b:
            pdf = pdfkit.from_file(b, False)
            pdf_blob_policy = base64.b64encode(pdf)
        return pdf, pdf_blob_policy

    @staticmethod
    def send_email(senderEmail, flowType, document_pdf, productName):
        fromaddr = 'ins.assistant@krtrimaiq.ai'
        password = 'wW!?{Q90uC9G'
        toaddrs = senderEmail
        server_smtp = 'mail.krtrimaiq.ai'
        port_smtp = 587

        try:
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddrs
            if flowType == "Show Quotation":
                filename = "quotation.pdf"
                msg['Subject'] = productName + " Quotation Document"
                body = "Hi, This is Disha. Thank you for visiting me. It was great having conversation with you." \
                       " Please find the attached Quotation for " + productName + " which you have requested"
            else:
                filename = "policy_document.pdf"
                msg['Subject'] = productName + " Document"
                body = "Hi, This is Disha. Thank you for purchasing a policy with me. It was great having conversation with you." \
                       " Please find the attachment for the details of " + productName + " which you have purchased"
            msg.attach(MIMEText(body, 'plain'))
            p = MIMEBase("application", "pdf")
            p.set_payload(document_pdf)
            encoders.encode_base64(p)
            #p.set_payload(str(document_pdf, 'ascii'))
            #p.add_header('Content-Transfer-Encoding', 'base64')
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)
            s = smtplib.SMTP('mail.krtrimaiq.ai', 587)
            s.starttls()
            #s.set_debuglevel(True)
            #s.esmtp_features['auth'] = 'LOGIN PLAIN'
            s.login("ins.assistant@krtrimaiq.ai", "wW!?{Q90uC9G")

            text = msg.as_string()

            # sending the mail
            s.sendmail(fromaddr, toaddrs, text)
            s.quit()
            print("Mail successful")
            return True, filename
        except smtplib.SMTPServerDisconnected:
            print("smtplib.SMTPServerDisconnected")
        except smtplib.SMTPResponseException as e:
            print("smtplib.SMTPResponseException: " + str(e.smtp_code) + " " + str(e.smtp_error))
        except smtplib.SMTPSenderRefused:
            print("smtplib.SMTPSenderRefused")
        except smtplib.SMTPRecipientsRefused:
            print("smtplib.SMTPRecipientsRefused")
        except smtplib.SMTPDataError:
            print("smtplib.SMTPDataError")
        except smtplib.SMTPConnectError:
            print("smtplib.SMTPConnectError")
        except smtplib.SMTPHeloError:
            print("smtplib.SMTPHeloError")
        except smtplib.SMTPAuthenticationError:
            print("smtplib.SMTPAuthenticationError")

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        senderEmail = tracker.get_slot('email_id')
        senderName = tracker.get_slot('customer_name')
        senderPhone = tracker.get_slot('phone_no')
        productName = tracker.get_slot('slot_product')
        flowType = tracker.get_slot('slot_flow')
        address = tracker.get_slot('address_slot')
        print(address)
        premium_details = write_into_db.get_product_details("totaltariff", productName)
        if premium_details != "Product not found":
            temp = []
            for i in range(0, len(premium_details[0])):
                temp.append(str(premium_details[0][i]))
            premium = " ".join(temp)
            # print("premium inside if")
            print(premium)
        else:
            print("Premium of the product not found")
        print("Flow : ")
        print(flowType)
        ecFlowType = tracker.get_slot('slot_ec_flow')
        print("EC Flow : ")
        print(ecFlowType)
        startDate = str(date.today())
        endDate = str(date.today() + datetime.timedelta(364 * 1))
        print(startDate)
        print(endDate)
        qrcode_base64_str, policyNumber = write_into_db.create_policy_number_and_qrcode()
        # write_blob()
        # self.read_blob()

        #this is for creation of PDF
        if flowType == "Show Quotation" or ecFlowType == "Show Quotation":
            document_pdf, document_blob_pdf = self.create_quotation_pdf(senderName, senderEmail, senderPhone, productName, address, premium, startDate, endDate)
            mailType = "Quotation"
        else:
            document_pdf, document_blob_pdf = self.create_policy_doc_pdf(senderName, senderEmail, senderPhone, productName, policyNumber,
                                                         startDate, endDate, qrcode_base64_str, address, premium)
            mailType = "Policy"

        #this is for sending mail
        if flowType != None:
            mail_status, file = self.send_email(senderEmail, flowType, document_pdf, productName)
        else:
            mail_status, file = self.send_email(senderEmail, ecFlowType, document_pdf, productName)

        if(not mail_status):
            dispatcher.utter_message(text="Email was not sent. Please contact the administrator!")
        if file == "quotation.pdf":
            dispatcher.utter_message(template="utter_mail_send")
        elif file == "policy_document.pdf":
            dispatcher.utter_message(text="Policy Document has been sent successfully to your mail : " + senderEmail)

        #this is done separately coz to save time for sending mail
        if mailType == "Quotation":
            write_into_db.insert_quotation_details(senderPhone, productName, document_blob_pdf)
        else:
            write_into_db.insert_policy_details(senderPhone, startDate, endDate, policyNumber, qrcode_base64_str,
                                                document_blob_pdf)
        return []


class SendMailOTP(Action):
    def name(self) -> Text:
        return "action_send_mail_otp"

    '''def write_blob():
           """ insert a BLOB into a table """
           conn = None
           try:
               # read data from a picture
               img = open('/output/qrcode.png', 'rb').read()
               # read database configuration
               # params = Config()
               # connect to the PostgresQL database
               conn = psycopg2.connect(host="164.52.202.154", database="rasa_insurance", user="rasa_insurance", password="rasa")
               # create a new cursor object
               cur = conn.cursor()
               # execute the INSERT statement
               cur.execute("insert into customerdetailsnew(customer_id, name, email, phoneno, age, profession)" +
                           "VALUES(%s, %s, %s, %s, %s, %s)", (1002, 'swetha', 'swetha.pathy@krtrimaiq.ai', '9868584848', '23', 'intern'))

               cur.execute("insert into documentdetailsnew(document_id, customer_id, PAN_Aadhar, QR_Code)" +
                           "VALUES(%s, %s, %s, %s)", (2, 1002, psycopg2.Binary(img), psycopg2.Binary(img)))
               # commit the changes to the database
               conn.commit()
               # close the communication with the PostgresQL database
               cur.close()
           except (Exception, psycopg2.DatabaseError) as error:
               print(error)
           finally:
               if conn is not None:
                   conn.close()'''

    @staticmethod
    def send_email(message, SubjectMessage, senderEmailId, OTP):
        fromaddr = 'ins.assistant@krtrimaiq.ai'
        password = 'wW!?{Q90uC9G'
        toaddrs = senderEmailId
        server_smtp = 'mail.krtrimaiq.ai'
        port_smtp = 587

        try:
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddrs
            msg['Subject'] = SubjectMessage
            body = "Hi !! I am Disha. This is your OTP " + message + " : {}".format(OTP)
            msg.attach(MIMEText(body, 'plain'))
            s = smtplib.SMTP('mail.krtrimaiq.ai', 587)
            s.starttls()
            # s.esmtp_features['auth'] = 'LOGIN PLAIN'
            s.login("ins.assistant@krtrimaiq.ai", "wW!?{Q90uC9G")

            text = msg.as_string()

            # sending the mail
            s.sendmail(fromaddr, toaddrs, text)
            s.quit()
            print("Mail successful")
            return True
        except smtplib.SMTPServerDisconnected:
            print("smtplib.SMTPServerDisconnected")
        except smtplib.SMTPResponseException as e:
            print("smtplib.SMTPResponseException: " + str(e.smtp_code) + " " + str(e.smtp_error))
        except smtplib.SMTPSenderRefused:
            print("smtplib.SMTPSenderRefused")
        except smtplib.SMTPRecipientsRefused:
            print("smtplib.SMTPRecipientsRefused")
        except smtplib.SMTPDataError:
            print("smtplib.SMTPDataError")
        except smtplib.SMTPConnectError:
            print("smtplib.SMTPConnectError")
        except smtplib.SMTPHeloError:
            print("smtplib.SMTPHeloError")
        except smtplib.SMTPAuthenticationError:
            print("smtplib.SMTPAuthenticationError")

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        senderPhone = tracker.get_slot('slot_ec_phone_no')
        print("old phone number : ")
        print(senderPhone)
        senderNewPhoneNo = tracker.get_slot('slot_ec_get_update_phone_no')
        print("new phone number : ")
        print(senderNewPhoneNo)
        write_into_db.insert_otp(senderPhone)
        OTP = write_into_db.get_otp(senderPhone)
        print(OTP)
        details = write_into_db.find_existing_customer_phone(senderPhone)
        senderEmailId = str(details[0][2])
        if senderNewPhoneNo == None:
            mail_status = self.send_email("for validating customer details", "Customer Validation OTP", senderEmailId, OTP)
        else:
            mail_status = self.send_email("for validating phone number updation", "Phone Number Updation OTP", senderEmailId, OTP)

        if (not mail_status):
            dispatcher.utter_message(text="Email was not sent. Please contact the administrator!")
            return []
        else:
            if senderNewPhoneNo == None:
                return [FollowupAction("ec_otp_form")]
            return []
        #dispatcher.utter_message(template="utter_mail_send_OTP")


class ProductsDisplay(Action):
    def name(self) -> Text:
        return "action_products_display"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> str:
        product_name = write_into_db.get_product_column_values("product_name")

        products_button_names = []
        for i in range(0, len(product_name)):
            products_button_names.append(product_name[i][0])

        buttons = []
        for row in products_button_names:  # dynamic buttons
            buttons.append(
                {"title": row,
                 "payload": "/product" + '{' + '"slot_product"' + ': ' + '"' + str(row) + '"' + '}'})
        dispatcher.utter_button_message("Here are some products available. Choose any option to know more..!!", buttons)
        return []


class ProductInfoDisplay(Action):
    def name(self) -> Text:
        return "action_product_info_display"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> str:
        product_name = tracker.get_slot("slot_product")
        print(product_name)
        product_details = write_into_db.get_product_details("description", product_name)
        if product_details != "Product not found":
            temp = []
            for i in range(0, len(product_details[0])):
                temp.append(str(product_details[0][i]))
            product_str_details = " ".join(temp)
            print(product_str_details)
            dispatcher.utter_message(text="Here are the product details")
            dispatcher.utter_message(text=product_str_details)
            return []
        else:
            print(product_details)


class ShowQuotation(Action):
    def name(self) -> Text:
        return "action_show_quotation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> str:
        product_name = tracker.get_slot("slot_product")
        print(product_name)
        product_details = write_into_db.get_product_details("totaltariff", product_name)
        if product_details != "Product not found":
            temp = []
            for i in range(0, len(product_details[0])):
                temp.append(str(product_details[0][i]))
            product_str_details = " ".join(temp)
            print(product_str_details)
            dispatcher.utter_message(text="Here is the Premium for the policy you have requested:")
            dispatcher.utter_message("Product: " + product_name + "\n" + "Premium :" + product_str_details)
            return [SlotSet("slot_flow", "Show Quotation"), SlotSet("slot_ec_flow", "Show Quotation")]
        else:
            print(product_details)
            return []


class DisplayExistingCustomerDetails(Action):
    def name(self) -> Text:
        return "action_existing_customer_details_display"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> str:
        phoneOrPolicy = tracker.get_slot("slot_ec_phone_or_policy")
        print(phoneOrPolicy)
        if phoneOrPolicy == "Phone Number":
            ecPhoneNo = tracker.get_slot("slot_ec_phone_no")
            details = write_into_db.find_existing_customer_phone(ecPhoneNo)
        else:
            ecPolicyNo = tracker.get_slot("slot_ec_policy_no")
            if "list" in str(type(ecPolicyNo)):
                details = write_into_db.find_existing_customer_policy_number(ecPolicyNo[0])
            else:
                details = write_into_db.find_existing_customer_policy_number(ecPolicyNo)
        temp = []
        for i in range(1, len(details[0])):
            temp.append(str(details[0][i]))
        str_details = " ".join(temp)
        print(str_details)
        dispatcher.utter_message(text="Welcome back " + str(details[0][1]))
        dispatcher.utter_template("utter_ec_options", tracker)
        return [SlotSet("customer_name", str(details[0][1])), SlotSet("email_id", str(details[0][2])),
                SlotSet("phone_no", str(details[0][3])), SlotSet("age_slot", str(details[0][4])),
                SlotSet("profession_slot", str(details[0][5])), SlotSet("address_slot", str(details[0][6])),
                SlotSet("slot_ec_phone_no", str(details[0][3]))]


class ValidateExistingCustomer(Action):
    def name(self) -> Text:
        return "action_validate_existing_customer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> str:
        phoneOrPolicy = tracker.get_slot("slot_ec_phone_or_policy")
        print("action_validate_existing_customer")
        print(phoneOrPolicy)
        if phoneOrPolicy == "Phone Number":
            ecPhoneNo = tracker.get_slot("slot_ec_phone_no")
            print(ecPhoneNo)
            details = write_into_db.find_existing_customer_phone(ecPhoneNo)
            if details != "Customer not found":
                print("Customer Found")
                #dispatcher.utter_template("utter_ec_phone_no_details_correct_otp_message", tracker)
                return[FollowupAction("action_send_mail_otp")]
            else:
                print("Customer NOT Found")
                dispatcher.utter_template("utter_ec_phone_no_details_wrong_message", tracker)
                print("we are in else condition, inside Phone No Slot")
                return [SlotSet("slot_ec_phone_no", None), FollowupAction("ec_phone_no_form")]
        else:
            ecPolicyNo = tracker.get_slot("slot_ec_policy_no")
            print(ecPolicyNo)
            if "list" in str(type(ecPolicyNo)):
                details = write_into_db.find_existing_customer_policy_number(ecPolicyNo[0])
                if details != "Customer not found":
                    print("Customer Found")
                    # dispatcher.utter_template("utter_ec_policy_no_details_correct_message", tracker)
                    return [FollowupAction("action_existing_customer_details_display")]
                else:
                    print("Customer NOT Found")
                    print("we are in else condition, inside Policy No Slot")
                    dispatcher.utter_template("utter_ec_policy_no_details_wrong_message", tracker)
                    dispatcher.utter_template("utter_ec_scan_or_manual_policy_no", tracker)
                    return [SlotSet("slot_ec_policy_no", None)]
            else:
                details = write_into_db.find_existing_customer_policy_number(ecPolicyNo)
                if details != "Customer not found":
                    print("Customer Found")
                    # dispatcher.utter_template("utter_ec_policy_no_details_correct_message", tracker)
                    return [FollowupAction("action_existing_customer_details_display")]
                else:
                    print("Customer NOT Found")
                    print("we are in else condition, inside Policy No Slot")
                    dispatcher.utter_template("utter_ec_policy_no_details_wrong_message", tracker)
                    dispatcher.utter_template("utter_ec_scan_or_manual_policy_no", tracker)
                    return [SlotSet("slot_ec_policy_no", None)]


class ValidateExistingCustomerOTP(Action):
    def name(self) -> Text:
        return "action_validate_existing_customer_otp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> str:
        getUserOTP = tracker.get_slot("slot_ec_otp")
        print("action_validate_existing_customer_otp")
        print(getUserOTP)
        ecPhoneNo = tracker.get_slot("slot_ec_phone_no")
        getDatabaseOTP = write_into_db.get_otp(ecPhoneNo)
        print(getDatabaseOTP)
        if int(getUserOTP) == int(getDatabaseOTP):
            #dispatcher.utter_template("utter_ec_phone_no_otp_correct_message", tracker)
            return [FollowupAction("action_existing_customer_details_display")]
        else:
            dispatcher.utter_template("utter_ec_phone_no_otp_wrong_message", tracker)
            return [SlotSet("slot_ec_otp", None)] #, FollowupAction("ec_otp_form")]


class ValidateUpdatePhoneNoOTP(Action):
    def name(self) -> Text:
        return "action_ec_validate_update_phone_no_otp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> str:
        getUserOTP = tracker.get_slot("slot_ec_otp_update_phone_no")
        print("action_ec_validate_update_phone_no_otp")
        print(getUserOTP)
        ecPhoneNo = tracker.get_slot("slot_ec_phone_no")
        getDatabaseOTP = write_into_db.get_otp(ecPhoneNo)
        print(getDatabaseOTP)
        if int(getUserOTP) == int(getDatabaseOTP):
            #dispatcher.utter_template("utter_ec_update_phone_no_otp_correct_message", tracker)
            return[FollowupAction("action_existing_customer_update_phone_no")]
        else:
            dispatcher.utter_template("utter_ec_update_phone_no_otp_wrong_message", tracker)
        return [SlotSet("slot_ec_otp_update_phone_no", None)] #, FollowupAction("ec_otp_form")


class ValidateUpdateEmailOTP(Action):
    def name(self) -> Text:
        return "action_ec_validate_update_email_otp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> str:
        getUserOTP = tracker.get_slot("slot_ec_otp_update_email_address")
        print("action_ec_validate_update_email_otp")
        print(getUserOTP)
        ecPhoneNo = tracker.get_slot("slot_ec_phone_no")
        getDatabaseOTP = write_into_db.get_otp(ecPhoneNo)
        print(getDatabaseOTP)
        if int(getUserOTP) == int(getDatabaseOTP):
            #dispatcher.utter_template("utter_ec_update_phone_no_otp_correct_message", tracker)
            return[FollowupAction("action_existing_customer_update_email_address")]
        else:
            dispatcher.utter_template("utter_wrong_slot_ec_otp_update_email_address", tracker)
        return [SlotSet("slot_ec_otp_update_email_address", None)]


class ECPhoneNoOTPForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ec_otp_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        if tracker.get_slot('slot_update_details') != "Update Phone No":
            return ["slot_ec_otp"]
        else:
            return ["slot_ec_otp_update_phone_no"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "slot_ec_otp": [
                self.from_entity(
                    entity="otp", intent=["one_time_pass"]
                )
            ],
            "slot_ec_otp_update_phone_no": [
                self.from_entity(
                    entity="otp", intent=["one_time_pass"]
                )
            ]
        }

    # USED FOR DOCS: do not rename without updating in docs

    def validate_slot_ec_otp(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        regexNum = "^[0-9]{6}$"
        print(value)
        print(type(value))
        if "list" in str(type(value)):
            print("inside if, type is list")
            if re.search(regexNum, value[0]):
                print("regex is matched")
                return {"slot_ec_otp": value[0]}
            else:
                dispatcher.utter_message(template="utter_wrong_slot_ec_otp")
                # validation failed, set slot to None
                return {"slot_ec_otp": None}
        else:
            print("inside else, type is string")
            if re.search(regexNum, value):
                print("regex is matched")
                return {"slot_ec_otp": value}
            else:
                dispatcher.utter_message(template="utter_wrong_slot_ec_otp")
                # validation failed, set slot to None
                return {"slot_ec_otp": None}

    def validate_slot_ec_otp_update_phone_no(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        regexNum = "^[0-9]{6}$"
        print(value)
        print(type(value))
        if "list" in str(type(value)):
            if re.search(regexNum, value[0]):
                return {"slot_ec_otp_update_phone_no": value[0]}
            else:
                dispatcher.utter_message(template="utter_wrong_slot_ec_otp")
                # validation failed, set slot to None
                return {"slot_ec_otp_update_phone_no": None}
        else:
            if re.search(regexNum, value):
                return {"slot_ec_otp_update_phone_no": value}
            else:
                dispatcher.utter_message(template="utter_wrong_slot_ec_otp")
                # validation failed, set slot to None
                return {"slot_ec_otp_update_phone_no": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        print("ec_otp_form")
        return []


class ECPolicyNoForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ec_policy_no_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["slot_ec_policy_no"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "slot_ec_policy_no": self.from_entity(entity="policy_number", intent="give_policyno")
        }
    # USED FOR DOCS: do not rename without updating in docs
    def validate_slot_ec_policy_no(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        print(value)
        print(type(value))
        if "list" in str(type(value)):
            return {"slot_ec_policy_no": value[0]}
        else:
            return {"slot_ec_policy_no": value}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        # dispatcher.utter_message(template="utter_ec_policy_no_validating_message")
        return [SlotSet("slot_ec_phone_or_policy", "Policy Number")]


class ECPhoneNoForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ec_phone_no_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["slot_ec_phone_no"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "slot_ec_phone_no": [
                self.from_entity(
                    entity="phone", intent=["give_phoneno"]
                )
            ]
        }

    # USED FOR DOCS: do not rename without updating in docs

    def validate_slot_ec_phone_no(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""

        '''if "list" in str(type(value)):
            if re.search(regexNum, value[0]):
                return {"slot_ec_phone_no": value[0]}
            else:
                dispatcher.utter_message(template="utter_wrong_slot_ec_phone_no")
                # validation failed, set slot to None
                return {"slot_ec_phone_no": None}
        else:
            if re.search(regexNum, value):
                return {"slot_ec_phone_no": value}
            else:
                dispatcher.utter_message(template="utter_wrong_slot_ec_phone_no")
                # validation failed, set slot to None
                return {"slot_ec_phone_no": None} '''
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        print(len(value))
        print(value)
        print(type(value))
        if "list" in str(type(value)):
            print("list is present, inside if condition")
            if 12 <= len(value[0]) <= 14:
                # re.search(regexNum, value[0]) , "+" in value[0], value[0] = value[0][1:]
                if (regex.search(value[0]) == None):
                    if "+" in value[0]:
                        print("phone no has plus symbol")
                        value[0] = value[0][1:]
                    if value[0].isdigit():
                        return {"slot_ec_phone_no": value[0]}
                    else:
                        print("phone no has string characters")
                        dispatcher.utter_message(text="Please enter numeric digits only for the Phone Number")
                        return {"slot_ec_phone_no": None}
                else:
                    print("phone no has special characters")
                    dispatcher.utter_message(text="Please enter numeric digits only for the Phone Number")
                    return {"slot_ec_phone_no": None}
            elif len(value[0]) > 14:
                print("phone no has more than 14 digits")
                dispatcher.utter_message(
                    text="I'm afraid its an invalid Phone Number, please enter a valid registered Phone Number")
                return {"slot_ec_phone_no": None}
            elif len(value[0]) < 12:
                print("phone no has less than 12 digits")
                dispatcher.utter_message(
                    text="I'm afraid its an invalid Phone Number, please enter a valid registered Phone Number")
                return {"slot_ec_phone_no": None}
        else:
            print("list is not present, inside else condition")
            if 12 <= len(value) <= 14:
                if (regex.search(value) == None):
                    if "+" in value:
                        print("phone no has plus symbol")
                        value = value[1:]
                    if value.isdigit():
                        return {"slot_ec_phone_no": value}
                    else:
                        print("phone no has string characters")
                        dispatcher.utter_message(text="Please enter numeric digits only for the Phone Number")
                        return {"slot_ec_phone_no": None}
                else:
                    print("phone no has special characters")
                    dispatcher.utter_message(text="Please enter numeric digits only for the Phone Number")
                    return {"slot_ec_phone_no": None}
            elif len(value) > 14:
                print("phone no has more than 14 digits")
                dispatcher.utter_message(
                    text="I'm afraid its an invalid Phone Number, please enter a valid registered Phone Number")
                return {"slot_ec_phone_no": None}
            elif len(value[0]) < 12:
                print("phone no has less than 12 digits")
                dispatcher.utter_message(
                    text="I'm afraid its an invalid Phone Number, please enter a valid Phone Number")
                return {"slot_ec_phone_no": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        # dispatcher.utter_message(template="utter_submit")
        return [SlotSet("slot_ec_phone_or_policy", "Phone Number")]


class ECUpdateDetailsForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ec_update_details_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        if tracker.get_slot('slot_update_details') == "Update Phone No":
            return ["slot_ec_get_update_phone_no"]
        elif tracker.get_slot('slot_update_details') == "Update Email Id":
            return ["slot_ec_get_update_email_id"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "slot_ec_get_update_phone_no": [self.from_entity(entity="phone", intent="give_phoneno"), self.from_text()],
            "slot_ec_get_update_email_id": [self.from_entity(entity="email", intent="give_mail"), self.from_text()]
        }

    def validate_slot_ec_get_update_phone_no(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        print(len(value))
        print(value)
        print(type(value))
        if "list" in str(type(value)):
            print("list is present, inside if condition")
            if 12 <= len(value[0]) <= 14:
                # re.search(regexNum, value[0]) , "+" in value[0], value[0] = value[0][1:]
                if (regex.search(value[0]) == None):
                    if "+" in value[0]:
                        print("phone no has plus symbol")
                        value[0] = value[0][1:]
                    if value[0].isdigit():
                        return {"slot_ec_get_update_phone_no": value[0]}
                    else:
                        print("phone no has string characters")
                        dispatcher.utter_message(text="Please enter numeric digits only for the Phone Numbers")
                        return {"slot_ec_get_update_phone_no": None}
                else:
                    print("phone no has special characters")
                    dispatcher.utter_message(text="Please enter numeric digits only for the Phone Number")
                    return {"slot_ec_get_update_phone_no": None}
            elif len(value[0]) > 14:
                print("phone no has more than 14 digits")
                dispatcher.utter_message(
                    text="I'm afraid its an invalid Phone Number, please enter a valid Phone Number")
                return {"slot_ec_get_update_phone_no": None}
            elif len(value[0]) < 12:
                print("phone no has less than 12 digits")
                dispatcher.utter_message(
                    text="I'm afraid its an invalid Phone Number, please enter a valid Phone Number")
                return {"slot_ec_get_update_phone_no": None}
        else:
            print("list is not present, inside else condition")
            if 12 <= len(value) <= 14:
                if (regex.search(value) == None):
                    if "+" in value:
                        print("phone no has plus symbol")
                        value = value[1:]
                    if value.isdigit():
                        return {"slot_ec_get_update_phone_no": value}
                    else:
                        print("phone no has string characters")
                        dispatcher.utter_message(text="Please enter numeric digits only for the Phone Number")
                        return {"slot_ec_get_update_phone_no": None}
                else:
                    print("phone no has special characters")
                    dispatcher.utter_message(text="Please enter numeric digits only for the Phone Number")
                    return {"slot_ec_get_update_phone_no": None}
            elif len(value) > 14:
                print("phone no has more than 14 digits")
                dispatcher.utter_message(
                    text="I'm afraid its an invalid Phone Number, please enter a valid Phone Number")
                return {"slot_ec_get_update_phone_no": None}
            elif len(value[0]) < 12:
                print("phone no has less than 12 digits")
                dispatcher.utter_message(
                    text="I'm afraid its an invalid Phone Number, please enter a valid Phone Number")
                return {"slot_ec_get_update_phone_no": None}

    def validate_slot_ec_get_update_email_id(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        print(value)
        print(type(value))
        if "list" in str(type(value)):
            print("inside update email id, type is list")
            if re.search(regex, value[0]):
                return {"slot_ec_get_update_email_id": value[0]}
            else:
                dispatcher.utter_message(template="utter_wrong_email_id")
                # validation failed, set slot to None
                return {"slot_ec_get_update_email_id": None}
        else:
            print("inside update email id, type is string")
            if re.search(regex, value):
                return {"slot_ec_get_update_email_id": value}
            else:
                dispatcher.utter_message(template="utter_wrong_email_id")
                # validation failed, set slot to None
                return {"slot_ec_get_update_email_id": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        print("ec_update_details_form")
        return []


class ECUpdatePhoneNo(Action):
    def name(self) -> Text:
        return "action_existing_customer_update_phone_no"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> str:
        print("action_existing_customer_update_phone_no")
        newPhoneNo = tracker.get_slot("slot_ec_get_update_phone_no")
        oldPhoneNo = tracker.get_slot("phone_no")
        write_into_db.update_customer_phone_no(oldPhoneNo, newPhoneNo)
        dispatcher.utter_message(text="Phone Number Updated successfully")
        dispatcher.utter_message(template="utter_ask_anything_else")
        return []


class ECUpdateEmailAddress(Action):
    def name(self) -> Text:
        return "action_existing_customer_update_email_address"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> str:
        print("action_existing_customer_update_email_address")
        newEmailId = tracker.get_slot("slot_ec_get_update_email_id")
        print("new mail id : ")
        print(newEmailId)
        phone_no = tracker.get_slot("phone_no")
        write_into_db.update_customer_email_id(phone_no, newEmailId)
        dispatcher.utter_message(text="Email Address Updated successfully")
        dispatcher.utter_message(template="utter_ask_anything_else")
        return []


class NamePhoneNoForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "name_phoneno_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["customer_name", "phone_no"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "customer_name": [self.from_entity(entity="customer_name", intent="give_name"), self.from_text()],
            "phone_no": [self.from_entity(entity="phone", intent="give_phoneno"), self.from_text()]
        }

    # USED FOR DOCS: do not rename without updating in docs

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_phone_no(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        #regexNum = "^(\d{12,14})$"
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        print(len(value))
        print(value)
        print(type(value))
        if "list" in str(type(value)):
            print("list is present, inside if condition")
            if 12 <= len(value[0]) <= 14:
                #re.search(regexNum, value[0]) , "+" in value[0], value[0] = value[0][1:]
                if (regex.search(value[0]) == None):
                    if "+" in value[0]:
                        print("phone no has plus symbol")
                        value[0] = value[0][1:]
                    if value[0].isdigit():
                        return {"phone_no": value[0]}
                    else:
                        print("phone no has string characters")
                        dispatcher.utter_message(text="Please enter numeric digits only for the Phone Numbers")
                        return {"phone_no": None}
                else:
                    print("phone no has special characters")
                    dispatcher.utter_message(text="Please enter numeric digits only for the Phone Number")
                    return {"phone_no": None}
            elif len(value[0]) > 14:
                print("phone no has more than 14 digits")
                dispatcher.utter_message(text="I'm afraid its an invalid Phone Number, please enter a valid Phone Number")
                return {"phone_no": None}
            elif len(value[0]) < 12:
                print("phone no has less than 12 digits")
                dispatcher.utter_message(text="I'm afraid its an invalid Phone Number, please enter a valid Phone Number")
                return {"phone_no": None}
        else:
            print("list is not present, inside else condition")
            if 12 <= len(value) <= 14:
                if (regex.search(value) == None):
                    if "+" in value:
                        print("phone no has plus symbol")
                        value = value[1:]
                    if value.isdigit():
                        return {"phone_no": value}
                    else:
                        print("phone no has string characters")
                        dispatcher.utter_message(text="Please enter numeric digits only for the Phone Number")
                        return {"phone_no": None}
                else:
                    print("phone no has special characters")
                    dispatcher.utter_message(text="Please enter numeric digits only for the Phone Number")
                    return {"phone_no": None}
            elif len(value) > 14:
                print("phone no has more than 14 digits")
                dispatcher.utter_message(text="I'm afraid its an invalid Phone Number, please enter a valid Phone Number")
                return {"phone_no": None}
            elif len(value[0]) < 12:
                print("phone no has less than 12 digits")
                dispatcher.utter_message(text="I'm afraid its an invalid Phone Number, please enter a valid Phone Number")
                return {"phone_no": None}

    def validate_customer_name(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        regexName = "^[a-zA-Z]{3,}(?: [a-zA-Z]+){0,2}$"
        if "list" in str(type(value)):
            if re.search(regexName, value[0]):
                return {"customer_name": value[0]}
            else:
                dispatcher.utter_message(template="utter_wrong_customer_name")
                # validation failed, set slot to None
                return {"customer_name": None}
        else:
            if re.search(regexName, value):
                return {"customer_name": value}
            else:
                dispatcher.utter_message(template="utter_wrong_customer_name")
                # validation failed, set slot to None
                return {"customer_name": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        print(tracker.get_slot("slot_flow"))
        return []


class AgeProfessionForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "age_profession_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["age_slot", "profession_slot"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "profession_slot": [self.from_entity(entity="profession", intent="give_profession"), self.from_text()],
            "age_slot": [self.from_entity(entity="age", intent="age_factor"), self.from_text()]
        }

    # USED FOR DOCS: do not rename without updating in docs

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_profession_slot(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        regexName = "^[a-zA-Z]{2,}(?: [a-zA-Z]+){0,2}$"
        if "list" in str(type(value)):
            if re.search(regexName, value[0]):
                return {"profession_slot": value[0]}
            else:
                dispatcher.utter_message(template="utter_wrong_profession_slot")
                # validation failed, set slot to None
                return {"profession_slot": None}
        else:
            if re.search(regexName, value):
                return {"profession_slot": value}
            else:
                dispatcher.utter_message(template="utter_wrong_profession_slot")
                # validation failed, set slot to None
                return {"profession_slot": None}

    def validate_age_slot(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        #regex = "^(0?[1-9]|[1-9][0-9]|[1][1-9][1-9]|200)$"
        print(value)
        print(type(value))
        print(len(value))
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if "list" in str(type(value)):
            if len(value[0]) <= 3:
                if (regex.search(value[0]) == None):
                    if value[0].isdigit():
                        if int(value[0]) <= 125:
                            return {"age_slot": value[0]}
                        else:
                            dispatcher.utter_message(template="utter_wrong_age_slot")
                            return {"age_slot": None}

                    else:
                        dispatcher.utter_message(text="Age can only have numeric digits")
                        return {"age_slot": None}
                else:
                    print("age has special characters")
                    dispatcher.utter_message(text="Age can only have  numeric digits")
                    return {"age_slot": None}
            else:
                dispatcher.utter_message(template="utter_wrong_age_slot")
                return {"age_slot": None}
        else:
            if len(value) <= 3:
                if (regex.search(value) == None):
                    if value.isdigit():
                        if int(value) <= 125:
                            return {"age_slot": value}
                        else:
                            dispatcher.utter_message(template="utter_wrong_age_slot")
                            return {"age_slot": None}
                    else:
                        dispatcher.utter_message(text="Age can only have numeric digits")
                        return {"age_slot": None}
                else:
                    print("age has special characters")
                    dispatcher.utter_message(text="Age can only have numeric digits")
                    return {"age_slot": None}
            else:
                dispatcher.utter_message(template="utter_wrong_age_slot")
                return {"age_slot": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        return []


class EmailAddressForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "email_address_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["email_id", "address_slot"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "email_id": [self.from_entity(entity="email", intent="give_mail"), self.from_text()],
            "address_slot": [self.from_entity(entity="address", intent="give_address"), self.from_text()],
        }

    # USED FOR DOCS: do not rename without updating in docs

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_email_id(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        if "list" in str(type(value)):
            if re.search(regex, value[0]):
                return {"email_id": value[0]}
            else:
                dispatcher.utter_message(template="utter_wrong_email_id")
                # validation failed, set slot to None
                return {"email_id": None}
        else:
            if re.search(regex, value):
                return {"email_id": value}
            else:
                dispatcher.utter_message(template="utter_wrong_email_id")
                # validation failed, set slot to None
                return {"email_id": None}

    def validate_address_slot(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        regex = "^[#\/.0-9a-zA-Z\s,-]+$"
        print(value)
        print(type(value))
        if "list" in str(type(value)):
            print("inside if, means type is list")
            if re.search(regex, value[0]):
                return {"address_slot": value[0]}
            else:
                dispatcher.utter_message(text="utter_wrong_address_slot")
                # validation failed, set slot to None
                return {"address_slot": None}
        else:
            print("inside else, means type is str")
            if re.search(regex, value):
                return {"address_slot": value}
            else:
                dispatcher.utter_message(template="utter_wrong_address_slot")
                return {"address_slot": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        print(tracker.get_slot("slot_flow"))
        dispatcher.utter_message(template="utter_submit")
        return []


class InsertNewCustomerDetails(Action):

    def name(self) -> Text:
        return "action_insert_new_customer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        customerName = tracker.get_slot("customer_name")
        phoneNo = tracker.get_slot("phone_no")
        ageSlot = tracker.get_slot("age_slot")
        emailId = tracker.get_slot("email_id")
        professionSlot = tracker.get_slot("profession_slot")
        addressSlot = tracker.get_slot("address_slot")
        print(customerName, phoneNo, emailId, professionSlot)
        write_into_db.insert_new_customer(customerName, phoneNo, emailId, ageSlot, professionSlot, addressSlot)
        return []


class CorrectCusInfo(Action):

    def name(self) -> Text:
        return "action_correct_cus_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("customer_name", None), SlotSet("email_id", None), SlotSet("phone_no", None),
                SlotSet("age_slot", None), SlotSet("address_slot", None), SlotSet("profession_slot", None)]


class ActionRestart(Action):

    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [Restarted()]
        #return [SlotSet("customer_name", None), SlotSet("email_id", None), SlotSet("phone_no", None),
                #SlotSet("age_slot", None), SlotSet("profession_slot", None)]


class ResetECPhoneNoSlot(Action):

    def name(self) -> Text:
        return "action_reset_existing_customer_phone_no_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("inside action_reset_existing_customer_phone_no_slot")
        return [SlotSet("slot_ec_phone_no", None)]


class ResetECPolicyNoSlot(Action):

    def name(self) -> Text:
        return "action_reset_existing_customer_policy_no_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("slot_ec_policy_no", None)]


class ResetECOTPSlot(Action):

    def name(self) -> Text:
        return "action_reset_ec_otp_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("slot_ec_otp", None)]


class ResetECUpdatePhoneNoOTPSlot(Action):

    def name(self) -> Text:
        return "action_reset_ec_update_phone_no_otp_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("slot_ec_otp_update_phone_no", None)]


class SendWhatsAppQuotation(Action):

    def name(self) -> Text:
        return "action_send_whatsapp_quotation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phoneNo = tracker.get_slot("phone_no")
        product_name = tracker.get_slot("slot_product")
        print(product_name)
        product_details = write_into_db.get_product_details("totaltariff", product_name)
        if product_details != "Product not found":
            temp = []
            for i in range(0, len(product_details[0])):
                temp.append(str(product_details[0][i]))
            tariff = " ".join(temp)
            whatsapp.sendWhatsapp_text(product_name, tariff, str(phoneNo))
            whatsapp.sendWhatsapp_pdf(str(phoneNo))
            dispatcher.utter_message(text="Quotation has been sent to your WhatsApp!")
        else:
            print(product_details)
        return []


class SendWhatsAppOTPUpdateEmail(Action):

    def name(self) -> Text:
        return "action_send_whatsapp_otp_update_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phoneNo = tracker.get_slot("phone_no")
        write_into_db.insert_otp(phoneNo)
        OTP = write_into_db.get_otp(phoneNo)
        print("inside action_send_whatsapp_otp_update_email")
        print(OTP)
        whatsapp.sendWhatsapp_otp(str(phoneNo), str(OTP))
        return []


class ECUpdateEmailWhatsAppOTPForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ec_whatsapp_otp_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["slot_ec_otp_update_email_address"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "slot_ec_otp_update_email_address": [
                self.from_entity(
                    entity="otp", intent=["one_time_pass"]
                )
            ]
        }

    # USED FOR DOCS: do not rename without updating in docs

    def validate_slot_ec_otp(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        regexNum = "^[0-9]{6}$"
        print(value)
        print(type(value))
        if "list" in str(type(value)):
            print("inside if, type is list")
            if re.search(regexNum, value[0]):
                print("regex is matched")
                return {"slot_ec_otp": value[0]}
            else:
                dispatcher.utter_message(template="utter_wrong_slot_ec_otp")
                # validation failed, set slot to None
                return {"slot_ec_otp": None}
        else:
            print("inside else, type is string")
            if re.search(regexNum, value):
                print("regex is matched")
                return {"slot_ec_otp": value}
            else:
                dispatcher.utter_message(template="utter_wrong_slot_ec_otp")
                # validation failed, set slot to None
                return {"slot_ec_otp": None}

    def validate_slot_ec_otp_update_email_address(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        regexNum = "^[0-9]{6}$"
        print(value)
        print(type(value))
        if "list" in str(type(value)):
            if re.search(regexNum, value[0]):
                return {"slot_ec_otp_update_email_address": value[0]}
            else:
                dispatcher.utter_message(template="utter_wrong_slot_ec_otp_update_email_address")
                return {"slot_ec_otp_update_email_address": None}
        else:
            if re.search(regexNum, value):
                return {"slot_ec_otp_update_email_address": value}
            else:
                dispatcher.utter_message(template="utter_wrong_slot_ec_otp_update_email_address")
                return {"slot_ec_otp_update_email_address": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        print("ec_whatsapp_otp_form")
        return []


class SetSlotFlowNewCustomer(Action):

    def name(self) -> Text:
        return "action_set_slot_flow_buy_policy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action_set_slot_flow_buy_policy")
        return [SlotSet("slot_flow", "Buy Policy"), SlotSet("slot_ec_flow", "Buy Policy")]


class SetSlotUpdateDetails(Action):

    def name(self) -> Text:
        return "action_set_slot_update_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("inside slot setting update details :")
        return [SlotSet("slot_update_details", "Update Phone No")] #, FollowupAction("ec_update_details_form")]


class SetSlotUpdateDetailsAsEmail(Action):

    def name(self) -> Text:
        return "action_set_slot_update_details_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("inside slot setting update details email_Id :")
        return [SlotSet("slot_update_details", "Update Email Id")] #, FollowupAction("ec_update_details_form")]


class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet", tracker)
        return [UserUtteranceReverted()]


class ActionOutOfScope(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_out_of_scope"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_out_of_scope", tracker)
        return [UserUtteranceReverted()]


class ActionThank(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_thankyou"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_noworries", tracker)
        return [UserUtteranceReverted()]


class ActionAffirm(Action):

    def name(self) -> Text:
        return "action_affirm"

    @staticmethod
    def get_latest_intent(events):
        actions = []
        for i in range(0, len(events)):
            try:
                if events[i]['event'] == 'action':
                    actions.append(events[i])
            except:
                try:
                    if events[i]['ev ent'] == 'action':
                        actions.append(events[i])
                except:
                    if events[i]['eve nt'] == 'action':
                        actions.append(events[i])
        if actions[-2:][0]['name'] == 'action_listen':
            previous_action_to_be_triggered = actions[-3:][0]['name']
        else:
            previous_action_to_be_triggered = actions[-2:][0]['name']
        print(previous_action_to_be_triggered)
        return previous_action_to_be_triggered


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        previous_action_to_be_triggered = self.get_latest_intent(tracker.events)
        try:
            next_to_be_triggered = Intents.affirm_intents(previous_action_to_be_triggered)
            for i in next_to_be_triggered:
                if "action" not in i and "form{'name'" in i and "form" not in i:
                    print("inside if :" + i)
                    dispatcher.utter_template(i, tracker)
                else:
                    print("inside else :" + i)
                    return [FollowupAction(i)]
            return []
        except:
            dispatcher.utter_message(text="Sorry I did not understand. Please contact the administrator")
            return []


class ActionDeny(Action):

    def name(self) -> Text:
        return "action_deny"

    @staticmethod
    def get_latest_intent(events):
        actions = []
        for i in range(0, len(events)):
            try:
                if events[i]['event'] == 'action':
                    actions.append(events[i])
            except:
                try:
                    if events[i]['ev ent'] == 'action':
                        actions.append(events[i])
                except:
                    if events[i]['eve nt'] == 'action':
                        actions.append(events[i])
        if actions[-2:][0]['name'] == 'action_listen':
            previous_action_to_be_triggered = actions[-3:][0]['name']
        else:
            previous_action_to_be_triggered = actions[-2:][0]['name']
        print(previous_action_to_be_triggered)
        return previous_action_to_be_triggered


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        previous_action_to_be_triggered = self.get_latest_intent(tracker.events)
        try:
            next_to_be_triggered = Intents.deny_intents(previous_action_to_be_triggered)
            for i in next_to_be_triggered:
                if "action" not in i and "form{'name'" in i and "form" not in i:
                    print("inside if :" + i)
                    dispatcher.utter_template(i, tracker)
                else:
                    print("inside else :" + i)
                    return [FollowupAction(i)]
            return []
        except:
            dispatcher.utter_message(text="Sorry I did not understand. Please contact the administrator")
            return []


class ActionPhoneNoIntent(Action):

    def name(self) -> Text:
        return "action_phone_no_intent"

    @staticmethod
    def get_latest_intent(events):
        actions = []
        for i in range(0, len(events)):
            try:
                if events[i]['event'] == 'action':
                    actions.append(events[i])
            except:
                try:
                    if events[i]['ev ent'] == 'action':
                        actions.append(events[i])
                except:
                    if events[i]['eve nt'] == 'action':
                        actions.append(events[i])
        if actions[-2:][0]['name'] == 'action_listen':
            previous_action_to_be_triggered = actions[-3:][0]['name']
        else:
            previous_action_to_be_triggered = actions[-2:][0]['name']
        print(previous_action_to_be_triggered)
        return previous_action_to_be_triggered


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        previous_action_to_be_triggered = self.get_latest_intent(tracker.events)
        try:
            next_to_be_triggered = Intents.phone_no_intents(previous_action_to_be_triggered)
            for i in next_to_be_triggered:
                if "action" not in i and "form{'name'" in i and "form" not in i:
                    print("inside if :" + i)
                    dispatcher.utter_template(i, tracker)
                else:
                    print("inside else :" + i)
                    return[FollowupAction(i)]
            return []
        except:
            dispatcher.utter_message(text="Sorry I did not understand. Please contact the administrator")
            return []



'''class ActionDefaultAskAffirmation(Action):

    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        # get the most likely intent
        last_intent_name = tracker.latest_message['intent']['name']
        print(last_intent_name)
        # get the prompt for the intent

        intent_prompt = Intents.intents(last_intent_name)

        # Create the affirmation message and add two buttons to it.
        # Use '/<intent_name>' as payload to directly trigger '<intent_name>'
        # when the button is clicked.
        message = "Did you mean '{}'?".format(intent_prompt)
        buttons = [{'title': 'Yes',
                    'payload': '/{}'.format(last_intent_name)},
                   {'title': 'No',
                    'payload': '/out_of_scope'}]
        dispatcher.utter_button_message(message, buttons=buttons)

        return [] '''

