from selenium import webdriver

browser = webdriver.Chrome()

browser.get(
    "https://github.com/"
    "PacktPublishing/Automate-it/tree/master/Chapter01")

author = browser.find_element_by_class_name('commit-author').text
last_commit_time = browser.find_element_by_tag_name('relative-time').text

print(f'The author is [{author}],')
print(f'and the last commit is done on [{last_commit_time}]')

searchField = browser.find_element_by_name('q')  # what ...
searchField.send_keys('selenium')

# TODO
#   I dunno how to send a 'Enter'
#   I CAN easily send a 'Enter' by a button
#     But like "github", it does NOT have a explicit one!

# optional
browser.close()
