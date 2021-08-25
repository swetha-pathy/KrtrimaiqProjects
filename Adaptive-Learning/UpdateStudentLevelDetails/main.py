import json
import psycopg2
import psycopg2.extras
import re
import os
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
    
    if request.method == 'POST':
        psycopg2.extras.register_uuid()
        conn = psycopg2.connect(host="164.52.202.154", database="AdaptiveLearning", user="rasa_insurance",
                                password="rasa")
        conn.autocommit = True
        cur = conn.cursor()

        data = request.get_json()
        subject = data['Subject']
        boarditem = data['BoardItem']
        board = data['Board']
        userPctValue = data['UserPctValue']
        userLevel = ["Beginner", "Intermediate", "Advanced"]

        boardid, boarditemid, subjectid = getBoardBoardItemSubjectIds(board, boarditem, subject)

        for i,j in zip(userPctValue, userLevel):
            minValue  = i.split(';')[0]
            maxValue = i.split(';')[1]
            cur.execute("UPDATE dev.userlevel "
                    "SET minpctvalue = %s, maxpctvalue = %s where levelname = %s and subjectid = %s"
                    "and boardid = %s and boarditemid = %s;"
                    % ("'" + minValue + "'", "'" + maxValue + "'", "'" + j + "'", "'" + subjectid + "'",
                      "'" + boardid + "'", "'" + boarditemid + "'"))

        userLevelPct = viewUserLevelPctRows(boardid, boarditemid, subjectid)

        return (userLevelPct, 200, headers)

    else:
        return ("User Level Updation Failed. Please try again!", 200, headers)