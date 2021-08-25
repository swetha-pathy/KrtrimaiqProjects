import os
import psycopg2.extras
import pandas as pd
import json
import re
from utils.helper import *

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "kr-adaptivelearning-gcp-key.json"

def handler(request):

    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': 'Content-Type, Content-Disposition'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    psycopg2.extras.register_uuid()
    conn = psycopg2.connect(host="164.52.202.154", database="AdaptiveLearning", user="rasa_insurance",
                            password="rasa")
    cur = conn.cursor()
    file = request.files['StgFile']
    emailId = request.form['EmailId']
    cur.execute('select userid from dev.users where emailid = %s' % ("'" + emailId + "'"))
    userId = json.dumps(cur.fetchall(), cls=UUIDEncoder)
    userId = re.findall(r'"([^"]*)"', userId)
    print(userId)
    df = pd.read_csv(file, encoding="latin1")
    df['userid'] = userId[0]

    cur.execute('delete from dev.stg_raw where userid = %s' % ("'" + userId[0] + "'"))

    if len(df) > 0:
        df_columns = list(df)
        # create (col1,col2,...)
        columns = ",".join(df_columns)

        # create VALUES('%s', '%s",...) one '%s' per column
        values = "VALUES({})".format(",".join(["%s" for _ in df_columns]))

        # create INSERT INTO table (columns) VALUES('%s',...)
        insert_stmt = "INSERT INTO {} ({}) {}".format('dev.stg_raw', columns, values)

        psycopg2.extras.execute_batch(cur, insert_stmt, df.values)

        cur.execute("CALL dev.insertquesdata()")

        conn.commit()

    cur.close()
    return ("Data Inserted into Questions Table Successfully",  200, headers)
