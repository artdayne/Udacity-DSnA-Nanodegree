# print('Hello World!')


name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 
  
# using zip() to map values 
mapped = zip(name, roll_no, marks) 
  
# converting values to print as list 
mapped = dict(mapped) 
  
# printing resultant values  
print ("The zipped result is : ",end="")  # this is Python 3 only
print (mapped) 
  
print("\n") 