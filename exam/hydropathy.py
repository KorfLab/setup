import sys
import argparse

parser = argparse.ArgumentParser(
	description='Calculate the hydropathy score of a given sequence')
parser.add_argument('seq', type=str, metavar='<stdin>',
	help='input sequence (stdin)')
parser.add_argument('-w', type=int, default=7, metavar='<int>',
	help='input window size [%(default)s]')
arg = parser.parse_args()

hs = {
'I': 4.5,  'V': 4.2,  'L': 3.8,  'F': 2.8,  'C': 2.5,
'M': 1.9,  'A': 1.8,  'G': -0.4, 'T': -0.7, 'S': -0.8,
'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def local_hydropathy(seq, hs):
	total = 0
	for aa in seq:
		total += hs[aa]
	return total / len(seq)

seq = arg.seq
win = arg.w
if len(seq) < win: sys.exit('sequence length is shorter than window length')
scores = []
for i in range(len(seq) - win + 1):
	local = seq[i:i+win]
	scores.append(local_hydropathy(local, hs))

tblout = ''
for score in scores: tblout += f'{score:.3f}\t'
print(tblout)


