import matplotlib.pyplot as plt

# 隐藏黑色的点边框

# 利用程序自动计算坐标值
x_values = list(range(1, 1001))
y_values = [x*x for x in x_values]

plt.scatter(x_values, y_values, s=40, edgecolors='none')
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.show()

