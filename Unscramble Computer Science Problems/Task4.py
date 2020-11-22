"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

in_calls = set([i[0] for i in calls])
out_calls = [i[1] for i in calls]

in_texts = [i[0] for i in texts]
out_texts = [i[1] for i in texts]

l = set(out_calls+in_texts+out_texts)

print("These numbers could be telemarketers: ")
lis = [i for i in in_calls if i not in l]
lis.sort()
for k in lis:
    print(k)
    
