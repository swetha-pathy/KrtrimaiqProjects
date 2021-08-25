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
        emailId = data['emailId']
        subject = data['Subject']
        boarditem = data['BoardItem']
        board = data['Board']
        boardid, boarditemid, subjectid = getBoardBoardItemSubjectIds(board, boarditem, subject)

        cur.execute("select userid from dev.users where emailid = %s" % ("'" + emailId + "'"))
        userId = json.dumps(cur.fetchall(), cls=UUIDEncoder)
        userId = re.findall(r'"([^"]*)"', userId)
        userId = userId[0]

        questionId_list = data['userResponses']
        quesIds = ""
        answerArray = []
        for i in range(0, len(questionId_list)):
            quesIds = quesIds + "," + questionId_list[i]['questionId']
        quesIds = quesIds[1:]
        cur.execute("INSERT INTO dev.quespaper(userid,quesgiven) VALUES (%s, %s)",
                    (userId, quesIds))

        cur.execute("select quespaperid from dev.quespaper where userid = %s "
                    "ORDER BY ansdate DESC LIMIT 1" % ("'" + userId + "'"))
        quespaperid = json.dumps(cur.fetchall(), cls=UUIDEncoder)
        quespaperid = re.findall(r'"([^"]*)"', quespaperid)
        quespaperid = quespaperid[0]

        for i in range(0, len(questionId_list)):
            templist = []
            cur.execute("select correctans from dev.rightans where quesid = %s"
                        % ("'" + questionId_list[i]['questionId'] + "'"))
            rightanswer = cur.fetchall()
            rightanswer = rightanswer[0][0]

            rightanswer = ("".join(rightanswer.split())).lower()
            answerSelected = ("".join(questionId_list[i]['answerSelected'].split())).lower()

            if rightanswer == answerSelected:
                templist.extend([userId, quespaperid, questionId_list[i]['questionId'],
                                 questionId_list[i]['answerSelected'], str(1), boardid, boarditemid])
            else:
                templist.extend([userId, quespaperid, questionId_list[i]['questionId'],
                                 questionId_list[i]['answerSelected'], str(0), boardid, boarditemid])
            answerArray.append(tuple(templist))

        cur.executemany(
            "INSERT INTO dev.userans(userid, quespaperid, quesid, userans, iscorrect, boardid, boarditemid) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s)", answerArray)

        cur.execute("select quesid, complexity from dev.questionsdata where iscorrect = '1' and "
                    "userid = %s and quespaperid = %s " % ("'" + userId + "'", "'" + quespaperid + "'"))

        correct_section = json.dumps(cur.fetchall(), cls=UUIDEncoder)
        correct_section = re.findall(r'"([^"]*)"', correct_section)
        correct_section_list = [correct_section[n:n + 2] for n in range(0, len(correct_section), 2)]
        correct_easy = 0
        correct_medium = 0
        correct_hard = 0
        for i in correct_section:
            if i == 'Easy':
                correct_easy += 1
            elif i == 'Medium':
                correct_medium += 1
            elif i == 'Hard':
                correct_hard += 1
        correct_dict = dict()
        correct_dict['correct_easy'] = correct_easy
        correct_dict['correct_medium'] = correct_medium
        correct_dict['correct_hard'] = correct_hard

        cur.execute("select quesid, complexity from dev.questionsdata where iscorrect = '0' and "
                    "userid = %s and quespaperid = %s " % ("'" + userId + "'", "'" + quespaperid + "'"))

        wrong_section = json.dumps(cur.fetchall(), cls=UUIDEncoder)
        wrong_section = re.findall(r'"([^"]*)"', wrong_section)
        wrong_easy = 0
        wrong_medium = 0
        wrong_hard = 0
        for i in wrong_section:
            if i == 'Easy':
                wrong_easy += 1
            elif i == 'Medium':
                wrong_medium += 1
            elif i == 'Hard':
                wrong_hard += 1
        wrong_dict = dict()
        wrong_dict['wrong_easy'] = wrong_easy
        wrong_dict['wrong_medium'] = wrong_medium
        wrong_dict['wrong_hard'] = wrong_hard

        cur.execute("select quesid, iscorrect, subtopicname from dev.questionsdata where "
                    "userid = %s and quespaperid = %s " % ("'" + userId + "'", "'" + quespaperid + "'"))

        result_section = json.dumps(cur.fetchall(), cls=UUIDEncoder)
        result_section = re.findall(r'"([^"]*)"', result_section)
        result_section_list = [result_section[n:n + 3] for n in range(0, len(result_section), 3)]
        print(result_section_list)
        print("\n")
        key_list = ["QuestionId", "IsCorrect", "SubTopicName"]
        result_section_main_list = []

        for i in range(0, len(result_section_list)):
            temp_dict = {}
            for key in key_list:
                for value in result_section_list[i]:
                    temp_dict[key] = value
                    result_section_list[i].remove(value)
                    break
            result_section_main_list.append(temp_dict)

        # userLevel = getUserLevel(correct_dict, wrong_dict, len(result_section_main_list))

        userLevel = getUserLevelNew(len(correct_section_list), len(result_section_main_list), boardid, boarditemid,
                                    subjectid)

        cur.execute("select levelid from dev.userlevel where levelname = %s "
                    "and boardid = %s and boarditemid = %s and subjectid = %s"
                    % ("'" + userLevel + "'", "'" + boardid + "'", "'" + boarditemid + "'", "'" + subjectid + "'"))
        levelid = json.dumps(cur.fetchall(), cls=UUIDEncoder)
        levelid = re.findall(r'"([^"]*)"', levelid)
        levelid = levelid[0]

        cur.execute(
            "UPDATE dev.users SET userlevelid = %s where emailid = %s" % ("'" + levelid + "'", "'" + emailId + "'"))

        percentage = str((len(correct_section_list) / len(result_section_main_list)) * 100)

        cur.execute("UPDATE dev.quespaper set userscore = %s, userlevelassigned = %s "
                    "where quespaperid = %s and userid = %s"
                    % ("'" + percentage + "'", "'" + userLevel + "'", "'" + quespaperid + "'", "'" + userId + "'"))

        final_dict = dict()
        final_dict['TotalQuestions'] = len(result_section_main_list)
        final_dict['CorrectAnswersCount'] = len(correct_section_list)
        final_dict['CorrectAnswersClassification'] = [correct_dict]
        final_dict['WrongAnswersClassification'] = [wrong_dict]
        final_dict['QuestionIds'] = result_section_main_list
        final_dict['userLevel'] = userLevel

        cur.close()

        return (final_dict, 200, headers)

    else:
        return (200, headers)