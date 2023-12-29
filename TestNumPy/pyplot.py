# python3
import numpy as np
import matplotlib.pyplot as plt

x = np.array([
    2,
    4,
    8,
    16,
    32,
    64,
    128,
    250
])
y = np.array([
    0.024,
    0.049,
    0.097,
    0.187,
    0.378,
    0.756,
    1.499,
    2.88
])


mr = [0 for x in range(len(x))]

for index in range(len(x)):
#    t1 = 1/(x[index]*x[index])
   t1 = 1
   mr[index] = t1
   
print(mr)

ww = np.array(mr)


coefficients = np.polyfit(x, y, deg=1,w=ww)
# coefficients = np.polyfit(x, y, deg=1)

Slope = coefficients[0]
Intercept = coefficients[1]
line = Slope * x + Intercept
print("line = %s * x + %s" % (Slope, Intercept))


# 计算拟合直线与原始数据的相关性系数
r = np.corrcoef(x, y, rowvar=False)[0, 1]

# 计算r2决定系数
r2 = r ** 2

plt.plot(x, y, 'o', label='Data')
plt.plot(x, line,"-")
plt.legend()
plt.show()

