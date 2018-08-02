
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# 一整年的最高和最低温度变化情况
# 两线之间的中间区域填充颜色

with open('sitka_weather_2014.csv') as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title('Daily high and low temperatures - 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
