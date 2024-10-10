import random
print(random.random()) 

import random
print(random.randint(1, 100))  
print(random.randint(1, 100))



import  random


print(random.randrange(1, 10)) 
print(random.randrange(1, 10, 2))
print(random.randrange(0, 101, 10))



import random
print(random.choice('computer'))  
print(random.choice([12,23,45,67,65,43]))
print(random.choice((12,23,45,67,65,43)))


import random
aList = [20, 40, 80, 100, 120]
sampled_list = random.sample(aList, 3)
print(sampled_list)

import random


# create list of 5 random numbers
num_list = random.sample(range(100), 5)
print(num_list)