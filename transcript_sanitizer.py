import csv
import re

with open('data imported/transcriptsample.txt', newline='') as file:
    data = list(csv.reader(file))

f = open("outputsample.txt", "a")

# Stripping out timestamp
pattern = '([0-9][0-9]:[0-9][0-9])|([0-9]:[0-9][0-9])|([0-9][0-9][0-9]:[0-9][0-9])'
result = "";

for line in data:
    if not re.match(pattern, line[0]):
        f.write(result + line[0] + " ")

f.close()