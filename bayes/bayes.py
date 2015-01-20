#assignment 4 bayes net Andrew Gordon

import getopt
import argparse
import sys
 


"""
-g = conditional probability
-j = joint probability
-m = marginal probability

-P = Pollution, -p = low pollution
-S = Smoker
-C = Cancer
-D = Dyspnoea
-X = X-ray

Markov Blankey:
parents:
	pollution, smoker
descendant(pollution, smoker):
	cancer
descendant(cancer):
	Xray, Dyspnoea
"""

probabilities = {'p' : .1, '~p' : .9,'s' : .3, '~s' : .7, 'x|c' : .9, '~x|c' : .1, 
					'd|c' : .65, '~d|c' : .3, 'c|p,s' : .05, 'c|~p,s' : .03, 'c|p,~s': .02, 'c|~p,~s' : .001}

options = "- P S C D X g j m".split()

args = []

try:
	for x in range(1,len(sys.argv)):
		if sys.argv[x] in probabilities or sys.argv[x] in options:
			args.append(sys.argv[x])
except:
	print "parsing error"

print args



def main():
	return






































































"""
def argparse():
	for x in range(0,len(args)):
		if args[x] == '~':
			if args[x+1].islower():
				probabilities[args[x+1]] = False
			else:
				print p
		if args[x] == '|':
			print 'bar'
		# if x.islower() and != '~' and != '|' and != 'g' and != 'm' and != 'j':
		# 	print 'lowercase'
"""



#fuck all of this 
# try:
# 	for x in range(1,len(sys.argv)):
# 		if sys.argv[x][0] == '-':
# 			for y in range(1,len(sys.argv[x])):
# 				if sys.argv[x][y] in options:
# 					if sys.argv[x][y] == '~':
# 						args.append(sys.argv[x][y] + sys.argv[x][y+1])
# 						y = y+1
# 					elif sys.argv[x][y] == '|':
# 						args.append(sys.argv[x][y] + sys.argv[x][y+1])
# 						y+=1
# 					else:
# 						if '~' + sys.argv[x][y] in args:
# 							pass
# 						else:
# 							args.append(sys.argv[x][y])
# 				else:
# 					print sys.argv[x][y], "not in available options, deleting..." 
# except:
# 	print "Error in parsing command line!"	
