
import pygal
from dice import Dice

dice = Dice()

results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

# 计算1000次中1-6面出现的次数
frequencies = []
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 描绘在直方图里
hist = pygal.Bar()
hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('dice_visual.svg')


