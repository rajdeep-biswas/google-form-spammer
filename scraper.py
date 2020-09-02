from lxml import html
import requests

page = requests.get('http://www.first-names-meanings.com/country-indian-names.html')
tree = html.fromstring(page.content)

names = tree.xpath('//td//a/text()')

with open("C:\\Users\\Rajdeep\\Desktop\\firstnames.txt", "w") as f:
    for name in names:
        f.write(name + '\n')

page = requests.get('https://blogs.transparent.com/hindi/common-surnames-in-india/')
tree = html.fromstring(page.content)

names = tree.xpath('//p/text()')

lnames = []

for name in names:
    lnames.append(name[str(name).find('–') + 2::])

for item in lnames:
    print(item)

page = requests.get('https://collegedunia.com/kolkata-colleges')
tree = html.fromstring(page.content)

names = tree.xpath('//h3/text()')

for name in names:
    print(name[1::])
