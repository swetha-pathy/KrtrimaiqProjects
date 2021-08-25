import psycopg2
import psycopg2.extras
import json
import re
from uuid import UUID

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


def getPercentage(percent, totalQuestions):
    return round((percent / 100) * totalQuestions)


def getBoardBoardItemSubjectIds(board, boarditem, subject):
    psycopg2.extras.register_uuid()
    conn = psycopg2.connect(host="164.52.202.154", database="AdaptiveLearning", user="rasa_insurance",
                            password="rasa")
    cur = conn.cursor()

    cur.execute("SELECT boardid FROM dev.board where boardname = %s" % ("'" + board + "'"))
    boardid = json.dumps(cur.fetchall(), cls=UUIDEncoder)
    boardid = re.findall(r'"([^"]*)"', boardid)
    boardid = boardid[0]

    cur.execute("SELECT boarditemid FROM dev.boarditem where boardid = %s and boarditem = %s" % (
        "'" + boardid + "'", "'" + boarditem + "'"))
    boarditemid = json.dumps(cur.fetchall(), cls=UUIDEncoder)
    boarditemid = re.findall(r'"([^"]*)"', boarditemid)
    boarditemid = boarditemid[0]

    cur.execute("SELECT subjectid FROM dev.subjects where boarditemid = %s and subjectname = %s" % (
        "'" + boarditemid + "'", "'" + subject + "'"))
    subjectid = json.dumps(cur.fetchall(), cls=UUIDEncoder)
    subjectid = re.findall(r'"([^"]*)"', subjectid)
    subjectid = subjectid[0]

    return boardid, boarditemid, subjectid


def generateQuestions(easyPct, mediumPct, hardPct, subject, noOfQuestions, board, boarditem, chapter):
    psycopg2.extras.register_uuid()
    conn = psycopg2.connect(host="164.52.202.154", database="AdaptiveLearning", user="rasa_insurance",
                            password="rasa")
    cur = conn.cursor()

    # execute the INSERT statement
    total = int(easyPct) + int(mediumPct) + int(hardPct)
    if total == 100:
        easyNoOfQuestions = str(getPercentage(int(easyPct), int(noOfQuestions)))
        mediumNoOfQuestions = str(getPercentage(int(mediumPct), int(noOfQuestions)))
        hardNoOfQuestions = str(getPercentage(int(hardPct), int(noOfQuestions)))

        temp_totalQues = int(easyNoOfQuestions) + int(mediumNoOfQuestions) + int(hardNoOfQuestions)

        if temp_totalQues != int(noOfQuestions):
            if temp_totalQues > int(noOfQuestions):
                temp = temp_totalQues - int(noOfQuestions)
                easyNoOfQuestions = str(int(easyNoOfQuestions) - temp)
            elif temp_totalQues < int(noOfQuestions):
                temp = int(noOfQuestions) - temp_totalQues
                easyNoOfQuestions = str(int(easyNoOfQuestions) + temp)

        boardid, boarditemid, subjectid = getBoardBoardItemSubjectIds(board, boarditem, subject)

        if chapter != "null":

            cur.execute("SELECT chapterid FROM dev.chapter where subjectid = %s and chaptername = %s",
                        (subjectid, chapter))
            chapterid = json.dumps(cur.fetchall(), cls=UUIDEncoder)
            chapterid = re.findall(r'"([^"]*)"', chapterid)
            chapterid = chapterid[0]

            cur.execute("SELECT questionid, questiontext, typeofques, options, noofsubques FROM dev.ques where complexity = 'Easy'"
                        "and boardid = %s and boarditemid = %s and subjectid = %s and chapterid = %s ORDER BY RANDOM() LIMIT %s"
                        % ("'" + boardid + "'", "'" + boarditemid + "'", "'" + subjectid + "'", "'" + chapterid + "'", easyNoOfQuestions))
            easy_result = json.dumps(cur.fetchall(), cls=UUIDEncoder)

            cur.execute("SELECT questionid, questiontext, typeofques, options, noofsubques FROM dev.ques where complexity = 'Medium'"
                        "and boardid = %s and boarditemid = %s and subjectid = %s and chapterid = %s ORDER BY RANDOM() LIMIT %s"
                        % ("'" + boardid + "'", "'" + boarditemid + "'", "'" + subjectid + "'", "'" + chapterid + "'", mediumNoOfQuestions))
            medium_result = json.dumps(cur.fetchall(), cls=UUIDEncoder)

            cur.execute("SELECT questionid, questiontext, typeofques, options, noofsubques FROM dev.ques where complexity = 'Hard'"
                        "and boardid = %s and boarditemid = %s and subjectid = %s and chapterid = %s ORDER BY RANDOM() LIMIT %s"
                        % ("'" + boardid + "'", "'" + boarditemid + "'", "'" + subjectid + "'", "'" + chapterid + "'", hardNoOfQuestions))
            hard_result = json.dumps(cur.fetchall(), cls=UUIDEncoder)
        else:
            cur.execute("SELECT questionid, questiontext, typeofques, options, noofsubques FROM dev.ques where complexity = 'Easy'"
                        "and boardid = %s and boarditemid = %s and subjectid = %s ORDER BY RANDOM() LIMIT %s"
                        % ("'" + boardid + "'", "'" + boarditemid + "'", "'" + subjectid + "'", easyNoOfQuestions))
            easy_result = json.dumps(cur.fetchall(), cls=UUIDEncoder)

            cur.execute("SELECT questionid, questiontext, typeofques, options, noofsubques FROM dev.ques where complexity = 'Medium'"
                        "and boardid = %s and boarditemid = %s and subjectid = %s ORDER BY RANDOM() LIMIT %s"
                        % ("'" + boardid + "'", "'" + boarditemid + "'", "'" + subjectid + "'", mediumNoOfQuestions))
            medium_result = json.dumps(cur.fetchall(), cls=UUIDEncoder)

            cur.execute("SELECT questionid, questiontext, typeofques, options, noofsubques FROM dev.ques where complexity = 'Hard'"
                        "and boardid = %s and boarditemid = %s and subjectid = %s ORDER BY RANDOM() LIMIT %s"
                        % ("'" + boardid + "'", "'" + boarditemid + "'", "'" + subjectid + "'", hardNoOfQuestions))
            hard_result = json.dumps(cur.fetchall(), cls=UUIDEncoder)

        result = easy_result[:-2] + "," + medium_result[2:-2] + "," + hard_result[2:]
        result_temp = re.findall(r'"([^"]*)"', result)
        result_main_list = [result_temp[n:n + 5] for n in range(0, len(result_temp), 5)]
        key_list = ["QuestionId", "Question", "TypeOfQuestion", "Options", "NoOfSubQuestions"]
        main_list = []
        for i in range(0, len(result_main_list)):
            temp_dict = {}
            for key in key_list:
                for value in result_main_list[i]:
                    temp_dict[key] = value
                    result_main_list[i].remove(value)
                    break
            main_list.append(temp_dict)
        questions = {"Questions": main_list}
        # close the communication with the PostgresQL database
        cur.close()
    else:
        questions = "Total Percentage do not add upto 100. Please input right percentages"

    return questions


