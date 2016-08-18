import random
import math

VERY_LARGE_NUMBER = 1000000000000

def dist(x,y,error_variance=0):
	'''
	Calculates the eucleadean distance between two points x and y, then multiply it by a random normal variable with mean=1 and error_variance
	'''
	error = 1.0
	if error_variance > 0:
		error = random.gauss(1,error_variance)
		error = min(max(0.7,error),1.3)
	dd = [x[i]-y[i] for i in range(len(x))]
	return math.sqrt(sum([e*e for e in dd]))*error

def total_dist(start,coords,order):
	total_dist = 0
	for i in range(len(order)):
		if i == 0:
			p1 = start
		else:
			p1 = coords[order[i-1]]
		p2 = coords[order[i]]
		total_dist += dist(p1,p2)
	return total_dist

def greedy(start,coords,error_variance=0):
	'''
	Implementation of the greedy algorithm
	'''
	n = len(coords)
	visited = [0 for e in coords]
	current = start

	for i in range(n):
		min_dist = VERY_LARGE_NUMBER
		min_k = -1
		for k in range(n):
			if visited[k] == 0:
				dist_ = dist(current,coords[k],error_variance)
				if dist_ < min_dist:
					min_dist = dist_
					min_k = k
		visited[min_k] = i+1
		current = coords[min_k]
	order = [visited.index(i) for i in range(1,1+n)]
	return total_dist(start,coords,order),order


def combinations(n,level,order,coords,dist_prev,min_dist_=VERY_LARGE_NUMBER):
	'''
	Helper function for the optimal algorithms
	'''
	if level == n:
		return dist_prev,order
	min_order = -1
	min_dist = min_dist_
	left = {e for e in range(n-1)}-set(order)
	for i in left:
		dist_next = dist_prev + dist(coords[i],coords[order[level-1]])
		if dist_next > min_dist:
			continue
		order[level] = i
		dist_,order_ = combinations(n,level+1,order,coords,dist_next,min_dist)
		if dist_ <= min_dist and order_ > -1:
			min_dist = dist_
			min_order = [e for e in order_]
		order[level] = -1
	return min_dist,min_order

def optimal(start,coords,min_dist_=VERY_LARGE_NUMBER):
	'''
	Implementation of the greedy algorithm
	'''
	n = len(coords)
	order = [-1 for e in range(n+1)]
	order[0] = n
	coords.append(start)
	min_dist,min_order = combinations(n+1,1,order,coords,0.0,min_dist_)
	del min_order[0]
	coords.pop()
	return min_dist,min_order

