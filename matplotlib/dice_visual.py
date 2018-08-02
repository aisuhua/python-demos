from dice import Dice

# 模拟掷骰子100次

dice = Dice()

results = []
for roll_num in range(100):
    result = dice.roll()
    results.append(result)

print(results)
