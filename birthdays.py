# birthdays.py

birthdays = {'Alice': 'Apr 1',
             'Bob': 'Dec 12',
             'Carol': 'Mar 4',
             'Dream': 'Jun 3',
             'Vincent': 'Aug 3',
             'Tony': 'Mar 11'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    elif name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
        