def getUserLevel(correctAnsDict, wrongAnsDict, totalQues):
    hard = correctAnsDict['correct_hard'] + wrongAnsDict['wrong_hard']
    if hard != 0:
        hardPercentage = (correctAnsDict['correct_hard']/hard) * 100
    else:
        hardPercentage = 0
    medium = correctAnsDict['correct_medium'] + wrongAnsDict['wrong_medium']
    if medium != 0:
        mediumPercentage = (correctAnsDict['correct_medium'] / medium) * 100
    else:
        mediumPercentage = 0
    if hardPercentage >= 75:
        level = 'Advanced'
    elif mediumPercentage >= 75:
        level = 'Intermediate'
    else:
        level = 'Beginner'
    return level


def getUserLevelNew(correctCount, totalCount, boardid, boarditemid, subjectid):
    psycopg2.extras.register_uuid()
    conn = psycopg2.connect(host="164.52.202.154", database="AdaptiveLearning", user="rasa_insurance",
                            password="rasa")
    cur = conn.cursor()
    cur.execute("select levelname, minpctvalue, maxpctvalue from dev.userlevel where levelname <> 'NotAssessed'"
                "and boardid = %s and boarditemid = %s and subjectid = %s"
                %("'" + boardid + "'", "'" + boarditemid + "'", "'" + subjectid + "'"))
    min_max = json.dumps(cur.fetchall(), cls=UUIDEncoder)
    min_max = re.findall(r'"([^"]*)"', min_max)
    min_max_list = [min_max[n:n + 3] for n in range(0, len(min_max), 3)]

    print(min_max_list)

    name_min_max_dict = {}
    for name, minpct, maxpct in min_max_list:
        name_min_max_dict[name] = {"MinPct": int(minpct), "MaxPct": int(maxpct)}

    print(name_min_max_dict)
    percentage = (correctCount / totalCount) * 100

    if percentage >= name_min_max_dict['Advanced']['MinPct'] and percentage <= name_min_max_dict['Advanced']['MaxPct']:
        level = 'Advanced'
    elif percentage >= name_min_max_dict['Intermediate']['MinPct'] and percentage <= name_min_max_dict['Intermediate']['MaxPct']:
        level = 'Intermediate'
    elif percentage >= name_min_max_dict['Beginner']['MinPct'] and percentage <= name_min_max_dict['Beginner']['MaxPct']:
        level = 'Beginner'
    return level


