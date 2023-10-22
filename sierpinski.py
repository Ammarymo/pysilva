import matplotlib.pyplot as plt
import random

def trans1(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x
    y1 = 0.5 * y
    return x1, y1
def trans2(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 0.5
    y1 = 0.5 * y + 0.5
    return x1,y1
def trans3(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 1
    y1 = 0.5 * y 
    return x1,y1

transformation = [trans1,trans2,trans3]
a1 = [0]
b1 = [0]
a,b = 0,0
for i in range(100000):
    trans = random.choice(transformation)
    a,b = trans((a,b))
    a1.append(a)
    b1.append(b)

plt.plot(a1,b1,'o')
plt.show()