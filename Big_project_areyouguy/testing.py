
chatID='64747'
GlobalDB = {
    chatID:{
        "memberID":[],
        "memberIDgay":2,
    },
    "chatID2":{
        "memberID":[],
        "memberIDgay":0,
    }
}

GlobalDB['64747']["memberID"].append(54456)
GlobalDB['64747']["memberID"].append(838)
GlobalDB["64747"]["memberID"].append(54455546)
GlobalDB["64747"]["memberIDgay"] = GlobalDB["64747"]["memberIDgay"]+True

print(GlobalDB)

GlobalDB2 = {"chat_id_246464":''}
GlobalDB2["chat_id_246464"] = dict({'fvf':[]})
GlobalDB2["chat_id_246464"]['fvf'].append(435)
GlobalDB2["chat_id_246464"]['fvf'].append(43544)


print(GlobalDB2)
#print(bool1)

class MyVisitor:
    def registr_0(self):
        print(0)

    def register_1(self):
        print(1)

    def register_2(self):
        print(2)

    def dispatch(self, value):
        method_name = 'register_' + str(value)
        method = getattr(self, method_name)
        method()

    Vist = self.dispatch()


Visit('2')

def func():
     print(45)

