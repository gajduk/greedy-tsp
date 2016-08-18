import random

import matplotlib.pyplot as plt

from core import greedy,optimal

def optimal_greedy():

	size = [10.0,10.0]
	start = [e/2 for e in size]


	n_diffs = []
	repeats = 1000
	ns = range(4,12)

	for n in ns:
		diffs = []
		for k in range(repeats):
			print n,k
			coords = [[random.random()*e for e in size] for i in range(n)]

			greedy_dist,greedy_order = greedy(start,coords)


			optimal_dist,optimal_order = optimal(start,coords,greedy_dist)

			diff = (greedy_dist-optimal_dist)/optimal_dist*100.0
			diffs.append(diff)
		n_diffs.append(diffs)

	plt.figure(figsize=(5,4))
	plt.boxplot(n_diffs)
	plt.xlabel('#Collectibles')
	labels = [str(e) for e in ns]
	labels.insert(0,'')
	plt.xticks(range(len(ns)+1), labels)
	plt.ylabel('Difference - %')
	plt.grid()
	plt.xlim([.5,len(ns)+.5])
	plt.ylim([-0.2,30.2])
	plt.yticks([e*2 for e in range(0,16)],[''if e%3>0 else str(e*2) for e in range(0,16) ])
	plt.tight_layout()
	plt.savefig('A1_difference.png')

optimal_greedy()