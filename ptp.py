"""
ptp.py - A function that translates a RNA string into a amino acid string
Date - 09/11/20
Author - Daniel Throop
Class - COSC 3090

"""

# codon dictionary

codon = {'UUU':'Phe','UUC':'Phe','uua':'Leu','UUG':'Leu','CUU':'Leu','CUC':'Leu','CUA':'Leu','CUG':'Leu','AUU':'Ile','AUC':'Ile','AUA':'Ile','AUG':'Met','GUU':'Val','GUC':'Val','GUA':'Val','GUG':'Val','UCU':'Ser','UCC':'Ser','UCA':'Ser','UCG':'Ser','CCU':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro','ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr','GCU':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala','UAU':'Tyr','UAC':'Tyr','UAA':'STOP','UAG':'STOP','CAU':'His','CAC':'His','CAA':'Gln','CAG':'Gln','AAU':'N','AAC':'N','AAA':'Lys','AAG':'Lys','GAU':'Asp','GAC':'Asp','GAA':'E','GAG':'E','UGU':'Cys','UGC':'Cys','UGA':'STOP','UGG':'Trp','CGU':'R','CGC':'R','CGA':'R','CGG':'R','AGU':'Ser','AGC':'Ser','AGA':'R','AGG':'R','GGU':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'}


def ptp(string):
	amino = ""
	i = 0
	j = 3

	for c in range(int(len(string)/3)):
		
		current_kmer = string[i:j]

		if(codon[current_kmer] == 'STOP'):
			break
		else:
			amino += codon[current_kmer][0]

		i = i + 3
		j = j + 3

	print(amino)


# TESTING

# ptp("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")

