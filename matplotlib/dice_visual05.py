
import pygal
from dice import Dice

# 统计同时抛两个面数不一样的骰子

dice_1 = Dice()
dice_2 = Dice(10)

# results = []
# for roll_num in range(50000):
#     result = dice_1.roll() + dice_2.roll()
#     results.append(result)

# 修改为列表解析语法
results = [dice_1.roll() + dice_2.roll() for roll_num in range(50000)]

# frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# 修改为列表解析语法
frequencies = [results.count(value) for value in range(2, max_result+1)]

# 描绘在直方图里
hist = pygal.Bar()
hist.title = 'Results of rolling a D6 and a D10 50,000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')


