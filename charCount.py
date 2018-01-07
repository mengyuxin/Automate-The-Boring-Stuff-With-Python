# charCount.py
msg = 'It was a bright cold day in April, ' + \
      'and the clocks were striking thirteen.'
count = {}
for char in msg:
    count.setdefault(char, 0)
    count[char] += 1

print(count)
print('\nThe answer is :')

for k, v in count.items():
    print(str(k) + ': ' + str(v))
