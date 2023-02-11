import argparse
import os
import stat

parser = argparse.ArgumentParser(description='Find duplicate files')
parser.add_argument('path', type=str, metavar='<path>')
parser.add_argument('--min', type=int, metavar='<min size>', default = 1024,
	help='minimum file size [%(default)s]')
parser.add_argument('--bytes', type=int, metavar='<bytes>', default = 128,
	help='number of bytes to read for pseudo-checksum [%(default)s]')
arg = parser.parse_args()

# Index all files by their size
size = {}
for path, subdirs, files in os.walk(arg.path):
	for name in files:
		filepath = os.path.join(path, name)
		mode = os.lstat(filepath).st_mode
		if not stat.S_ISREG(mode): continue
		s = os.path.getsize(filepath)
		if s < arg.min: continue
		if s not in size: size[s] = []
		size[s].append(filepath)

# Find duplicate files (1) by file size (2) by pseudo-checksum
for s in sorted(size, reverse=True):
	if len(size[s]) == 1: continue

	# Create a pseudo-checksum by looking at the head and tail of a file
	pseudosum = {}
	for filepath in size[s]:
		with open(filepath, mode='rb') as fp:
			head = fp.read(arg.bytes)
			fp.seek(-arg.bytes, 2)
			tail = fp.read(arg.bytes)
			sig = (head, tail)
			if sig not in pseudosum: pseudosum[sig] = []
			pseudosum[sig].append(filepath)

	# Report duplicates
	for sig in pseudosum:
		if len(pseudosum[sig]) == 1: continue
		ps = None
		if   s > 1e12: ps = f'{s/1e12:.2f}T'
		elif s > 1e9:  ps = f'{s/1e9:.2f}G'
		elif s > 1e6:  ps = f'{s/1e6:.2f}M'
		elif s > 1e3:  ps = f'{s/1e3:.2f}K'
		else:          ps = s
		print(ps, ' '.join(pseudosum[sig]))
