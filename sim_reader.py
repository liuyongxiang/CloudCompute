import pymongo
import time
import datetime


def init_datelist():
    ti = "2017-01-03"
    t = datetime.datetime(int(ti.split('-')[0]), int(ti.split('-')[1]), int(ti.split('-')[2]))
    datelist = []
    while not str(t).split()[0] == "2017-08-31":
        datelist.append(str(t).split()[0])
        t = t + datetime.timedelta(1)

    print("date list :")
    print(datelist)
    return datelist


myclient = pymongo.MongoClient("mongodb://188.131.181.36:27017/")
mydb = myclient["stock"]
mycol = mydb["transaction"]

datelist = init_datelist()

for date in datelist:
    list = []

    myquery = {'Trddt': date}
    for x in mycol.find(myquery, {"_id": 0}):
        list.append(x)

    with open("/root/sim_dataset/" + date, 'w', encoding="utf-8") as new:
        for element in list:
            if len(list) == 0:
                break
            print(str(element))
            # print(str(element) + "\n")
            if list.index(element) == len(list)-1:
                new.write(str(element))
            else:
                new.write(str(element) + '\n')


    print("read " + date)
    time.sleep(3)

# with open("C:\\usr\\Code\\python_code\\sim_sparkstreaming\\test-data\\2017-01-03", "r", encoding='UTF-8') as new:
#     data = new.readlines()
#
# for line in data:
#     print(line)





