import sys
import argparse

parser = argparse.ArgumentParser(
	description='Find overlapped features between two gff files')
parser.add_argument('gff1', type=str, metavar='<gff path>',
	help='path to 1st gff file')
parser.add_argument('gff2', type=str, metavar='<gff path>',
	help='path to 2nd gff file')
arg = parser.parse_args()

def get_features(path):
	features = {}
	with open(path) as fh:
		while True:
			line = fh.readline().strip()
			if line == '': break
			fields = line.split()
			chrom = int(fields[0])
			start = int(fields[3])
			end   = int(fields[4])
			if chrom in features: features[chrom].append((start, end))
			else: features[chrom] = [(start, end)]
	return features

def find_overlap(fts1, fts2):
	overlaps = []
	for f1 in fts1:
		for f2 in fts2:
			if f1[1] >= f2[0] and f2[1] >= f1[0]:
				if f2[0] > f1[0]:
					if f2[1] > f1[1]: start, end = f2[0], f1[1]
					else: start, end = f2[0], f2[1]
				else:
					if f2[1] < f1[1]: start, end = f1[0], f2[1]
					else: start, end = f1[0], f1[1]
				overlaps.append(((start, end), f1, f2))
	return overlaps
fts1 = get_features(arg.gff1)
fts2 = get_features(arg.gff2)

print('chr\tbeg\tend\tbeg1\tend1\tbeg2\tend2')
for chrom in fts1:
	if chrom in fts2:
		overlaps = find_overlap(fts1[chrom], fts2[chrom])
		for overlap in overlaps:
			print(chrom, end='\t')
			for i in range(3):
				for j in range(2): print(overlap[i][j], end='\t')
			print()
	else: continue


