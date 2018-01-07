#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Quick Python Script Explanation for Programmers
# mailto:emyx@msn.com
import os

def main():
    print ('Hello World!')
    
    print ("This is MengYuxin\'s Greeting")
    
    foo(5, 10)
    
    print ('=' * 10)
    print ('Current working directory is '+os.getcwd())
    
    counter = 0
    counter += 1
    
    food = ['Apples', 'Lemons', 'Bananas', 'Oranges']
    for i in food:
        print ('I like to eat'+i)
    
    print ("Count up to number ten:")
    for i in range(10):
        print (i+1)
        
def foo(param1, secondParam):
    res = param1+secondParam
    
    print ('%s + %s = %s' % (param1, secondParam, res))
    
    if res < 50:
        print ('foo')
        
    elif (res >=50) and ((param1 == 42) or (secondParam == 24)):
        print ('bar')
        
    else:
        print ('moo')
        
    return res # This is a on-line comment.

    '''A multi-
line string, but can also be a multi-line commnet.'''

if __name__ == '__main__':
    main()