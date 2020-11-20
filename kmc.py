"""
kmc.py - a function that implements the lloyd's algorithim for k-means clustering
Date - 11/18/20 
Author - Daniel Throop
Class - COSC 3090

"""

import random
import math


def kmc(k, m, points):
	centers = [[0, 0], [0, 0]]
	clusters = [[],[]]
	noChange = True 
	arb = 0 

	
	# Create k arbitrary clusters - pick k points as cluster center and assign
	# each other point to the closest center

	# check if the centers have changed 
	while(noChange):

		# working
		# create k aribitrary centers
		for i in range(k):
			# assign k centers
			arb = random.randint(0, len(points) - 1)
			print(arb)
			centers[i] = points[arb]

		# assign k aribitrary clusters
		for i in range(len(points)):
			if not (points[i] == centers[0] or points[i] == centers[1]):
				if distance(centers[0], points[i]) > distance(centers[1], points[i]):
					clusters[1].append(points[i])
				else:
					clusters[0].append(points[i])

		print(centers)
		print(clusters)

		# Re-compute the center of each cluster






		noChange = False





	



	

	# Re-assign points to clusters

	# repeat


	return centers

# calculates the distance between points p1 and p2
def distance(p1, p2):

	return (math.sqrt(((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2)))

# calculates the centroid for 
def centroidCalc(clusters):

	newCenterOne = [0, 0]
	newCenterTwo = [0, 0]
	xSum = 0
	ySum = 0

	for i in range(len(clusters[0])):
		



	return newCenterOne, newCenterTwo





# TESTING

# Test 1

test1 = [[1.3, 1.1], [1.3, .2], [.6, 2.8], [3.0, 3.2], [1.2, .7], [1.4, 1.6], [1.2, 1.0], [1.2, 1.1], [.6, 1.5], [1.8, 2.6], [1.2, 1.3], [1.2, 1.0], [0.0, 1.9]]
print(test1)

kmc(2, 2, test1)

# expected output

# 1.800 2.876
# 1.060 1.140