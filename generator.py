import random
from random import random as rndm
from random import seed
seed(1)

fnames = []
lnames = []
locations = []
colleges = []
numbers = []

with open('C:\\Users\\Rajdeep\\Desktop\\firstnames.txt') as f:
    for item in f:
        fnames.append(item)

with open('C:\\Users\\Rajdeep\\Desktop\\lastnames2.txt') as f:
    for item in f:
        lnames.append(item)

with open('C:\\Users\\Rajdeep\\Desktop\\colleges.txt') as f:
    for item in f:
        colleges.append(item)

with open('C:\\Users\\Rajdeep\\Desktop\\locations.txt') as f:
    for item in f:
        locations.append(item)

with open('C:\\Users\\Rajdeep\\Desktop\\numbers.txt') as f:
    for item in f:
        numbers.append(item)

for i in range(3):
    fname = random.choice(fnames).strip()[:-1]
    lname = random.choice(lnames).strip()
    print((fname + ' ' + lname) + ' studies at ' + random.choice(colleges).strip() + ' is from ' + random.choice(locations).strip() + ' can be called at ' + random.choice(numbers).strip() + ' and can be reached at ' + (fname + lname).lower() + str(rndm())[2:5] + '@gmail.com')
    print()

for i in range(50):
    print(int(str(rndm())[2:3]) % 3 + 1)
