import urllib.request as url
from bs4 import BeautifulSoup
import requests
import shutil
import os
import sys


def downloadAllImages(celeb, fromPage, numberOfPages):
    """ This func was NOT written by me """

    urli = 'http://celebmafia.com/' + celeb + '/'

    for i in range(fromPage, fromPage+numberOfPages+1):
        wiki = urli+"page/"+str(i)+'/'
        print(wiki)

        r = url.Request(wiki, headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
        html = url.urlopen(r)
        soup = BeautifulSoup(html)

        allPageLinks = []
        for nextlink1 in soup.findAll("a", {"class": "more-link"}):
            a = nextlink1.get('href')
            allPageLinks.append(a)

        print(os.getcwd())
        os.mkdir(celeb)
        os.chdir(celeb)

        for pagelink in allPageLinks:
            imgURL = pagelink
            r1 = url.Request(imgURL, headers={
                             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
            html1 = url.urlopen(r1)
            soup = BeautifulSoup(html1)

            allimageLinks = []
            for nextlink1 in soup.findAll("a"):
                a = nextlink1.get('href')
                allimageLinks.append(a)

            lo = [s for s in allimageLinks if '.jpg' in s]

            for image in lo:
                r = requests.get(image, stream=True)

                if r.status_code == 200:
                    print(
                        '_img'
                        + str(allPageLinks.index(pagelink))
                        + str(lo.index(image))
                        + '.jpg')

                    with open(
                        '_img'
                        + str(allPageLinks.index(pagelink))
                        + str(lo.index(image))
                            + '.jpg', 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)


downloadAllImages('mackenzie-foy', 1, 5)
