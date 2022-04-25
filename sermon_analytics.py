from collections import defaultdict
import csv

# Note:
# The intent of this code is to analyze ONE sermon only.
# Many variables were used to visualize the code better.
# Do not use this to process multiple sermons unless optimizing for memory/cpu.

with open('outputsample.txt', newline='') as csvfile:
    data = list(csv.reader(csvfile))
with open('ignore.txt', newline='') as csvfile:
    data2 = list(csv.reader(csvfile))

# Variables
sermon = str(data[0][0])
tokenized = sermon.split()
frequencies = defaultdict(int)
ignore = []

# set ignore
for word in data2:
    ignore.append(word[0])

# Number of Words
print(len(tokenized) , "words used.") 

# Unique Words Used
for word in tokenized:
    if (word not in ignore):
        frequencies[word] += 1
print(len(frequencies), " unique words used.")

# Frequncy Distribution
print("\n---- Frequency Distribution ---")
sorted_words=sorted(frequencies.items(),key=lambda item: int(item[1]))

top10words = ""
count = 10
for word in sorted_words[-10:]:
    top10words += word[0] + ", " if count > 0 else ""
    count -= 1
    
print("Top 10 words used: ", top10words)