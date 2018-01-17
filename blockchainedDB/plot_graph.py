import numpy as np

NUM_ITERS = 100
from numpy import genfromtxt
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

data_iterative = genfromtxt('comparehc_iter1_diff', delimiter=',', skiprows=1)
data_random = genfromtxt('comparehc_random1_diff.csv', delimiter=',', skiprows=1)

time_iterative = np.array(data_iterative[:,0] - data_iterative[0][0])
time_random = np.array(data_random[:,0] - data_random[0][0])

fig = plt.figure(figsize=(10,10))
plt.xlabel("TIME")
plt.ylabel("BLOCK INDEX")
plt.title("RANDOM")     

#print(len([i for i in range(len(time_iterative))]))
#print(len(time_iterative))

plt.plot(time_iterative, np.array([i for i in range(len(time_iterative))]), label = "iteractive method")

plt.plot(time_random, np.array([i for i in range(len(time_random))]), label = "random method")

fontP = FontProperties()
fontP.set_size('large')
plt.legend(prop=fontP)

plt.legend(loc=2, bbox_to_anchor=(0.6,0.5))
plt.show() 
fig.savefig('COMPARSION diff2 iter100.png')
