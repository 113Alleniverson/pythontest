# import csv
# filename='sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader=csv.reader(f)
#     header_row=next(reader)
#     # a=next(reader)
#     # print(header_row)
#     # print(a)
#     # for index,column_header in enumerate(header_row):
#     #     print(index,column_header)
#     highs=[]
#     for row in reader:
#         high=int(row[1])
#         highs.append(high)
#     print(highs)
# import csv
# from matplotlib import pyplot as plt
# filename='sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader=csv.reader(f)
#     header_row=next(reader)
#     highs=[]
#     for row in reader:
#         high=int(row[1])
#         highs.append(high)
# plt.plot(highs,c='red')
# plt.title('Daily high temperatures, July 2014',fontsize=24)
# plt.xlabel('',fontsize=24)
# plt.ylabel('Temperature (F',fontsize=16)
# plt.tick_params(axis='both',which='major',labelsize=16)
# plt.show()
# datetime模块中读取时间，加入到横坐标当中
# import csv
# from matplotlib import pyplot as plt
# from datetime import datetime
# filename='sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader=csv.reader(f)
#     header_row=next(reader)
#     dates,highs=[],[]
#     for row in reader:
#         current_time=datetime.strptime(row[0],'%Y-%m-%d')
#         dates.append(current_time)
#
#         high=int(row[1])
#         highs.append(high)
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates,highs,c='red')
# plt.title('sitka_weather_07-2014',fontsize=24)
# plt.xlabel('',fontsize=16)
# fig.autofmt_xdate()#绘制倾斜的日期标签，但是好像只对X轴起作用
# plt.ylabel('Temperature (F)',fontsize=16)
# fig.autofmt_xdate()
# plt.tick_params(axis='both',which='major',labelsize=16)
# plt.show()
# import csv
# import datetime
# from matplotlib import pyplot as plt
# filename='sitka_weather_2014.csv'
# with open(filename) as f:
#     reader=csv.reader(f)
#     header_row=next(reader)
#     dates,highs,lows=[],[],[]
#     for row in reader:
#         current_time=datetime.datetime.strptime(row[0],'%Y-%m-%d')
#         high=int(row[1])
#         low=int(row[3])
#         highs.append(high)
#         lows.append(low)
#         dates.append(current_time)
# fig=plt.figure(dpi=128,figsize=(10,6))
# plt.plot(dates,highs,c='red',alpha=0.5)
# plt.plot(dates,lows,c='blue',alpha=0.5)
# plt.fill_between(dates,lows,highs,facecolor='blue',alpha=0.1)
# plt.xlabel('',fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel('Temperature (F)',fontsize=16)
# plt.show()

#错误处理
# import csv
# import datetime
# from matplotlib import  pyplot as plt
# filename='death_valley_2014.csv'
# with open(filename) as f:
#     reader=csv.reader(f)
#     header_row=next(reader)
#     dates,highs,lows=[],[],[]
#     for row in reader:
#         try:
#             current_time=datetime.datetime.strptime(row[0],'%Y-%m-%d')
#
#             high=int(row[1])
#
#             low=int(row[3])
#         except ValueError:
#             print(current_time,'missing date')
#         else:
#             dates.append(current_time)
#             highs.append(high)
#             lows.append(low)
# fig=plt.figure(dpi=128,figsize=(10,6))
# plt.plot(dates,highs,c='red',alpha=0.5)
# plt.plot(dates,lows,c='blue',alpha=0.5)
# plt.fill_between(dates,lows,highs,facecolor='blue',alpha=0.1)
# plt.xlabel('',fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel('Temperature (F)',fontsize=16)
# plt.show()
import csv
import datetime
from matplotlib import pyplot as plt
class Read():
    def __init__(self,filename):
        self.filename=filename
    def read(self,filename,words):
        filename=self.filename
        with open(filename) as f:
            reader = csv.reader(f)
            header_row=next(f)
            dates,highs,lows=[],[],[]
            for row in reader:
                try:
                    current_date=datetime.datetime.strptime(row[0],'%Y-%m-%d')
                    high=int(row[1])
                    low=int(row[3])
                except ValueError:
                    print(current_date,"missing date")
                else:
                    dates.append(current_date)
                    highs.append(high)
                    lows.append(low)
            if words=='dates':
                return dates
            elif words=='highs':
                return highs
            elif words=='lows':
                return lows
            else :
                print('error')
sitka=Read('sitka_weather_2014.csv')
death_visual=Read('death_valley_2014.csv')
sitka_highs=sitka.read('sitka_weather_2014.csv','highs')
sitka_lows=sitka.read('sitka_weather_2014.csv','lows')
sitka_dates=sitka.read('sitka_weather_2014.csv','dates')
death_visual_highs=sitka.read('death_valley_2014.csv','highs')
death_visual_lows=sitka.read('death_valley_2014.csv','lows')
death_visual_dates=sitka.read('death_valley_2014.csv','dates')
fig=plt.figure(dpi=128,figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(sitka_dates,sitka_highs,c='red',alpha=0.5)
plt.plot(sitka_dates,sitka_lows,c='blue',alpha=0.5)
plt.fill_between(sitka_dates,sitka_lows,sitka_highs,facecolor='blue',alpha=0.1)
plt.subplot(2,1,2)
plt.plot(sitka_dates,death_visual_highs,c='green',alpha=0.5)
plt.plot(sitka_dates,death_visual_lows,c='yellow',alpha=0.5)
plt.fill_between(sitka_dates,death_visual_lows,death_visual_highs,facecolor='green',alpha=0.1)

plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.show()