import argparse
import itertools
import json
import math
import random
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('--size', type=float, default=1e6,
	help='size of the benchmark [%(default)g]')
parser.add_argument('--tmpfile', default='bench.tmp',
	help='name of temp file [%(default)s]')
parser.add_argument('--seed', type=int, default=1,
	help='set random seed [%(default)i]')
arg = parser.parse_args()

random.seed(arg.seed)

k = math.ceil(math.log(arg.size / 10) / math.log(4))

# part 1: create a table of random data
t0 = time.time()
with open(arg.tmpfile, 'w') as fp:
	for _ in range(int(arg.size)):
		uid = ''.join(random.choices('ACGT', k=k))
		val = random.random()
		print(uid, val, sep='\t', file=fp)
t1 = time.time()
print(t1 - t0)

# part 2: read table of data into a dictionary of lists
t0 = time.time()
dol = {}
with open(arg.tmpfile) as fp:
	for line in fp:
		kmer, val = line.split()
		if kmer not in dol: dol[kmer] = []
		dol[kmer].append(float(val))
t1 = time.time()
print(t1 - t0)

# part 3: edit distance
t0 = time.time()
for k1 in dol:
	for k2 in dol:
		d = 0
		for nt1, nt2 in zip(k1, k2):
			if nt1 != nt2: d += 1
t1 = time.time()
print(t1 - t0)