# Definition of the generator to produce even numbers.
def all_even():
    n = 0
    while True:
        yield n
        n += 2

my_gen = all_even()

# Generate the first 5 even numbers.
# for i in range(5):
#     print(next(my_gen))

# Now go and do some other processing.
do_something = 4
do_something += 3

# print("do+something : {}".format(do_something))

# Now go back to generating more even numbers.
# for i in range(100):
#     print(next(my_gen))

for i in range(1,10,2):
    print("{}. Hello!".format(i))

# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

print(capitalized_cities)

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here


print(html_str)