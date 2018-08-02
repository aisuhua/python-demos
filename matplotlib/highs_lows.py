
import csv

with open('sitka_weather_07-2014.csv') as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)
    print(header_row)
