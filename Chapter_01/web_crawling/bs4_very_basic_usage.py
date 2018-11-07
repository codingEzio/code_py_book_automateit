import bs4

with open('./a_page_for_bs4.html', 'r') as mypage:
	soup = bs4.BeautifulSoup(mypage, "lxml")

print(f"{type(soup)}\n")


def find_it_first():
	aha = [
		soup.find('div', {'id': 'tagdiv'}),
		soup.find_all('strong'),
		soup.find_all('a'),
		soup.select('#tagdiv'),
		soup.select('.tagp'),
	]


def then_get_text():
	yay = [
		soup.find_all('a')[0]['href'],
		soup.find('div', {'id': 'tagdiv'}).text,
		soup.select('span')[0].getText(),
	]
	
	for i in yay:
		print(i)


# find_it_first()
then_get_text()