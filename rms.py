"""
rms.py - a function that returns a collection of the best motifs
Date - 09/11/20
Author - Daniel Throop
Class - COSC 3090

"""

import random


def randomizedMotifSearch(dna, k, t):
	allMotifs = []
	motifs = []
	bestMotifs = []
	concencous = ""
	score = 0

	#intializing profile matrix with 't' rows and 'k' colums

	w, h = k, t;
	profile = [[0 for x in range(w)] for y in range(h)] 


	allMotifs = (randomMotifs(dna, k, t))[0]		
	motifs = (randomMotifs(dna, k, t))[1]

	# print(allMotifs)
	# print(motifs)

	bestMotifs = motifs

	#main loop	
	while(True):

		#obtain the profile and concencous string
		profile = makeProfile(motifs, profile, k, t)[0]
		concencous = makeProfile(motifs, profile, k, t)[1]

		#creating motifs(profile(motifs), dna)
		motifs = profileScore(profile, allMotifs, dna, k, t)

		if(scoreMotifs(motifs, concencous) < scoreMotifs(bestMotifs, concencous)):
			bestMotifs = motifs
		else:
			print(bestMotifs)
			return bestMotifs


#TESTED -> WORKS
#returns a list of t random k-mers
def randomMotifs(dna, k, t):
	motifs = []
	temp = []
	transfer = []
	randomMotifs = []
	
	#filling list with all possible k-mers 
	for i in range(t):
		for j in range((len(dna[i]) + 1) - k):
			temp.append((dna[i])[j:(j+k)])

		#selecting random k-mer from string 'i'
		randomMotifs.append(random.choice(temp))

		#transferring temp list and appending to overall motif tracker
		transfer = temp
		motifs.append(transfer)

		#resetting temp array
		temp = []

	return motifs, randomMotifs
	


#determines the profile of t strings of dna
#TESTED -> WORKS
def makeProfile(motifs, profile, k, t):
	char = ' '
	#intializing profile matrix with 't' rows and 'k' colums
	profile = [[0 for x in range(k)] for y in range(4)] 

	
	#TESTED -> WORKS
	#counts
	for i in range(t):
		for j in range(k):
			char = motifs[i][j]
			if(char == 'A'):
				profile[0][j] += 1

			elif(char == 'C'):
				profile[1][j] += 1	

			elif(char == 'G'):
				profile[2][j] += 1	

			elif(char == 'T'):
				profile[3][j] += 1

	#TESTED -> WORKS
	#pseudo-counts
	for i in range(4):
		for j in range(k):
			profile[i][j] += 1 


	#TESTED -> WORKS
	#probabilities 	
	for i in range(4):
		for j in range(k):
			profile[i][j] /= float((t+4))

	
	#TESTED -> WORKS
	#building concencous string 
	concencous = ""
	for i in range(k):
		let = 'A'
		highest = profile[0][i]
		for j in range(1,4):
			if(profile[j][i] > highest):
				if(j == 1):
					let = 'C'
				elif(j == 2):
					let = 'G'
				elif(j == 3):
					let = 'T'
				highest = profile[j][i]

		concencous += let
		highest = 0.0
	

	return profile, concencous





#determines the score of t strings of dna given a profile
#@returns - highest scoring k-mer (using the profile) from each string of dna 
#TESTED -> WORKS
def profileScore(profile, motifs, dna, k, t):
	currScore = 1.0
	highestScore = 0.0
	currKmer = ""
	profileCol = 0
	temp = []
	finalMotifs = []
	stringScores = {}
	scores = []



	#inserting the scores of each kmer in each string into 'scores'
	for i in range(len(motifs)):
		for j in range(len(motifs[i])):
			currKmer = motifs[i][j]

			#creating score of currKmer based off of profile
			for x in range(k):
				if(currKmer[x] == 'A'):
					currScore *= profile[0][x]
				elif(currKmer[x] == 'C'):
					currScore *= profile[1][x]
				elif(currKmer[x] == 'G'):
					currScore *= profile[2][x]
				elif(currKmer[x] == 'T'):
					currScore *= profile[3][x]



			stringScores[currScore] = currKmer
			currScore = 1.0

		temp = stringScores
		scores.append(temp)
		stringScores = {} 


	maxProb = 0.0

	#determing the maximum scored k-mer in each string
	for i in range(len(scores)):
		for prob in scores[i]:
			if(prob > maxProb):
				maxProb = prob

		#appending the maximum probabilty k-mer of each string in dna
		finalMotifs.append(scores[i][maxProb])
		maxProb = 0.0


	# print(motifs)
	# printProfile(profile)
	# print(scores)
	# print(finalMotifs)
	

	return finalMotifs 


#TESTED -> WORKS 
#determines the score (distance) of motifs using concencous
#@returns the score
def scoreMotifs(motifs, concencous):
	score = 0

	#determining the hamming distance between concencous and each motif in motifs
	for i in range(len(motifs)):
		for j in range(len(motifs[i])):
			if(motifs[i][j] != concencous[j]):
				score += 1



	return score


def printProfile(profile):

	for i in range(4):
		print(profile[i])
		print('\n')

	return


#TESTING

# dna = ["AGCTGCAT", "GACCTACC", "GGCTACCT", "CCCAATGG"]

dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]


randomizedMotifSearch(dna, 8, 5)










