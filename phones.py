from random import seed
from random import random
# seed random number generator
seed(1)
# generate random numbers between 0-1

with open("C:\\Users\\Rajdeep\\Desktop\\numbers.txt", "w") as f:
    for _ in range(6000):
        value = str(random())[2:12]
        if int(value[:2]) > 65:
            f.write(value + '\n')
        
