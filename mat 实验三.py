# import matplotlib.pyplot as plt
# input_value=[1,2,3,4,5,6]
# square=[1,4,9,16,25,36]
# plt.plot(input_value,square,linewidth=5)
# plt.xlabel('value')
# plt.ylabel('square of value')
# plt.title('square')
# plt.tick_params(axis='both',labelsize=14)
# plt.show()
# import matplotlib.pyplot as plt
# # plt.scatter(2,4)
# x=[1,2,3,4,5,6]
# y=[1,4,9,16,25,36]
# plt.scatter(x,y,s=10)  # s可以理解为点的半径
# plt.show()
# import matplotlib.pyplot as  plt
# x=list(range(1,1001))
# y=list(i**2 for i in x)
# plt.scatter(x,y,c=y,cmap=plt.cm.Blues,edgecolors='None',s=40)
# plt.axes([0,1100,0,110000001])
# plt.show()
# import matplotlib.pyplot as plt
# x=list(range(1,1001))
# y=list(i*i*i for i in x)
# plt.scatter(x,y,c=y,cmap=plt.cm.Blues,edgecolors='none',s=40)
# plt.axes([1,1100,1,1100000000])
# plt.xlabel('value')
# plt.ylabel('result')
# plt.show()
# from random import choice
# class RandomWalk():
#     def __init__(self,num_points=5000):
#         self.num_points=num_points
#         self.x_values=[0]
#         self.y_values=[0]
#     def fill_walk(self):
#         while len(self.x_values) <self.num_points:
#             x_direction=choice([-1,1])
#             x_distance=choice([0,1,2,3,4])
#             x_step=x_distance*x_direction
#
#             y_direction=choice([-1,1])
#             y_distance=choice([0,1,2,3,4])
#             y_step=y_distance*y_direction
#
#             if x_step==0 and y_step==0:
#                 continue
#             next_x=self.x_values[-1]+x_step
#             next_y=self.y_values[-1]+y_step
#
#             self.x_values.append(next_x)
#             self.y_values.append(next_y)
#连续图像
# import matplotlib.pyplot as plt
# rw=RandomWalk()
# rw.fill_walk()
# plt.plot(rw.x_values,rw.y_values)
# plt.show()
#离散图像
# import matplotlib.pyplot as plt
# rw=RandomWalk()
# rw.fill_walk()
# plt.plot(rw.x_values,rw.y_values)
# plt.show()

# import matplotlib.pyplot as plt
# while True:
#     rw=RandomWalk()
#     rw.fill_walk()
#     point=list(range(rw.num_points))
#     plt.scatter(rw.x_values,rw.y_values,c=point,cmap=plt.cm.Blues,edgecolors='none',s=10)
#     #突出起点和终点
#     plt.scatter(0,0,c='green',edgecolors='none',s=100)
#     plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
#     plt.show()
#     keep=input('是否继续')
#     if keep=='n':
#         break
from random import choice
class RandomWalk_plas():
    def __init__(self,num_point):
        self.num_point=num_point
        self.x_value=[0]
        self.y_value=[0]
    def get_step(self):
        self.direction=choice([-1,1])
        self.distance=choice([0,1,2,3,4])
        self.step=self.distance*self.direction
        return self.step
    def fill_walk(self):
        while len(self.x_value) <self.num_point:
            x_step=self.get_step()
            y_step=self.get_step()
            if x_step==0 and y_step==0:
                continue
            next_x=self.x_value[-1]+x_step
            next_y=self.y_value[-1]+y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)
import random
import matplotlib.pyplot as plt
while True:
    rw=RandomWalk_plas(5000)
    rw.fill_walk()
    piont=list(range(rw.num_point))
    plt.scatter(rw.x_value,rw.y_value,c=piont,cmap=plt.cm.Blues,edgecolors='none',s=10)
    plt.scatter(0,0,cmap='green',edgecolors='none',s=40)
    plt.scatter(rw.x_value[-1],rw.y_value[-1],cmap='red',edgecolors='none',s=40)
    plt.show()
    keep=input('是否继续')
    if keep=='n':
        break
