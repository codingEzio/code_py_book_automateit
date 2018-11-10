from bs4 import BeautifulSoup
from threading import Thread
import requests

home_url = "https://www.yelp.com"
find_wat = "restaurants"
location = "HongKong"

# single string (splited into multilines)
search_url = (
    "https://www.yelp.com/search?find_desc="
    + find_wat
    + "&find_loc=" + location
)

srch_html = requests.get(search_url).content
srch_soup = BeautifulSoup(srch_html, features="lxml")

# get Top5
srch_urls = srch_soup.select('.biz-name')[:5]

urls = []
for u in range(len(srch_urls)):
    urls.append(home_url + srch_urls[u]['href'])  # link only

# --- actual scraping begins!! ---


def fuckin_scrape_it(url):

    page = requests.get(url).content
    soup = BeautifulSoup(page, features="lxml")

    title = soup.select('.biz-page-title')
    address = soup.select('.street-address')
    phone = soup.select('.biz-phone')

    if title:
        print(f'title   : {title[0].getText().strip()}')
    if address:
        print(f'address : {address[0].getText().strip()}')
    if phone:
        print(f'phone   : {phone[0].getText().strip()}')

    print('-' * 25)


thread_list = []

i = 0

while i < len(urls):
    t = Thread(target=fuckin_scrape_it, args=(urls[i],))
    t.start()
    thread_list.append(t)
    i = i + 1

for t in thread_list:
    t.join()
