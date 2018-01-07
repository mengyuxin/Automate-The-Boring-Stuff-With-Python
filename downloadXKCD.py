#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests
import os
import bs4

url = 'http://xkcd.com' # starting url
os.makedirs('XKCD', exist_ok=True) # store comics in ./XKCD
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s ...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
        # Download the image.
        print('Downloading image http:%s ...' % (comicUrl))
        res = requests.get('http:' + comicUrl)
        res.raise_for_status()    

        # Save the image to ./XKCD.
        imageFile = open(os.path.join('XKCD', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
