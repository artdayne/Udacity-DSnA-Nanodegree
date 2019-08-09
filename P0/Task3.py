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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# To count total calls made from Bangalore for Part B
# starting with '1' instead of '0' to account for 
# correct percentage calculation. 
callsFromBangalore = 0

# To count total calls made to Bangalore, from Bangalore, for Part B
callsToBangalore = 0

# Empty set to be filled up with all the unique prefixes dialed
# from Bangalore
prefixes = set()

# To be used for string splicing
end = 0

for callLog in calls:
  # For each call log in 'calls' list, check if call 
  # originated from fixed line in Bangalore
  if callLog[0].startswith('(080)'):
    callsFromBangalore += 1                 # increment counter by 1 for calls made from Bangalore 
    if callLog[1].startswith('140'):  
      continue                              # if call made to tele-marketing, ignore
    elif callLog[1].startswith('('):        # if call made to landline, recipient number to start with "("
      if callLog[1].startswith('(080)'):    # if call made to Bangalore, increment counter
        callsToBangalore += 1
      end = callLog[1].find(')') + 1        # find length of "(xxx)" to splice and add to prefixes
      prefixes.add(callLog[1][0:end])
    else:
      prefixes.add(callLog[1][0:4])


print("The numbers called by people in Bangalore have codes:")
# prefixes.sort()
print(*sorted(prefixes), sep = "\n")

print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(callsToBangalore*100/callsFromBangalore))
