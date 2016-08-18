import random

import matplotlib.pyplot as plt

from core import greedy,optimal

def reproduce_greedy_with_error():

	size = [1000.0,1000.0]
	start = [e/2 for e in size]
	n_diffs = []
	repeats = 1000
	n = 10
	filename = "correct_res_batch_2_"+str(n)+"_"+str(repeats)+".txt"
	with open(filename,"w") as f:
		pass
	error_variances = [e*.04 for e in range(6,11)]

	for error_variance in error_variances:
		diffs = []
		for k in range(repeats):
			print error_variance,str(k+1)+"/"+str(repeats)
			coords = [[random.random()*e for e in size] for i in range(n)]

			greedy_dist,greedy_order = greedy(start,coords,error_variance)


			optimal_dist,optimal_order = optimal(start,coords,greedy_dist)

			diff = (greedy_dist-optimal_dist)/optimal_dist*100.0
			diffs.append(diff)
		with open(filename,"a") as f:
			f.write(str(error_variance)+":"+",".join([str(e) for e in diffs])+"\n")
		n_diffs.append(diffs)
	print [sum(diffs)/repeats for diffs in n_diffs]

def load_data_and_plot():
	filename = "correct_res_10_1000.txt"
	repeats = 1000
	n_diffs = []
	sigmas = [e*0.04 for e in range(11)]
	with open(filename,"r") as pin:
		for line in pin:
			sigma,diff_s = line.split(":")
			diffs = [float(e) for e in diff_s.split(",")]
			diffs.sort()
			n_diffs.append(diffs)

	plt.figure(figsize=(5,4))
	plt.boxplot(n_diffs)
	plt.xlabel('$\sigma$')
	labels = [str(e) if i%2==0 else '' for i,e in enumerate(sigmas)]
	labels.insert(0,'')
	plt.xticks(range(len(sigmas)+1), labels)
	plt.ylabel('Difference - %')
	plt.grid()
	plt.xlim([.5,len(sigmas)+.5])
	plt.ylim([-0.2,50.2])
	plt.yticks([e*5 for e in range(0,11)],[''if e%2==1 else str(e*5) for e in range(0,11) ])
	plt.tight_layout()
	plt.savefig('sigma_diff.png')




load_data_and_plot()