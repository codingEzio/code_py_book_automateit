from bs4 import BeautifulSoup
import subprocess
import requests

# url
KEYWORD = "Mary+Elizabeth+Winstead"
url = u"https://celebmafia.com/page/1/?s=" + KEYWORD

# [celeb list reminder]
# 	mackenzie+foy
# 	Mary+Elizabeth+Winstead

# get page
page = requests.get(url).text
soup = BeautifulSoup(page, features="lxml")

# find picture links
#   The link itself reveals how many pics out there!
#   e.g.
# 		"... /2018/10/mary-elizabeth-winstead- ... -in-la-6.jpg"
# 	That means this album got 7 pictures
# 		both starts with the same url
# 		only the '6' changed to (0, 1, 2, 3, 4, 5, 6)
images = [i['src']
          for i in soup.find_all('img', {"class": "wp-image-143424"})]


# thumbnail => full resolution
img_full = []

for i in images:
    i = i.replace('_thumbnail', '')
    img_full.append(i)

# download


def down_it(flags="no"):

    if flags == "yes":
        for i in img_full:
            cmd = ['wget', i, '-P', 'tmp']
            subprocess.run(cmd)


down_it()


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
