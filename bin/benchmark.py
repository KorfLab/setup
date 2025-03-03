import argparse
import itertools
import json
import random
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('--size', type=float, default=1e6,
	help='size of the benchmark [%(default)g]')
parser.add_argument('--tmpfile', default='bench.tmp',
	help='name of temp file [%(default)s]')
arg = parser.parse_args()

# part 1: create a table of random data
t0 = time.time()
with open(arg.tmpfile, 'w') as fp:
	for _ in range(int(arg.size)):
		uid = ''.join(random.choices('ACGT', k=5))
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
#print(json.dumps(dol, indent=3))
