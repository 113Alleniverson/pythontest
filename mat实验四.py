# import pygal
# from random import randint
# class die():
#     def __init__(self,num_sides=6):
#         self.num_sides=num_sides
#     def roll(self):
#         return randint(1,self.num_sides)
# die1=die()
# results=[]
# for i in range(1,101):
#     result=die1.roll()
#     results.append(result)
# print(results)
#
# frequences=[]
# for i in range(1,die1.num_sides+1):
#     frequency=results.count(i)
#     frequences.append(frequency)
# print(frequences)
# hist=pygal.Bar()
# hist._title='Result of rolling one D6 100 times'
# hist.x_labels=['1','2','3','4','5','6']
# hist._x_title='Result'
# hist._y_title='frequences'
# hist.add('D6',frequences)
# hist.render_to_file('D6_result')

#同时投掷两个骰子
# import pygal
# import random
# class die_2():
#     def __init__(self,num_sides=6):
#         self.num_sides=num_sides
#     def roll(self):
#         return random.randint(1,self.num_sides)
# die1=die_2()
# die2=die_2()
# die1_result=[]
# die2_result=[]
# die_result=[]
# for i in range(1,101):
#     a=die1.roll()
#     b=die1.roll()
#     c=a+b
#     # die1_result.append(a)
#     # die2_result.append(b)
#     die_result.append(c)
# frequences=[]
# for i in range(1,13):
#     frequency=die_result.count(i)
#     frequences.append(frequency)
# hist=pygal.Bar()
# hist._title='Result of rolling one D6 100 times'
# hist.x_labels=['1','2','3','4','5','6','7','8','9','10','11','12']
# hist._x_title='Result'
# hist._y_title='frequences'
# hist.add('D12',frequences)
# hist.render_to_file('dice_visual.svg')
#简化过程
import pygal
import random
class die():
    def __init__(self,num_sides=6,num_dies=1):
        self.num_sides=num_sides
        self.num_dies=num_dies
    def roll(self):
        return random.randint(1,self.num_sides)
    def x_labels(self):
        x_max=self.num_dies*self.num_sides
        x_label=[i for i in range(1,x_max+1)]
        return x_label
die1=die(6,2)
die2=die(6,2)
die_result=[]
for i in range(1,1001):
    die_result.append(die1.roll()+die2.roll())
frequences=[]
for i in range(1,die1.num_sides+die2.num_sides+1):
    frequences.append(die_result.count(i))
hist=pygal.Bar()
hist._title='Result of rolling one D6 100 times'
hist.x_labels=die1.x_labels()
hist._x_title='Result'
hist._y_title='frequences'
hist.add('D12',frequences)
hist.render_to_file('dice_visual.svg')