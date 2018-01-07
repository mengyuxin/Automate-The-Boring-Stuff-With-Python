# processString.py

# 双引号
spam = "That is Andy's school bag."
print(spam)

# 6.1.3 转义字符
spam = "Hello there!\nHow are you?\nI\'m doing fine."
print(spam)

print('\'') #单引号
print('\"') #双引号
print('\t') #制表符
print('\n') #换行符
print('\\') #反斜杠


# 6.1.4 原始字符串
spam = r'That is Andy\'s iPad.'
print(spam)

print('\n')
# 用三重引号的多行字符串
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Andy''')

# 多行注释
""" This is a test Python program.
 Studied by Meng Yuxin emyx@msn.com

 This program was designed for Python 3 not Python 2.
"""

def test():
    """This is a multiline comment to help
    explain what the test() function does."""
    print('\nHello')

test()

