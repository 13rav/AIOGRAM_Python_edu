GlobalDB = {}
""" GlobalDB={
    chat_id:{
    membersID:[],
    userIsGay:0
    }
} 
    IDTOuser={id_int:username}
  """
class reg_user:

    def reg_user_0(self):
        global GlobalDB
        GlobalDB.update({self.chatID:dict({"membersID":[]})})
        GlobalDB[self.chatID]["membersID"].append(self.id_int)
        text_msg_answer = 'User added'+str(GlobalDB)
        return text_msg_answer

    def reg_user_1(self):
        global GlobalDB
        GlobalDB[self.chatID]["membersID"].append(self.id_int)
        text_msg_answer = 'User added'+str(GlobalDB)
        return text_msg_answer
    
    def reg_user_2(self):
        print(2)

    def choose_method(self, value):
        method_name = "reg_user_"+str(value)
        method = getattr(self, method_name)
        return method()
    

call_reg_user = reg_user()



def check_user(chatID, id_int, username_str):

    bool1 = 0

    S=chatID in GlobalDB.keys()
    bool1 = bool1 + S

    try:
        S=id_int in GlobalDB[chatID]["membersID"]  
    except KeyError:
        S=False
        bool1=bool1+S

    call_reg_user.chatID = chatID
    call_reg_user.id_int = id_int
    call_reg_user.username_str = username_str
    
    return call_reg_user.choose_method(bool1)
    #return record


print(check_user(32234, 54343, 'userhhhe'))

print(check_user(32234, 5434443, 'userhhhe'))