#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
# http://www.nostarch.com/contactus.htm
# http://docs.python.org/3/library/re.html
# http://www.regular-expression.info/

import pyperclip # Clipboard 剪贴板
import re        # Regular Expression 正则表达式

# Create phone regex.
# 为电话号码创建一个正则表达式
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                    # area code
    (\s|-|\.)?                          # separator
    (\d{3})                             # first 3 digits
    (\s|-|\.)                           # separator
    (\d{4})                             # last 3 digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?     # extension
    )''', re.VERBOSE)

# Create email regex.
# 为E-mail地址创建一个正则表达式
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot something
    )''', re.VERBOSE)       # for complex regular expression

# Find matches in clipboard text.
# 在剪贴板文本中找到所有匹配
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])
    
# copy Results to the clipboard.
# 复制结果到剪贴板
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
    
