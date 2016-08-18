import numpy as np

import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from core import greedy,optimal,total_dist

def plot_a_map(size,start,coords,order,color,background_img):
	plt.plot(start[0],start[1],'or',markersize =10)
	plt.plot([e[0] for e in coords],[e[1] for e in coords],'+w',markersize =10)

	coords_x = [coords[e][0] for e in order]
	coords_y = [coords[e][1] for e in order]
	coords_x.insert(0,start[0])
	coords_y.insert(0,start[1])
	coords_x = np.array(coords_x)
	coords_y = np.array(coords_y)
	plt.plot(coords_x,coords_y,linewidth=2.0,color = color)
	angles = [math.atan2(coords_y[i+1]-coords_y[i],coords_x[i+1]-coords_x[i]) for i in range(len(coords_x)-1)]
	plt.quiver(coords_x[1:], coords_y[1:], [15*math.cos(a) for a in angles], [15*math.sin(a) for a in angles], color=color,pivot='tip',angles='xy', headwidth=15,scale=100, headlength=10)
	plt.xlim([0,size[0]])
	plt.ylim([0,size[1]])
	plt.grid()
	
	imgplot = plt.imshow(background_img, interpolation="bicubic",  zorder=0, extent=[0, size[0], 0, size[1]])

def reproduce_map():
	n = 8


	size = [1000.0,1000.0]
				#  0         1        2         3        4  

	all_sites = [[44,442],[212,515],[46,802],[275,92],[795,480],
#       5         6        7          8           9      10       11        12        13
	[886,842],[811,333],[337,252],[400,385],[650,676],[679,322],[788,252],[560,434],[908,419]]
	
	background_img=mpimg.imread('Untitled.png')
	plt.figure(figsize=(9,6))
	temp = 0
	for start_idx in [1,4]:
		start = all_sites[start_idx]
		coords = [e for i,e in enumerate(all_sites) if not i==start_idx]

		greedy_dist,greedy_order = greedy(start,coords)
		greedy_error_dist,greedy_error_order = greedy(start,coords,0.4)
		#optimal_dist,optimal_order = optimal(start,coords,greedy_dist)
		if start_idx == 4:
			optimal_dist,optimal_order = 2882.88169892,[8, 4, 12, 5, 10, 9, 11, 7, 6, 3, 0, 1, 2]
		else:
			optimal_dist,optimal_order = 2764.55415179,[1, 0, 2, 6, 7, 11, 9, 10, 5, 12, 3, 8, 4]
		diff = (greedy_dist-optimal_dist)/optimal_dist*100.0
		plt.subplot(2,3,1+temp*3)
		plot_a_map(size,start,coords,greedy_order,'#8888ff',background_img)

		plt.subplot(2,3,2+temp*3)
		plot_a_map(size,start,coords,greedy_error_order,'#dd88cc',background_img)
		
		plt.subplot(2,3,3+temp*3)
		plot_a_map(size,start,coords,optimal_order,'#77ff77',background_img)
		plt.tight_layout()
		#plt.show()
		print start_idx
		print "Greedy:",greedy_dist,total_dist(start,coords,greedy_order),greedy_order
		print "Greedy error:",greedy_error_dist,total_dist(start,coords,greedy_error_order),greedy_error_order
		print "Optimal:",optimal_dist,total_dist(start,coords,optimal_order),optimal_order
		temp = 1
	plt.savefig('mapi\\combinirana.png', dpi=300)

reproduce_map()
