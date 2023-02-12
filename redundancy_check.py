import argparse
import os
import re
import stat

parser = argparse.ArgumentParser(description='Find duplicate files')
parser.add_argument('path', type=str, metavar='<path>')
parser.add_argument('--min', type=int, metavar='<min size>', default = 1024,
	help='minimum file size [%(default)s]')
parser.add_argument('--bytes', type=int, metavar='<bytes>', default = 128,
	help='number of bytes to read for pseudo-checksum [%(default)s]')
parser.add_argument('--skip', type=str, metavar='<tokens>', nargs='+',
	help='skip specific tokens, e.g. anaconda')
parser.add_argument('--config', action='store_true',
	help='include configuration files and directories /.*')
arg = parser.parse_args()

def humanify(n):
	if   n > 1e12: return f'{n/1e12:.2f}T'
	elif n > 1e9:  return f'{n/1e9:.2f}G'
	elif n > 1e6:  return f'{n/1e6:.2f}M'
	elif n > 1e3:  return f'{n/1e3:.2f}K'
	else:          return n

# Global stats
total_files = 0
total_space = 0
locked_files = 0
locked_space = 0
config_files = 0
config_space = 0
skip_files = 0
skip_space = 0
small_files = 0
small_space = 0

# Index all files by their size
size = {}
for path, subdirs, files in os.walk(arg.path):
	for name in files:
		filepath = os.path.join(path, name)
		mode = os.lstat(filepath).st_mode
		if not stat.S_ISREG(mode): continue
		s = os.path.getsize(filepath)



		# check for config files and directories (leading .)
		if '/.' in filepath and not arg.config:
			config_space += s
			config_files += 1
			continue

		# check for user-specified skip tokens
		skip = False
		if arg.skip:
			for token in arg.skip:
				if token in filepath:
					skip = True
					break
		if skip:
			skip_space += s
			skip_files += 1
			continue

		# check for minimum file size
		if s < arg.min:
			small_space += s
			small_files += 1
			continue
		if s not in size: size[s] = []
		size[s].append(filepath)
		total_space += s
		total_files += 1

		# check for read permissions - need later for checksum
		try:
			fp = open(filepath)
			fp.close()
		except:
			locked_space += s
			locked_files += 1
			continue

# Find duplicate files (1) by file size (2) by pseudo-checksum
waste_space = 0
waste_files = 0
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
		print(humanify(s), ' '.join(pseudosum[sig]))
		waste_space += (len(pseudosum[sig]) -1) * s
		waste_files += len(pseudosum[sig]) -1

# Final report
print(f'Total Files: {total_files}')
print(f'Total Space: {humanify(total_space)}')
print(f'Duplicate Files: {waste_files} ({waste_files/total_files:.3f})')
print(f'Duplicate Space: {humanify(waste_space)} ({waste_space/total_space:.3f})')
print(f'Config Files: {config_files}')
print(f'Config Space: {humanify(config_space)}')
print(f'Skipped Files: {skip_files}')
print(f'Skipped Space: {humanify(skip_space)}')
print(f'Locked Files: {locked_files}')
print(f'Locked Space: {humanify(locked_space)}')
print(f'Small Files: {small_files}')
print(f'Small Space: {humanify(small_space)}')
