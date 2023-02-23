import argparse
import os
import re
import stat
import sys

def humanify(n):
	if   n > 1e12: return f'{n/1e12:.2f}T'
	elif n > 1e9:  return f'{n/1e9:.2f}G'
	elif n > 1e6:  return f'{n/1e6:.2f}M'
	elif n > 1e3:  return f'{n/1e3:.2f}K'
	else:          return n

def dehuman(s):
	if   s.endswith('k') or s.endswith('K'): return int(s[:-1]) * 1e3
	elif s.endswith('m') or s.endswith('M'): return int(s[:-1]) * 1e6
	elif s.endswith('g') or s.endswith('G'): return int(s[:-1]) * 1e9
	elif s.endswith('t') or s.endswith('T'): return int(s[:-1]) * 1e12
	else: return int(s)

parser = argparse.ArgumentParser(description='Find duplicate files.')
parser.add_argument('path', type=str, metavar='<path>')
parser.add_argument('--min', type=str, metavar='<min size>', default = '10M',
	help='minimum file size (may use K, M, G, T) [%(default)s]')
parser.add_argument('--bytes', type=int, metavar='<bytes>', default = 128,
	help='number of bytes to read for pseudo-checksum [%(default)s]')
parser.add_argument('--skip', type=str, metavar='<tokens>', nargs='+',
	help='skip specific tokens, e.g. anaconda')
parser.add_argument('--duplicates', action='store_true',
	help='show all duplicte file paths and failed paths')
parser.add_argument('--denied', action='store_true',
	help='show all paths that deny permission')
parser.add_argument('--hidden', action='store_true',
	help='include hidden (configuration) files and directories')
parser.add_argument('--progress', action='store_true',
	help='show progress')
arg = parser.parse_args()


# Global stats
failed_paths = {}
config_files = 0
config_space = 0
skip_files = 0
skip_space = 0
locked_files = 0
locked_space = 0
small_files = 0
small_space = 0
check_files = 0
check_space = 0


# Index all files by their size
size = {}
minsize = dehuman(arg.min)
filecount = 0
for path, subdirs, files in os.walk(arg.path):
	for name in files:
		filecount += 1
		if arg.progress: print(f'sizing {filecount}', end='\r', file=sys.stderr)
		
		filepath = os.path.join(path, name)
		try:
			mode = os.lstat(filepath).st_mode
		except:
			if path not in failed_paths: failed_paths[path] = 0
			failed_paths[path] += 1
			continue
		if not stat.S_ISREG(mode): continue
		s = os.path.getsize(filepath)

		# check for hidden files and directories (leading .)
		if '/.' in filepath and not arg.hidden:
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

		# check for read permissions - need later for checksum
		if not os.access(filepath, os.R_OK):
			locked_space += s
			locked_files += 1
			continue

		# check for minimum file size
		if s < minsize:
			small_space += s
			small_files += 1
			continue
		if s not in size: size[s] = []
		size[s].append(filepath)
		check_space += s
		check_files += 1
if arg.progress: print(file=sys.stderr)

# Find duplicate files (1) by file size (2) by pseudo-checksum
waste_space = 0
waste_files = 0
duplicates = []
filecount = 0
for s in sorted(size, reverse=True):
	filecount += 1
	if arg.progress: print(f'checking {filecount}', end='\r', file=sys.stderr)
	
	if len(size[s]) == 1: continue

	# Create a pseudo-checksum by looking at the head and tail of a file
	pseudosum = {}
	for filepath in size[s]:
		with open(filepath, mode='rb') as fp:
			head = fp.read(arg.bytes)
			tail = None
			if s > arg.bytes:
				fp.seek(-arg.bytes, 2)
				tail = fp.read(arg.bytes)
			sig = (head, tail)
			if sig not in pseudosum: pseudosum[sig] = []
			pseudosum[sig].append(filepath)

	# Save duplicates
	for sig in pseudosum:
		if len(pseudosum[sig]) == 1: continue
		duplicates.append( (s, pseudosum[sig]) )
		waste_space += (len(pseudosum[sig]) -1) * s
		waste_files += len(pseudosum[sig]) -1
if arg.progress: print(file=sys.stderr)

# Summary report
print(f'Hidden Files: {config_files}')
print(f'Hidden Space: {humanify(config_space)}')
print(f'Skipped Files: {skip_files}')
print(f'Skipped Space: {humanify(skip_space)}')
print(f'Locked Files: {locked_files}')
print(f'Locked Space: {humanify(locked_space)}')
print(f'Small Files: {small_files}')
print(f'Small Space: {humanify(small_space)}')
print(f'Checked Files: {check_files}')
print(f'Checked Space: {humanify(check_space)}')
if check_files != 0 and check_space != 0:
	print(f'Duplicate Files: {waste_files} ({waste_files/check_files:.3f})')
	print(f'Duplicate Space: {humanify(waste_space)} ({waste_space/check_space:.3f})')

# Duplicates report
if arg.duplicates:
	print('\nDuplicates')
	for s, files in duplicates:
		print(humanify(s))
		for f in files:
			print(f'\t{f}')

# Denied report
if arg.denied:
	print('\nDenied')
	for path in failed_paths:
		print(failed_paths[path], path)
