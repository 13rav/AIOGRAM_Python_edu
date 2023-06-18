import random
import datetime, time

#chatID='64747'
""" GlobalDB = {
    chatID:{
        "membersID":[],
        "memberIDgay":2,
    },
    "chatID2":{
        "memberID":[],
        "memberIDgay":0,
    }
} """
GlobalDB = {}
IDTOuser = {234234123421:"user11", 234264364361:"user22", 364364361:"user33", 453788931999335:"user44"}

def update_DB():
    
    global GlobalDB
    GlobalDB.update({"chat1":dict({"membersID":[]})})
    GlobalDB.update({"chat2":dict({"membersID":[]})})

    GlobalDB["chat1"]["membersID"].append(234234123421)
    GlobalDB["chat1"]["membersID"].append(234264364361)
    GlobalDB["chat1"]["membersID"].append(364364361)
    GlobalDB["chat1"]["membersID"].append(453788931999335)

    GlobalDB["chat2"]["membersID"].append(453788931999335)
    GlobalDB["chat2"]["membersID"].append(453799335)
    GlobalDB["chat2"]["membersID"].append(7188723674)
    GlobalDB["chat2"]["membersID"].append(71727843529)
    GlobalDB["chat2"]["membersID"].append(78723674)
    GlobalDB["chat2"]["membersID"].append(834657813)

    GlobalDB["chat1"].update(dict({234234123421:4}))
    GlobalDB["chat1"].update(dict({234264364361:1}))
    GlobalDB["chat1"].update(dict({364364361:1}))
    GlobalDB["chat1"].update(dict({453788931999335:3}))
    print(GlobalDB)

def choose():
    global GlobalDB
    temp_int = random.choice(GlobalDB['chat1']['membersID'])
    GlobalDB['chat1'][temp_int] = GlobalDB['chat1'][temp_int]+1
    print(GlobalDB)

""" for k in GlobalDB['chat1']['membersID']:
    temp_value = k
    print(temp_value)
    print(GlobalDB['chat1'][temp_value])
    print(IDTOuser[temp_value]) """


def add_DB(value):
    global GlobalDB

    GlobalDB["chat1"]["membersID"].append(value)
    GlobalDB["chat1"].update(dict({value:0}))

def checking():
    chatInGlobalDB = GlobalDB.get("chat2")

    try:
        checkMembersID = bool(GlobalDB["messaged"]["membersID"])
    except Exception as er:
        checkMembersID = False

    if chatInGlobalDB is None:
        print("зарегайся в боте")
        return None
    g=324+5
    print(g)


def statistic(chat_int):
    global GlobalDB, IDTOuser
    text=""
    test2 = dict()

    for i in GlobalDB[chat_int]["membersID"]:
        test2.update({i:GlobalDB[chat_int][i]})

    print(test2)

update_DB()
statistic("chat1")