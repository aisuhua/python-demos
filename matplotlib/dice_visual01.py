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

print(frequencies)
