"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Create a dictionary to store list of phone numbers and
# cumulative call duration in seconds -- both calling & receiving
callLog = {}

maxDuration = 0

# Iterate through 'calls' to keep adding phone numbers and 
# keep adding call durations for each transaction (whether 
# they made the call, or if they were the receiver)
for call in calls:
    callLog[call[0]] = callLog.get(call[0], 0) + int(call[3])   # Add number + duration which made the call
    callLog[call[1]] = callLog.get(call[1], 0) + int(call[3])   # Add number + duration which received the call
    if maxDuration < callLog.get(call[0]):                      # In the same loop, also find max duration spent
        maxDuration = callLog.get(call[0])                      #   on the call, so don't have to run a loop on 
    if maxDuration < callLog.get(call[1]):                      #   the dictionary again.
        maxDuration = callLog.get(call[1])

# Find the max duration for which a number was in a call
# maxDuration = max(callLog.items(),key = lambda x : x[1])

# Create a list to store all the numbers which made a call 
# for the same duration as maxDuration
maxDurationPhoneNumbers = list()

# Iterate through the callLog dictionary to find other 
# keys (i.e. phone numbers) whose value (i.e. duration 
# in seconds) matches maxDuration
for number, duration in callLog.items():
    if duration == maxDuration:
        maxDurationPhoneNumbers.append(number)

# If there's only 1 number with the max duration, print that, 
# else loop through the list to print it for all the numbers
if len(maxDurationPhoneNumbers) == 1:
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(maxDurationPhoneNumbers[0], maxDuration))
else:
    for phoneNumbers in maxDurationPhoneNumbers:
        print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phoneNumbers, maxDuration))

###################
## Previous Code ##
###################

# print('Keys with maximum Value in Dictionary : ', listOfCalls)

# print(callLog)
# maxDuration = 0
# longestDurationCall = []

# for callLog in calls:
#     if int(callLog[3]) == maxDuration:
#         # maxDuration = callLog[3]
#         # print("EQUAL!!! Phone numbers are {} and {}, and the duration is {}".format(callLog[0], callLog[1], maxDuration))
#         longestDurationCall.append(callLog[0])
#         longestDurationCall.append(callLog[1])
#         # print("Longest Duration List: {}".format(longestDurationCall))
#     if int(callLog[3]) > maxDuration:
#         maxDuration = int(callLog[3])
#         # print("Phone numbers are {} and {}, and the duration is {}".format(callLog[0], callLog[1], maxDuration))
#         # print("Longest Duration List before clear: {}".format(longestDurationCall))
#         longestDurationCall.clear()
#         longestDurationCall.append(callLog[0])
#         longestDurationCall.append(callLog[1])
#         # print("Longest Duration List after clear: {}".format(longestDurationCall))

# print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longestDurationCall[0], maxDuration))
# print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longestDurationCall[1], maxDuration))
# print(longestDurationCall)
    

# print(calls[0])
# print(calls[0][2][6:10])

# dateOfCall = []

# for item in calls:
#     if item[2][3:10] not in dateOfCall:
#         dateOfCall.append(item[2][3:10])

# print(dateOfCall)