import matplotlib.pyplot as plt

# 提供x和y坐标

# 提供x坐标值
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=5)

# 设置标题
plt.title('Squares Title', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Squares of Value', fontsize=14)

# 设置刻度
plt.tick_params(axis='both', labelsize=14)

plt.show()

