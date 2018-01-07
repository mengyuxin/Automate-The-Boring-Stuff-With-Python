def collatz(num):
    while num > 1:
        print(num)
        if num % 2 == 0:
            num = int(num // 2)
        else:
            num = int(3 * num + 1)
    else:
        print(num)
        #print('Finished.')

def main():
    myInput = input('Please enter an integer: ')
    try:
        num = int(myInput)
        collatz(num)
    except:
        print('ValueError: invalid input. You entered ' + myInput + '.')      
    
main()
