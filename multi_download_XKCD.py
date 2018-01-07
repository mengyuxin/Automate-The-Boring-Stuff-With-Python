#! python3
# multi_download_Xkcd.py - Downloads XKCD comics using mutiple threads.

import requests
import os
import bs4
import threading

url = 'http://xkcd.com' # starting url
os.makedirs('XKCD', exist_ok=True) # store comics in ./XKCD

def download_XKCD(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Download the page.
        print('Downloading page %s/%s ...' % (url, url_number))
        res = requests.get('%s/%s' % (url, url_number))
        res.raise_for_status()
        
        soup = bs4.BeautifulSoup(res.text, "lxml")

        # Find the URL of the comic image.
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('Could not find comic image.')
        else:
            comic_URL = comic_elem[0].get('src')
            # Download the image.
            print('Downloading image http:%s ...' % (comic_URL))
            res = requests.get('http:' + comic_URL)
            res.raise_for_status()    

            # Save the image to ./XKCD.
            image_file = open(os.path.join('XKCD', os.path.basename(comic_URL)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()
    
# Create and start the Thread object.
download_threads = []   # a list of all the thread object
for i in range(0, 1400, 100):
    download_thread = threading.Thread(target=download_XKCD, args=(i, i + 99))
    download_threads.append(download_thread)
    download_thread.start()

# Wait for all threads to end.
for download_thread in download_threads:
    download_thread.join()
print('Done.')
