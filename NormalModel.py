import random

results=[]

for i in range (100000):
    heads=0
    print(i)
    for i in range(1000):
        coin = random.randint(0, 1)
        if coin == 1:
            heads += 1
    results.append(heads)
    print(heads)

import matplotlib.pyplot as plt
plt.hist(results,bins=500)
plt.show()
