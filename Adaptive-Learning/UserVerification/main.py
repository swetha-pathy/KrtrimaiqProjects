import json
import psycopg2
import psycopg2.extras
import re
import os
from utlis.helper import *

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
    
    if request.method == 'POST':
        emailId = request.form['emailid']
        password = request.form['password']
        psycopg2.extras.register_uuid()
        conn = psycopg2.connect(host="164.52.202.154", database="AdaptiveLearning",  user="rasa_insurance",
                                password="rasa")
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute('select password, userlevelid, usertype, boardid, boarditemid'
                    ' from dev.users where emailid = %s' % ("'" + emailId + "'"))
        records = json.dumps(cur.fetchall(), cls=UUIDEncoder)
        records = re.findall(r'"([^"]*)"', records)
        main_result = dict()
        if records != []:
            if records[0] == password:
                result = "Authentication Successful"
            else:
                result = "Authentication Not Successful"
            cur.execute('select levelname from dev.userlevel where levelid = %s' % ("'" + records[1] + "'"))
            levelname = json.dumps(cur.fetchall())
            levelname = re.findall(r'"([^"]*)"', levelname)
            levelname = levelname[0]
            main_result['UserLevel'] = levelname
            main_result['UserType'] = records[2]
            boardid = records[3]
            boarditemid = records[4]

            cur.execute("SELECT boardname FROM dev.board where boardid = %s" % ("'" + boardid + "'"))
            boardname = json.dumps(cur.fetchall(), cls=UUIDEncoder)
            boardname = re.findall(r'"([^"]*)"', boardname)
            boardname = boardname[0]

            cur.execute("SELECT boarditem FROM dev.boarditem where boarditemid = %s" % ( "'" + boarditemid + "'"))
            boarditemname = json.dumps(cur.fetchall(), cls=UUIDEncoder)
            boarditemname = re.findall(r'"([^"]*)"', boarditemname)
            boarditemname = boarditemname[0]

            main_result['Board'] = boardname
            main_result['BoardItem'] = boarditemname

        else:
            result = "This is not registered User Id. Please contact Administrator"
        main_result['Authentication Status'] = result
        # close the communication with the PostgresQL database
        cur.close()
        return (main_result,  200, headers)
    else:
        return ("User Verification Failed. Please try again!", 200, headers)
       
    