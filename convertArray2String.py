# convertListToString.py
def convertListToString(para):
    ret = ''
    for i in range(len(para)):
        if i < len(para) - 1:
            ret += para[i] + ', '
        else:
            ret += 'and ' + para[i]
    return ret

spam = ['apples', 'bananas', 'tofu', 'cats']
print(convertListToString(spam))
