#!/usr/bin/python

import itertools

def iterative_levenshtein(s, t, costs=(1, 1, 1)):

    rows = len(s)+1
    cols = len(t)+1
    deletes, inserts, substitutes = costs
    
    dist = [[0 for x in range(cols)] for x in range(rows)]
    # deletions:
    for row in range(1, rows):
        dist[row][0] = row * deletes
    # insertion
    for col in range(1, cols):
        dist[0][col] = col * inserts
        
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = substitutes
            dist[row][col] = min(dist[row-1][col] + deletes,
                                 dist[row][col-1] + inserts,
                                 dist[row-1][col-1] + cost) # substitution
    for r in range(rows):
        print(dist[r])
    
    return dist[row][col]

list1=[]
list2=[]
pairs=[]

outfile = r"/Users/lscpuser/Desktop/trytest.txt" # to adapt
text = open(outfile,"r")
for line in text:
 line1=line.strip('\n')
 list1.append(line1)
list1 = filter(None, list1)

for L in range(0, len(list1)+1):
  for subset in itertools.combinations(list1, 2):
  	pairs.append(subset)
for x in pairs:
	if x not in list2:
		list2.append(x)
		


for combination in list2:
		print(combination[0], combination[1])
		print(iterative_levenshtein(combination[0], combination[1], costs=(1, 1, 1)))
	

