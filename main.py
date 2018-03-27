"""
    Author: Ali Ghelmani,   Date: 3/27/2018
    The original goal was to write an image downloader to get
    all the images from a website but for now I've settled to
    links only! :(
    to be completed ...
"""

import requests
from bs4 import BeautifulSoup
# import shutil


def web_img_downloader(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.misucell.com/group/high-resolution-dark-wallpaper/'
        source = requests.get(url)
        plain_text = source.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        # print(soup.prettify())
        fw = open('links.txt', 'w')
        fw.close()
        for link in soup.find_all('a', {'style': 'text-decoration: none; color:#777;'}):
            href = link.get('href')
            href = 'http://www.misucell.com' + href
            # print(href)
            one_step_crawler(href)
        page += 1


def one_step_crawler(url):
    source = requests.get(url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for link in soup.find_all('a', {'class': 'ffl_info'}):
        href = link.get('href')
        href = 'http://www.misucell.com' + href
        fr = open('links.txt', 'a')
        fr.write(href + '\n')
        fr.close()
        '''
        source2 = requests.get(href)
        if source2.status_code == 200:
            with open('1.jpg', 'wb') as f:
                source2.raw.decode_content = True
                shutil.copyfileobj(source2.raw, f)
                
        '''


web_img_downloader(1)