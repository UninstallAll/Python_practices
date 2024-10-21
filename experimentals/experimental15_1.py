import csv

with open('weather.txt','r') as file:
    data = list(csv.reader(file))

city = input('enter a name of city: ')

for row in data[1:]:
    if row[0] == city:
        print(row[1])