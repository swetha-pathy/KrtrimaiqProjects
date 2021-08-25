from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import base64
import uuid
import psycopg2
import psycopg2.extras

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/upload', methods=['POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        image = request.files['file']
        phone_no = request.form['phone']
        image_string = base64.b64encode(image.read())

        psycopg2.extras.register_uuid()
        conn = psycopg2.connect(host="164.52.202.154", database="rasa_insurance", user="rasa_insurance",
                                password="rasa")
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("select customer_id from customerdetails where phoneno = %s" % (phone_no))
        records = cur.fetchall()
        print(cur.mogrify("select customer_id from customerdetails where phoneno = %s" % (phone_no)))
        length = len(records)
        if length == 1:
            print("inside insert documents")
            cur.execute("insert into documentdetails(document_id, customer_id, pan_aadhar)" +
                        "VALUES(%s, %s, %s)", (
                            uuid.uuid4(), records[0][0], image_string))
            conn.commit()
            # close the communication with the PostgresQL database
            cur.close()
            return "Row inserted"
        else:
            return "Customer does not exist"


@app.route('/webcam', methods=['POST'])
@cross_origin()
def webcam_upload():
    if request.method == 'POST':
        image = request.form['image_data']
        phone_no = request.form['phone']
        psycopg2.extras.register_uuid()
        conn = psycopg2.connect(host="164.52.202.154", database="rasa_insurance", user="rasa_insurance",
                                password="rasa")
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("select customer_id from customerdetails where phoneno = %s" % (phone_no))
        records = cur.fetchall()
        length = len(records)
        if length == 1:
            print("inside insert documents")
            cur.execute("insert into documentdetails(document_id, customer_id, pan_aadhar)" +
                        "VALUES(%s, %s, %s)", (
                            uuid.uuid4(), records[0][0], image))
            conn.commit()
        #     close the communication with the PostgresQL database
            cur.close()
            return "Row inserted"
        else:
            return "Customer does not exist"


@app.route('/upload_policy_number', methods=['POST'])
@cross_origin()
def upload_file_policy_number():
    if request.method == 'POST':
        image = request.files['file']
        image_string = base64.b64encode(image.read())
        policy_num = request.form['policy_number']
        # print(image)
        policy_number = "'{0}'".format(policy_num)
        psycopg2.extras.register_uuid()
        conn = psycopg2.connect(host="164.52.202.154", database="rasa_insurance", user="rasa_insurance",
                                password="rasa")
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("select customer_id from policydetails where policy_number = %s" % (policy_number))
        records = cur.fetchall()
        length = len(records)
        if length == 1:
            cur.execute("insert into documentdetails(document_id, customer_id, pan_aadhar)" +
                        "VALUES(%s, %s, %s)", (uuid.uuid4(), records[0][0], image_string))
            conn.commit()
        #     close the communication with the PostgresQL database
            cur.close()
            return "Row inserted"
        else:
            return "Customer does not exist"


@app.route('/webcam_policy_number', methods=['POST'])
@cross_origin()
def webcam_upload_policy_number():
    if request.method == 'POST':
        image = request.form['image_data']
        policy_num = request.form['policy_number']
        policy_number = "'{0}'".format(policy_num)
        psycopg2.extras.register_uuid()
        conn = psycopg2.connect(host="164.52.202.154", database="rasa_insurance", user="rasa_insurance",
                                password="rasa")
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("select customer_id from policydetails where policy_number = %s" % (policy_number))
        records = cur.fetchall()
        length = len(records)
        if length == 1:
            cur.execute("insert into documentdetails(document_id, customer_id, pan_aadhar)" +
                        "VALUES(%s, %s, %s)", (
                            uuid.uuid4(), records[0][0], image))
            conn.commit()
        #     close the communication with the PostgresQL database
            cur.close()
            return "Row inserted"
        else:
            return "Customer does not exist"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
