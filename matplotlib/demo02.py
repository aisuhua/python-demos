import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

plt.plot(squares, linewidth=5)

# 设置标题
plt.title('Squares Title', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Squares of Value', fontsize=14)

# 设置刻度
plt.tick_params(axis='both', labelsize=14)

plt.show()

