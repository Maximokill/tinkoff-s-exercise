import csv

filename = "YNDX_160101_161231.csv"
date = []
time = []
high_price = []
low_price = []

with open(filename, 'r') as file:
    data = csv.reader(file)
    for row in data:
        date.append(row[0])
        time.append(row[1])
        high_price.append(row[3])
        low_price.append(row[4])

high_price = list(map(float, high_price[1:]))
low_price = list(map(float, low_price[1:]))

min_low = low_price.index(min(low_price)) + 1
max_high = high_price.index(max(high_price)) + 1

print(min_low)
print(max_high)
