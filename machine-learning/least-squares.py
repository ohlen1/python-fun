import numpy as np
import matplotlib.pyplot as plt

#x = np.array([2,3,7,14,22,26,28], dtype=np.float64)
#y = np.array([4,5,11,20,38,47,59], dtype=np.float64)

rng = np.random.RandomState(1)
x = 10 * rng.rand(150)
y = 2 * x - 5 + rng.randn(150)

def calc_slope(x,y):
    index = 0
    a = 0
    sumX = 0
    sumY = 0
    x2 = 0
    for i in x:
        sumX += i
        sumY += y[index]
        a += (i*y[index])
        index += 1
        x2 += i**2

    #print("a is ", a)

    a = x.size * a
    a = a - (sumX*sumY)
    #print("a is ", a)

    #print("x2 is ", x2)
    b = x.size * x2 - (sumX**2)

    return a/b

def calc_intercept(x,y,m):
    index = 0
    sumY = 0;
    sumX = 0;
    for i in x:
        sumX += i
        sumY += y[index]
        index += 1

    return (sumY - (m*sumX)) / x.size

def calc_y2_array(x,y,m,b):
    y2 = np.zeros(x.size,dtype=np.float64)
    index = 0
    for i in x:
        y2[index] = (m*i)+b
        index += 1

    return y2

def calc_error_array(y,y2):
    error = np.zeros(y.size,dtype=np.float64)
    index = 0
    for i in y:
        error[index] = y2[index]-y[index]
        index += 1
    return error;

m = calc_slope(x,y)
print("m/slope is ["+str(m))+"]"

b = calc_intercept(x,y,m)
print("b/intercept is ["+str(b)+"]")

y2 = calc_y2_array(x,y,m,b)
#for i in y2:
#    print("y2 is ", i)

error = calc_error_array(y,y2)

plt.plot(x, y, ".")
plt.plot(x, y2)
plt.show()
