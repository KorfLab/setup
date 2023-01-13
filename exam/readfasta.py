import sys
import gzip

def read_fasta(fasta):
	if fasta.endswith('.gz'): fh = gzip.open(fasta, 'rt')
	else: fh = open(fasta)
	idn = ''
	seq = ''
	while True:
		line = fh.readline().strip()
		if line == '': break
		if line.startswith('>'): 
			if idn: 
				yield idn, seq
				idn = line[1:]
				seq = ''
			else: idn = line[1:]
		else: seq += line
	if idn: yield idn, seq
