GlobalDB = {}
IDTOuser = {}
""" GlobalDB={
    chat_id:{
    membersID:[],
    userIsGay:0
    nowDay:0
    id_thePIDOR: 
    }
} 
    IDTOuser={id_int:username}
  """
class reg_user:

    def reg_user_0(self):
        global GlobalDB
        global IDTOuser

        GlobalDB.update({self.chatID:dict({"membersID":[]})})
        GlobalDB[self.chatID]["membersID"].append(self.id_int)
        IDTOuser.update({self.id_int:self.username_str})
        GlobalDB[self.chatID].update({self.id_int:0})
        GlobalDB[self.chatID].update({"nowDay":None})
        GlobalDB[self.chatID].update({"id_thePIDOR":0})

        text_msg_answer = 'User added '+str(GlobalDB) + '''
        соответстиве id - username 

        '''+str(IDTOuser)
        return text_msg_answer

    def reg_user_1(self):
        global GlobalDB
        global IDTOuser

        GlobalDB[self.chatID]["membersID"].append(self.id_int)
        IDTOuser.update({self.id_int:self.username_str})
        GlobalDB[self.chatID].update({self.id_int:0})

        text_msg_answer = 'User added '+str(GlobalDB) + '''
        соответстиве id - username 

        '''+str(IDTOuser)
        return text_msg_answer
    
    def reg_user_2(self):
        global IDTOuser
        IDTOuser.update({self.id_int:self.username_str})

        text_msg_answer = 'User added '+str(GlobalDB) + '''
        соответстиве id - username 

        '''+str(IDTOuser)
        return text_msg_answer

    def choose_method(self, value):
        method_name = "reg_user_"+str(value)
        method = getattr(self, method_name)
        return method()
    

call_reg_user = reg_user()



def check_user(chatID, id_int, username_str):

    choose_reg_method = 0

    bool_p1=chatID in GlobalDB.keys()
    choose_reg_method = choose_reg_method + bool_p1

    try:
        bool_p1=id_int in GlobalDB[chatID]["membersID"]  
    except KeyError:
        bool_p1 =False
        choose_reg_method=choose_reg_method+bool_p1

    call_reg_user.chatID = chatID
    call_reg_user.id_int = id_int
    call_reg_user.username_str = username_str
    
    return call_reg_user.choose_method(choose_reg_method)

def updateDB_thePIDOR(chat_int, id_int):
    global GlobalDB

    GlobalDB[chat_int][id_int] = GlobalDB[chat_int][id_int]+1
    GlobalDB
    return "Succes update"+str(GlobalDB)