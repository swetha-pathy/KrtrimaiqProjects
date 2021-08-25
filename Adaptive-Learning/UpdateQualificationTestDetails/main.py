import os
import psycopg2.extras
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
        userLevel = data['UserLevel']
        percentLevel = data['PercentLevel']
        subject = data['Subject']
        boarditem = data['BoardItem']
        board = data['Board']
        totalQues = data['TotalQues']

        boardid, boarditemid, subjectid = getBoardBoardItemSubjectIds(board, boarditem, subject)

        cur.execute("UPDATE dev.userlevel "
                    "SET quescomp = %s, totalques = %s where subjectid = %s and levelname = %s "
                    "and boardid = %s and boarditemid = %s;"
                    % ("'" + percentLevel + "'",  totalQues, "'" + subjectid + "'", "'" + userLevel + "'",
                       "'" + boardid + "'", "'" + boarditemid + "'"))

        userLevelDetails = viewUserLevelRows(boardid, boarditemid, subjectid)

        return (userLevelDetails,  200, headers)
    else:
        return ("User Level Updation Failed. Please try again!",  200, headers)