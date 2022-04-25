import csv

with open('data\data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

query = "disci"

for sunday in data:
    if query.lower() in sunday[1].lower():
        print(sunday)