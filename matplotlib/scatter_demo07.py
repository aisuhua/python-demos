import matplotlib.pyplot as plt

# 将输出保存为图片文件

# 利用程序自动计算坐标值
x_values = list(range(1, 1001))
y_values = [x*x for x in x_values]

# 红色
# plt.scatter(x_values, y_values, s=40, edgecolors='none', c='red')
# RGB颜色
# plt.scatter(x_values, y_values, s=40, edgecolors='none', c=(0, 0, 0.8))
# 渐变色
plt.scatter(x_values, y_values, s=40, edgecolors='none', c=y_values, cmap=plt.cm.Blues)

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])

# 保存为图片
plt.savefig('squares_plot.png', bbox_inches='tight')

