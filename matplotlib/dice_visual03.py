
import pygal
from dice import Dice

# 统计同时抛两个骰子的结果分布

dice_1 = Dice()
dice_2 = Dice()

results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# 计算1000次中1-6面出现的次数
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 描绘在直方图里
hist = pygal.Bar()
hist.title = 'Results of rolling two D6 1000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')


