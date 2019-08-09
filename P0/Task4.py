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


teleMarketers = set()

for item in calls:
    teleMarketers.add(item[0])

for item in calls:
    teleMarketers.discard(item[1])

for item in texts:
    teleMarketers.discard(item[0])
    teleMarketers.discard(item[1])

# Print all the phone numbers sorted
print("These numbers could be telemarketers: ")
print(*sorted(teleMarketers), sep = "\n")

############################
## CODE BASED ON REVIEW 1 ##
############################

# def getUniquePhoneNumbers(phoneNumberList, colNum):
#     """ 
#     This method takes in a list and the index of a column for that list,
#     and will return a set() of all the numbers in that column, essentially
#     de-duping the list.
#     """
#     # Create an empty set to store all the unique phone numbers to be returned
#     uniquePhoneNumbers = set()

#     # Iterate through the list to get all the phone numbers
#     for numbers in phoneNumberList:
#         uniquePhoneNumbers.add(numbers[colNum])
    
#     return uniquePhoneNumbers

# # Get all the phone numbers in a variable, which will be calculated using set 
# # subtraction. Set A - Set B = all elements in Set A, which are not in B. So we 
# # take all phone numbers which made a call, and remove from that all phone 
# # numbers which also received a call, sent a text or received a text. Thus left 
# # only with numbers who made a call.
# marketingPhoneNumbers = (
#                             getUniquePhoneNumbers(calls, 0) 
#                             - getUniquePhoneNumbers(calls, 1) 
#                             - getUniquePhoneNumbers(texts, 0) 
#                             - getUniquePhoneNumbers(texts, 1)
#                         )

# # Print all the phone numbers
# print("These numbers could be telemarketers: ")
# for numbers in marketingPhoneNumbers:
#     print(numbers)


### SECOND APPROACH (USING LOGIC FROM PREVIOUS SUBMI)
####################################
## PREVIOUS CODE WITH ERROR FIXED ##
####################################

# uniqueCallers = []
# uniqueReceivers = []
# uniqueSenders = []
# uniqueTxtRcv = []

# for callLog in calls:
#     if callLog[0] not in uniqueCallers:
#         uniqueCallers.append(callLog[0])
#     if callLog[1] not in uniqueReceivers:
#         uniqueReceivers.append(callLog[1])

# for smsLog in texts:
#     if smsLog[0] not in uniqueSenders:
#         uniqueSenders.append(smsLog[0])
#     if smsLog[1] not in uniqueTxtRcv:
#         uniqueTxtRcv.append(smsLog[1])

# # counter = 0

# # print("Unique Callers: " + str(len(uniqueCallers)) + " Unique Call Receivers: " + str(len(uniqueReceivers)))
# # print("Unique SMS Senders: " + str(len(uniqueSenders)) + " Unique SMS Receivers: " + str(len(uniqueTxtRcv)))

# teleMarketers = []

# for callers in uniqueCallers:
#     if (callers not in uniqueReceivers) and (callers not in uniqueSenders) and (callers not in uniqueTxtRcv):
#         teleMarketers.append(callers)
#         # counter+=1

# # uniqueCallers.sort()

# # teleMarketers.sort()
# # marketingPhoneNumbers.sort()

# print("These numbers could be telemarketers: ")
# print(*teleMarketers, sep = "\n")

# # print(counter)
# # print(teleMarketers == marketingPhoneNumbers)