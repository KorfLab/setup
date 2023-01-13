import sys
import math
import argparse
from readfasta import read_fasta

parser = argparse.ArgumentParser(
	description='complexity filter')
parser.add_argument('fa', type=str, metavar='<fasta path>',
	help='path to fasta file')
parser.add_argument('-w', type=int, default=11, metavar='<int>',
	help='input window size [%(default)s]')
parser.add_argument('-t', type=float, default=1.1, metavar='<float>',
	help='input entropy threshold [%(default)s]')
parser.add_argument('-lc', action='store_true',
	help='mask to lowercase, (default mask to N)')
arg = parser.parse_args()

def entropy(count, w):
	pa = count['A'] / w
	pc = count['C'] / w
	pg = count['G'] / w
	pt = count['T'] / w
	
	h = 0
	if pa > 0: h -= pa * math.log(pa)
	if pc > 0: h -= pc * math.log(pc)
	if pg > 0: h -= pg * math.log(pg)
	if pt > 0: h -= pt * math.log(pt)
	h /= math.log(2)
	
	return h

def mask(seq, w, t, lc):
	count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
	seq = seq.upper()
	new = list(seq)
	for i in range(len(seq)-w+1):
		# first window
		if i == 0:
			for base in seq[0:w]:
				if base in count: count[base] += 1
				else: sys.exit(f'Unrecognized base: {base}')
			if entropy(count, w) < t:
				pos = i + int(w/2)
				if lc: new[pos] = new[pos].lower()
				else:  new[pos] = 'N'
			to_rmv = seq[i]
		# subsequent windows
		else:
			to_add = seq[i+w-1]
			count[to_rmv] -= 1
			count[to_add] += 1
			to_rmv = seq[i]
			if entropy(count, w) < t:
				pos = i + int(w/2)
				if lc: new[pos] = new[pos].lower()
				else:  new[pos] = 'N'
				
	return ''.join(new)

# Main
w  = arg.w
t  = arg.t
lc = arg.lc

for idn, seq in read_fasta(arg.fa):
	print(f'>{idn}')
	masked = mask(seq, w, t, lc)
	for i in range(0, len(masked), 80): print(masked[i:i+80])
