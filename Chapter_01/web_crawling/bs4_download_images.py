from bs4 import BeautifulSoup
import subprocess
import requests

# url
KEYWORD = "mackenzie+foy"
url = u"https://celebmafia.com/page/1/?s=" + KEYWORD

# get page
page = requests.get(url).text
soup = BeautifulSoup(page, features="lxml")

# find picture links
images = [ i['src'] for i in soup.find_all('_img', {"class": "wp-image-143424"})]

# thumbnail => full resolution
img_full = []

for i in images:
	i = i.replace('_thumbnail', '')
	img_full.append(i)

# download
for i in img_full:
	cmd = ['wget', i, '-P', 'tmp']
	subprocess.run(cmd)


"""
--- piclink ---

<_img class="size-full wp-image-143424 " alt="Peyton List - Personal Pics 09/10/2018"
src="https://celebmafia.com/wp-content/uploads/2018/09/
peyton-list-personal-pics-09-10-2018-6_thumbnail.jpg" width="558">

--- page ---

https://celebmafia.com/page/1/?s=peyton+list

--- nice articles ---

stackoverflow.com/questions/37158246/how-to-download-images-from-beautifulsoup

"""