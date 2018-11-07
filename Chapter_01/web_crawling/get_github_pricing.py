from lxml import html
import requests

page = requests.get('https://github.com/pricing/')
tree = html.fromstring(page.content)

print(f"Page object :", tree)

# These might change over time.
plans = tree.xpath('//h2[@class="h3-mktg"]/text()')
price = tree.xpath('//span[@class="default-currency"]/text()')

print(f"Plans: {plans}, \nPrice: {price}")