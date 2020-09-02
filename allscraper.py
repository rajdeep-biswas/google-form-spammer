from lxml import html
import requests

page = requests.get('https://collegedunia.com/kolkata-colleges')
tree = html.fromstring(page.content)

names = tree.xpath('//h3/text()')

for name in names:
    print(name[1::])

