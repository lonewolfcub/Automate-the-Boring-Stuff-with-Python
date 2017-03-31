#! usr/bin/env python3

# imgursearch.py - searches imgur with a given search term and downloads
# resulting images

import requests, os, bs4

os.makedirs('imgurSearch', exist_ok=True)

# Search Imgur
def imgurSearch(searchterm):
    search = requests.get('http://imgur.com/search/score?q=' + searchterm)
    search.raise_for_status()
# Save images
    soup = bs4.BeautifulSoup(search.text)
#    print(search.text)
    imgTags = soup.findAll('img')
    for imgTag in imgTags:
        imgURL = imgTag['src']
        if imgURL.lower().endswith('.jpeg') or \
           imgURL.lower().endswith('.jpg') or \
           imgURL.lower().endswith('.gif') or \
           imgURL.lower().endswith('.png') or \
           imgURL.lower().endswith('.bmp'):
            try:
                print('Downloading image %s...' % (imgURL))
                res = requests.get('http:' + imgURL)
                res.raise_for_status()
                imgFile = open(os.path.join('imgurSearch', os.path.basename(imgURL)), 'wb')
                for chunk in res.iter_content(1000000):
                    imgFile.write(chunk)
                imgFile.close()
            except Exception:
                print (Exception)

# Prompt for search term
print('What would you like to search imgur for?')
searchterm = input()

imgurSearch(searchterm)
