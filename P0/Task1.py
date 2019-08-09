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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# print("Length of texts {} and length of calls {}".format(len(texts), len(calls)))

# Create a set to store the list of all unique phone numbers
phoneNumbers = set([])

# Iterate through all the items in texts and calls list; adding unique
# phone numbers to phoneNumbers list, and checking against previous
# entries before adding new ones
for item in texts:
    phoneNumbers.add(item[0])
    phoneNumbers.add(item[1])

for item in calls:
    phoneNumbers.add(item[0])
    phoneNumbers.add(item[1])

# print the length of phoneNumbers to get all the unique numbers
print("There are {} different telephone numbers in the records.".format(len(phoneNumbers)))

# for items in phoneNumbers:
# print(phoneNumbers)