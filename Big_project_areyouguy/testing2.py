from testing import GlobalDB, IDTOuser, update_DB, choose, add_DB
import random

update_DB()
choose()


temp_int = random.choice(GlobalDB['chat1']['membersID'])
GlobalDB['chat1'][temp_int] = GlobalDB['chat1'][temp_int]+1
print("пидор дня @"+IDTOuser[temp_int])
print(GlobalDB['chat1'][temp_int])

def add_db2():
    GlobalDB['chat1'][temp_int] = GlobalDB['chat1'][temp_int]+1
add_DB(7832878823)

print(GlobalDB)
