import sys
import re

for line in sys.stdin:
    key, value = line.split('   ')
    values = value.split(';')[:-1]
    numbers = set([int(num) for num in re.findall(r'\d+', values[0])])
    common_friends = numbers
    for i in range(1, len(values)):
        numbers = set([int(num) for num in re.findall(r'\d+', values[i])])
        common_friends = common_friends.intersection(numbers)
    print(key, '   ', tuple(common_friends))
