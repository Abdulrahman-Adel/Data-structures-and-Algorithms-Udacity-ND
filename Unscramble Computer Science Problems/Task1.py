"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import time
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
tic = time.time()
numbers = []
for i in texts:
   numbers.append(i[0])
   numbers.append(i[1])
   
for i in calls:
    numbers.append(i[0])
    numbers.append(i[1])
toc = time.time()    
print("There are {} different telephone numbers in the records.".format(len(set(numbers))))

print("It took {} Seconds".format(toc-tic))

