test_dic={"Alice":6, "Bob":1, "Green":1, "Harry":3, "Liza":5}

sorted_dic = dict(sorted(test_dic.items(), key = lambda item: item[0]))

print(sorted_dic)
for i in range(0, 1, 2):
    sorted2_dic = test_dic.items()

print(sorted2_dic)
