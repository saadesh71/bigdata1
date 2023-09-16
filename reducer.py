
import re
import sys


for line in sys.stdin:
    key, values = line.split('   ', 1)
    values = values.split(')')
    common_friends = set([int(num)
                          for num in re.findall(r'\d+', values[0])])
    for i in range(1, len(values)):
        numbers = set([int(num) for num in re.findall(r'\d+', values[i])])
        if (len(numbers) != 0):
            common_friends = common_friends.intersection(numbers)
    print('%s\t%s' % key, common_friends)
