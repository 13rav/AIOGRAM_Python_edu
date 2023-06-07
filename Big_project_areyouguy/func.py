GlobalDB = dict()

""" GlobalDB={
    chat_id:{
    membersID:[],
    userIsGay:0
    }
} 
    IDTOuser={id_int:username}
  """

bool1 = 0



def check_user(chatID, id_int, username_str):
    S=chatID in GlobalDB.keys()
    bool1 = bool1 + S

    try:
       S=id_int in GlobalDB[chatID][membersID]
    except KeyError:
        S=False
        bool1=bool1+S
    return bool1

