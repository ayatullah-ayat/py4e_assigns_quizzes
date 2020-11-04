#In this assignment you will read through and 
# parse a file with text and numbers. You will extract 
# all the numbers in the file and compute the sum of the numbers.

import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_965876.txt"
handle = open(name)

txt = handle.read()
numbers = re.findall('[0-9]+', txt)

# make_int = list(map(int, numbers))        //using map to make int
make_int = [int(item) for item in numbers]  # list comprehension logic
print('sum: ', sum(make_int))