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

def humanify(n):
	if   n > 1e12: return f'{n/1e12:.2f}T'
	elif n > 1e9:  return f'{n/1e9:.2f}G'
	elif n > 1e6:  return f'{n/1e6:.2f}M'
	elif n > 1e3:  return f'{n/1e3:.2f}K'
	else:          return n

# Index all files by their size
size = {}
total_size = 0
total_files = 0
for path, subdirs, files in os.walk(arg.path):
	for name in files:
		filepath = os.path.join(path, name)
		mode = os.lstat(filepath).st_mode
		if not stat.S_ISREG(mode): continue
		s = os.path.getsize(filepath)
		if s < arg.min: continue
		if s not in size: size[s] = []
		size[s].append(filepath)
		total_size += s
		total_files += 1

# Find duplicate files (1) by file size (2) by pseudo-checksum
wasted_size = 0
wasted_files = 0
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
		hs = humanify(s)
		print(hs, ' '.join(pseudosum[sig]))
		wasted_size += (len(pseudosum[sig]) -1) * s
		wasted_files += len(pseudosum[sig]) -1

print(f'Total Space: {humanify(total_size)}')
print(f'Total Files: {total_files}')
print(f'Wasted Space: {humanify(wasted_size)} ({wasted_size/total_size:.3f})')
print(f'Duplicate Files: {wasted_files} ({wasted_files/total_files:.3f})')
