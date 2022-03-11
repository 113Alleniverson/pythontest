from matplotlib import pyplot as plt
from random import *

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['font.size'] = 80# 修改默认字体字号
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


figure=plt.figure(figsize=(80,20),dpi=20)
y1=[randint(0,7) for i in range(20)]
y2=[randint(0,7) for i in range(20)]
x=range(11,31)
_x=['{}岁'.format(i) for i in range(11,31)]
plt.xticks(list(x),_x,rotation=45)
# plt.yticks(range(min(y),max(y)+1)) #调整纵坐标的范围是最小值到最大值
_y=[i/2 for i in range(0,13)]
plt.yticks(_y)
plt.xlabel('年龄')
plt.ylabel('个数')
plt.title('11到30岁')
plt.grid(alpha=0.4)       #绘制网格 alpha参数指的是透明度
plt.plot(x,y1,label='一号',color='red',linestyle=':')
plt.plot(x,y2,label='二号',color='cyan',linestyle='-.') #将y1 y2 绘制到一张图片上，并分别表标注（label参数）
plt.legend(loc='upper right')
plt.show()