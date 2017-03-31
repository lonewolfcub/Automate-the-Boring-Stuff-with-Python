#! usr/bin/env python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.
# This program also saves the alt text and title of each picture to a text file

import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "lxml")

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            titleText = comicElem[0].get('title')
            altText = comicElem[0].get('alt')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get('http:' + comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

            # Save title and alt text to file
            textFile = open(os.path.join('xkcd', os.path.basename(altText)), 'w', encoding='utf-8')
            textFile.write(titleText)
            textFile.close()

# Create and start the Thread objects.
downloadThreads = [] # a list of all the Thread objects
for i in range(0, 1400, 100): # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