def genQuesBasedOnUserLevel(userLevel, board, boarditem, subject):
    psycopg2.extras.register_uuid()
    conn = psycopg2.connect(host="164.52.202.154", database="AdaptiveLearning", user="rasa_insurance",
                            password="rasa")
    cur = conn.cursor()

    boardid, boarditemid, subjectid = getBoardBoardItemSubjectIds(board, boarditem, subject)

    cur.execute("select quescomp, totalques from dev.userlevel where levelname = %s and "
                "boardid = %s and boarditemid = %s and subjectid = %s"
                % ("'" + userLevel + "'", "'" + boardid + "'", "'" + boarditemid + "'", "'" + subjectid + "'"))
    record = json.dumps(cur.fetchall(), cls=UUIDEncoder)
    record = re.findall(r'"([^"]*)"', record)
    print(record)

    quesComp = record[0]
    quesComp = quesComp.split(';')

    easyPct = quesComp[0]
    mediumPct = quesComp[1]
    hardPct = quesComp[2]

    noOfQuestions = record[1]
    return easyPct, mediumPct, hardPct, noOfQuestions


def viewUserLevelRows(boardid, boarditemid, subjectid):
    psycopg2.extras.register_uuid()
    conn = psycopg2.connect(host="164.52.202.154", database="AdaptiveLearning", user="rasa_insurance",
                            password="rasa")
    cur = conn.cursor()

    cur.execute("select levelname, quescomp, totalques from dev.userlevel where boardid = %s and "
                "boarditemid = %s and subjectid = %s"
                % ("'" + boardid + "'", "'" + boarditemid + "'", "'" + subjectid + "'"))
    userlevels = json.dumps(cur.fetchall(), cls=UUIDEncoder)
    userlevels = re.findall(r'"([^"]*)"', userlevels)
    userlevels_list = [userlevels[n:n + 3] for n in range(0, len(userlevels), 3)]
    key_list = ["LevelName", "QuesComp", "TotalQuestions"]
    userlevels_main_list = []

    for i in range(0, len(userlevels_list)):
        temp_dict = {}
        for key in key_list:
            for value in userlevels_list[i]:
                temp_dict[key] = value
                userlevels_list[i].remove(value)
                break
        userlevels_main_list.append(temp_dict)
    for i in range(0, len(userlevels_main_list)):
        temp_key = ["Easy", "Medium", "Hard"]
        temp_string_list = userlevels_main_list[i]['QuesComp'].split(';')
        temp_dict = {}
        for key in temp_key:
            for value in temp_string_list:
                temp_dict[key] = value
                temp_string_list.remove(value)
                break
        userlevels_main_list[i]['QuesComp'] = temp_dict

    userLevel_dict = dict()
    userLevel_dict['TableDetails'] = userlevels_main_list

    return userLevel_dict


def viewUserLevelPctRows(boardid, boarditemid, subjectid):
    psycopg2.extras.register_uuid()
    conn = psycopg2.connect(host="164.52.202.154", database="AdaptiveLearning", user="rasa_insurance",
                            password="rasa")
    cur = conn.cursor()

    cur.execute("select levelname, minpctvalue, maxpctvalue from dev.userlevel "
                "where boardid = %s and boarditemid = %s and subjectid = %s"
                % ("'" + boardid + "'", "'" + boarditemid + "'", "'" + subjectid + "'"))
    userlevelPcts = json.dumps(cur.fetchall(), cls=UUIDEncoder)
    userlevelPcts = re.findall(r'"([^"]*)"', userlevelPcts)
    userlevelPcts_list = [userlevelPcts[n:n + 3] for n in range(0, len(userlevelPcts), 3)]

    key_list = ["LevelName", "MinPctValue", "MaxPctValue"]
    userlevelPcts_main_list = []

    for i in range(0, len(userlevelPcts_list)):
        temp_dict = {}
        for key in key_list:
            for value in userlevelPcts_list[i]:
                temp_dict[key] = value
                userlevelPcts_list[i].remove(value)
                break
        userlevelPcts_main_list.append(temp_dict)
    userlevelPcts_dict = dict()
    userlevelPcts_dict['TableDetails'] = userlevelPcts_main_list

    return userlevelPcts_dict
