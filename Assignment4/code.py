def f(x):
    return -(x-1)**2+10

def df(x):
    return -2*(x-1)

eplison = 0.000000001

current_answer  = -5
error = 10
rate = 0.1
maximum_iters = 10000000
num_iters = 0
while (error > eplison) and (num_iters < maximum_iters):
    new_answer = current_answer+df(current_answer)*rate
    error = abs(current_answer-new_answer)
    current_answer = new_answer
    num_iters = num_iters+1
    

print("Maximum_value attanied at: ",current_answer)
print("Maximum value is: ",f(current_answer))


# Parabola sketch:

from matplotlib.pyplot import *
from numpy import *
x=linspace(-10,12,500000)
y=-(x-1)**2+10
plot(x,y)
xlabel("x axis")
ylabel("y axis")
annotate('A',(-5,-26),textcoords="offset points",xytext=(0,10),ha='center') 
annotate('B',(1,10),textcoords="offset points",xytext=(0,2),ha='right') 
plot(-5,-26,'ro')
plot(1,10,'g*')
show()
