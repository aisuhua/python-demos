import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:

    # 增加坐标点数量
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 修改图表的宽度和高度
    plt.figure(figsize=(10, 6))

    # 去除边框颜色和使用渐变色来描绘漫步的路径
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 重点突出起点和终点，再次绘制终点和起点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏x和y坐标
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
