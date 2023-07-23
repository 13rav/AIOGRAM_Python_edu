from func import check_user, GlobalDB, IDTOuser, updateDB_thePIDOR, statistic
import random, datetime, asyncio, time
test_dic={"Alice":6, "Bob":1, "Green":1, "Harry":3, "Liza":5}

import datetime, time

GlobalDB = {-1001792492889: {'membersID': [1176746813, 420946976, 437718142, 462989522, 339420375, 473898130, 438456033, 687774772], 1176746813: 9, 'nowDay': None, 'id_thePIDOR': None, 420946976: 9, 437718142: 13, 687774772:12, 462989522: 8, 339420375: 7, 473898130: 5, 438456033: 7}}

IDTOuser = {1176746813: 'rav_pr', 420946976: 'occult_fox', 437718142: 'nikitas21', 462989522: 'Danil5621', 339420375: 'yell0wlamp', 473898130: 'nihaoh', 438456033: 'dimchis3', 687774772: 'vvvr1g'}

def statistic(chat_int):
    global GlobalDB, IDTOuser
    list_with_str = list()
    value_for_max = ()
    text_to_return=f"""Топ 10 пидоров:
"""
    copy_GlobalDB_stat = dict()

    if GlobalDB.get(chat_int) is None:
        return "Нет информации для отображения, пройдите регистрацию"

    for i in GlobalDB[chat_int]["membersID"]:
        copy_GlobalDB_stat.update({i:GlobalDB[chat_int][i]})
    
    sorted_DB = dict(sorted(copy_GlobalDB_stat.items(), key= lambda item: item[1], reverse=True))

    first_best_userID = list(sorted_DB)[0:10]

    for i in range(len(first_best_userID)):
        #list_with_str.append(f"""
        #<b>{IDTOuser[first_best_userID[i]]}</b>    --    {sorted_DB[first_best_userID[i]]}""")
        list_with_str.append(f"""
        <b>{IDTOuser[first_best_userID[i]]}</b>""")
        print(list_with_str[i])
        value_for_max = value_for_max + (len(list_with_str[i]),)

    print(max(
        value_for_max
    ))

    for i in range(len(list_with_str)):
        for k in range(max(value_for_max)-len(list_with_str[i])):
            list_with_str[i] = list_with_str[i]+" "
        print(list_with_str[i])

    for i in range(len(list_with_str)):
        text_to_return=text_to_return + str(list_with_str[i])+ f"  --    {sorted_DB[first_best_userID[i]]}"

    print(str(text_to_return))
    return str(text_to_return)

statistic(-1001792492889)
 