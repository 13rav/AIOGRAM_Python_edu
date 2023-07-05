from func import check_user, GlobalDB, IDTOuser, updateDB_thePIDOR, statistic
test_dic={"Alice":6, "Bob":1, "Green":1, "Harry":3, "Liza":5}

sorted_dic = dict(sorted(test_dic.items(), key = lambda item: item[0]))

print(sorted_dic)
for i in range(0, 1, 2):
    sorted2_dic = test_dic.items()

check_user(111, 122343244235, "andrusha")
check_user(111, 943278234, "Roma")
check_user(111, 984382899234, "Daniil")
check_user(111, 8437818234787, "Ilya")
check_user(555, 81288914, "Sanya")
check_user(555, 834895882345, "Grisha")
check_user(555, 122343244235, "andrusha")

updateDB_thePIDOR(111, 943278234, 2)
updateDB_thePIDOR(111, 943278234, 3)
updateDB_thePIDOR(111, 8437818234787, 2)
updateDB_thePIDOR(111, 8437818234787, 1)
updateDB_thePIDOR(111, 8437818234787, 2)
updateDB_thePIDOR(111, 8437818234787, 4)
updateDB_thePIDOR(111, 984382899234, 1)

print(statistic(111))
print(GlobalDB)

for key in GlobalDB:
    print(key)
