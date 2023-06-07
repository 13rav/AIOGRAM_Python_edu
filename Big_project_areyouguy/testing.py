
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
GlobalDB2.update({"chat_id_243336464":''})


print(GlobalDB2)
#print(bool1)

class MyVisitor:

    def register_0(self):
        print("0 " + str(self.fiction))

    def register_1(self):
        print(1)

    def register_2(self):
        print(2)

    def dispatch(self, value):
        method_name = 'register_' + str(value)
        method = getattr(self, method_name)
        method()


Visit = MyVisitor()
Visit.fiction = '432'
Visit.dispatch('0')

s=0
d= '643747' in GlobalDB["64747"]["memberID"]
s=s+d
print(s)
