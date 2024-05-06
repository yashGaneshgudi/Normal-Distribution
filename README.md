# Normal-Distribution

A normal distribution is generated as seen below.

![image](https://github.com/yashGaneshgudi/Normal-Distribution/assets/153029336/567c5b22-d9b1-4fde-9c00-1efe9912dfb7)


It works by working out the amount of times heads is flipped when you flip the coin 1000 times.
It then repeats 1000 flips 100K times.

The result is a normal distribution showing the distribution of values as a histogram using matplotlib.

![image](https://github.com/yashGaneshgudi/Normal-Distribution/assets/153029336/1345ab99-f3f8-477a-bbf7-23ab7662b200)

Issues I encountered was that the generated graph looked fixed not fluid like a normal distribution.
![image](https://github.com/yashGaneshgudi/Normal-Distribution/assets/153029336/8c1a199c-2842-4963-a3ec-21214529851e)
Fixed by using the bins function on matplotlib to make sepeate intervals and increasing the size of each trial.

Reference:
https://stackoverflow.com/questions/78437177/matplotlib-histogram-data-automatically-grouped/78437679#78437679
