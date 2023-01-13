import sys
import random

# Number of features
ftrnum = int(sys.argv[1])
# Number of chromosomes
chrnum = int(sys.argv[2])
# Sequence length
seqlen = int(sys.argv[3])
# Feature length
ftrlen = int(sys.argv[4])

features = []
while len(features) < ftrnum:
	start = random.randint(1,seqlen)
	cur_ft = (random.randint(1,chrnum), start)
	taken = False
	for ft in features:
		if cur_ft[0] == ft[0] and abs(cur_ft[1]-ft[1]) < ftrlen:
			taken = True
			break
	if not taken: features.append(cur_ft)
	
for ft in features:
	chrom = ft[0]
	start = ft[1]
	end = start+ftrlen-1
	print(chrom, 'rand_gen', 'exon', start, end, '.', '.', '.', '.', sep='\t')

