# This is a guess the number game.
# Written by Vicent.Meng on December 30th in 2017.

import random

secretNumber = random.randint(1, 20)
print(u'我想了一个0到20的数字。')

# Ask the player to guess 6 times.
for guessTaken in range(1, 7):
    print(u'请你猜一猜吧。')
    guess = int(input())

    if guess < secretNumber:
        print(u'你输入的数字太小了。')
    elif guess > secretNumber:
        print(u'你输入的数字太大了。')
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print(u'你猜对了。正确答案就是： ' + str(guessTaken) + '。')
else:
    print(u'没有机会了。其实正确答案是 ' + str(secretNumber) + '。')
    
