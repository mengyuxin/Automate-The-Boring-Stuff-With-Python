# prettyCharCount.py
import pprint

msg = 'It was a bright cold day in April, ' + \
      'and the clocks were striking thirteen.'
count = {}
for char in msg:
    count.setdefault(char, 0)
    count[char] += 1

# Solution 1 for Pretty Print
print('Solution 1: ')
for k, v in count.items():
    print(str(k) + ': ' + str(v))

# Solution 2 for Pretty Print
print('Solution 2: ')
pprint.pprint(count)

# Solution 3 for Pretty Print
print('Solution 3: ')
print(pprint.pformat(count)) #pprint.pformat()

