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
        subject = request.form['Subject']
        boarditem = request.form['BoardItem']
        board = request.form['Board']
        boardid, boarditemid, subjectid = getBoardBoardItemSubjectIds(board, boarditem, subject)
        data = viewUserLevelRows(boardid, boarditemid, subjectid)
        return (data, 200, headers)   
            
    else:
        return (200, headers)

    