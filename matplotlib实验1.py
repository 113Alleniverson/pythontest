# from matplotlib import pyplot as plt
# figure=plt.figure(figsize=(20,8),dpi=80) #设置图片的长宽，像素值
# x=range(2,26,2)
# y=[15,14,12,24,18,19,18,17,16,13,10,14]
# plt.plot(x,y)
# plt.xticks(x[::2])    #设置横纵坐标的刻度如果坐标太密集，就需要对x取步长
# plt.yticks(range(min(y),max(y)+1))
# plt.show()
from matplotlib import pyplot as plt
from random import *
#设置中文字体
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

figure=plt.figure(figsize=(20,8),dpi=80)
y=[randint(20,35) for i in range(120)]
x=range(0,120)
plt.plot(x,y)

# plt.yticks(y)           垃圾的调整坐标
# plt.xticks(x[::10])

_x=['10点{}分'.format(i) for i in range(60)]
_x+=['11:{}'.format(i) for i in range(60)]
plt.xticks(list(x)[::3],_x[::3],rotation=45)      #取步长，数字和字符串一一对应，数据的长度一样,rotation可以让坐标旋转方向
plt.xlabel('时间')
plt.ylabel('温度')
plt.title('十点到十二点的温度显示')
plt.show()
