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
        userLevel = request.form['UserLevel']
        subject = request.form['Subject']
        boarditem = request.form['BoardItem']
        board = request.form['Board']
        chapter = request.form['Chapter']
        easyPct, mediumPct, hardPct, noOfQuestions = genQuesBasedOnUserLevel(userLevel, board, boarditem, subject)
        questions = generateQuestions(easyPct, mediumPct, hardPct, subject, noOfQuestions, board, boarditem, chapter)
        return (questions,  200, headers)
    else:
        return ("Questions retrieval Failed. Please try again!",  200, headers)