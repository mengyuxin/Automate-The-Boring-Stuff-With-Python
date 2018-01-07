#! python3
# exampleHTML.py
import bs4

exampleFile = open('.\\sample\example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'lxml')

elems = exampleSoup.select('#author')
print('type(elems): ' + str(type(elems)))
print('len(elems): ' + str(len(elems)))
print('type(elems[0]): ' + str(type(elems[0])))

print('Author = ' + elems[0].getText())
print('elems[0]: ' + str(elems[0]))
print('elems[0].attrs: ' + str(elems[0].attrs))