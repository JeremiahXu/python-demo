# python3
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate, signal,ndimage

x = np.array([
    0.5,
    0.6,
    0.8,
    2,
    2.5,
    3,
    3.5,
    4,
    4.5,
    5,
    5.5,
    6,
    8,
    10,
    12,
    24,
    48,
    72
])
y = np.array([
    0.2,
    4,
    8,
    17.6,
    21,
    22.8,
    24,
    22.6,
    20,
    16,
    7.6,
    5.8,
    3.2,
    2.5,
    2.1,
    1,
    0.4,
    0
])


# mr = [0 for x in range(len(x))]

# for index in range(len(x)):
#    t1 = 1/(x[index]*x[index])
#    mr[index] = t1
   
# print(mr)

# ww = np.array(mr)

# 插值数据
f = interpolate.interp1d(x, y, kind='cubic')
xnew = np.linspace(x.min(), x.max(), 1000)
ynew = f(xnew)

# 使用高斯滤波器对插值曲线进行平滑处理
# sigma = 5
# y_smooth = signal.gaussian_filter(ynew, sigma=sigma)

y_smooth = ynew
# 使用高斯滤波器平滑插值曲线
sigma = 5
# y_smooth = ndimage.gaussian_filter1d(ynew, sigma=sigma)

# plt.plot(x, y, 'o', xnew, ynew, '-')
# plt.show()

# plt.plot(x, y, 'o', xnew, ynew, '-', xnew, y_smooth, '--')
# plt.legend(['Data', 'Interpolation', 'Smoothing'])
plt.plot(x, y, 'o')
plt.plot(xnew, y_smooth, '-')
plt.show()


# coefficients = np.polyfit(x, y, deg=1,w=ww)
# coefficients = np.polyfit(x, y, deg=3)

# Slope3 = coefficients[0]
# Slope2 = coefficients[1]
# Slope1 = coefficients[2]
# Slope = coefficients[3]

# Slope = coefficients[0]
# Intercept = coefficients[1]
# line = Slope3 * (x**3) + Slope2 * (x**2) +  Slope1 * x + Slope
# print("line = %s * x + %s" % (Slope, Intercept))

# plt.plot(x, y, 'o', label='Data')
# 
plt.plot(x, y, 'purple', label='-')
# plt.plot(x, line, label='Fit')
plt.legend()
plt.show()



# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# X = np.arange(-5, 5, 0.15)
# Y = np.arange(-5, 5, 0.15)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)

# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')

# plt.show()

