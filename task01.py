#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

import json

filename = 'task01c.txt'
file = open(filename,'r')
data = file.read()

encodedNumbers = json.loads(data)
sorted_data = sorted(encodedNumbers, key=lambda x: x)
print(sorted_data[-1])