import sys

hs = {
'I': 0, 'V': 0, 'L': 0, 'F': 0, 'C': 0,
'M': 0, 'A': 0, 'G': 0, 'T': 0, 'S': 0,
'W': 0, 'Y': 0, 'P': 0, 'H': 0, 'E': 0,
'Q': 0, 'D': 0, 'N': 0, 'K': 0, 'R': 0
}

seq = sys.argv[1]
unknown = 0
for aa in seq:
	if aa in hs: hs[aa] += 1
	else: unknown += 1

keys = list(hs.keys())
keys.sort()
for key in keys: print(f'{key}\t{hs[key]}')

if unknown: print(f'unknown\t{unknown}')
