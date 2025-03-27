"""
Miscellaneous functions for typical bioinformatics tasks.
"""

import gzip
import itertools
import json
import math
import random
import re

## Math Functions ##

def sumlog(v1, v2):
	"""Returns the sum of two logspaced values in logspace"""
	if v1 < v2: v1, v2 = v2, v1
	return math.log(1 + math.exp(v2 - v1)) + v1

def kmers(k, alph='ACGT', init=0):
	"""Creates a dictionary of kmers"""
	table = {}
	for t in itertools.product(alph, repeat=k):
		table[''.join(t)] = init
	return table

## Sequence Functions ##

def random_dna(length, a=0.25, c=0.25, g=0.25, t=0.25):
	"""Generates random nucleotide sequence"""

	assert(math.isclose(a+c+g+t, 1.0))
	seq = ''
	for i in range(length):
		r = random.random()
		if   r < a:     seq += 'A'
		elif r < a+c:   seq += 'C'
		elif r < a+c+g: seq += 'G'
		else:           seq += 'T'
	return seq

def anti(seq):
	"""Produces the reverse complement of a sequence"""
	comp = str.maketrans('ACGTRYMKWSBDHV', 'TGCAYRKMWSVHDB')
	anti = seq.translate(comp)[::-1]
	return anti


GCODE = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'AAR' : 'K',	'AAY' : 'N',	'ACA' : 'T',	'ACC' : 'T',
	'ACG' : 'T',	'ACT' : 'T',	'ACR' : 'T',	'ACY' : 'T',
	'ACK' : 'T',	'ACM' : 'T',	'ACW' : 'T',	'ACS' : 'T',
	'ACB' : 'T',	'ACD' : 'T',	'ACH' : 'T',	'ACV' : 'T',
	'ACN' : 'T',	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',
	'AGT' : 'S',	'AGR' : 'R',	'AGY' : 'S',	'ATA' : 'I',
	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',	'ATY' : 'I',
	'ATM' : 'I',	'ATW' : 'I',	'ATH' : 'I',	'CAA' : 'Q',
	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',	'CAR' : 'Q',
	'CAY' : 'H',	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',
	'CCT' : 'P',	'CCR' : 'P',	'CCY' : 'P',	'CCK' : 'P',
	'CCM' : 'P',	'CCW' : 'P',	'CCS' : 'P',	'CCB' : 'P',
	'CCD' : 'P',	'CCH' : 'P',	'CCV' : 'P',	'CCN' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CGR' : 'R',	'CGY' : 'R',	'CGK' : 'R',	'CGM' : 'R',
	'CGW' : 'R',	'CGS' : 'R',	'CGB' : 'R',	'CGD' : 'R',
	'CGH' : 'R',	'CGV' : 'R',	'CGN' : 'R',	'CTA' : 'L',
	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',	'CTR' : 'L',
	'CTY' : 'L',	'CTK' : 'L',	'CTM' : 'L',	'CTW' : 'L',
	'CTS' : 'L',	'CTB' : 'L',	'CTD' : 'L',	'CTH' : 'L',
	'CTV' : 'L',	'CTN' : 'L',	'GAA' : 'E',	'GAC' : 'D',
	'GAG' : 'E',	'GAT' : 'D',	'GAR' : 'E',	'GAY' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GCR' : 'A',	'GCY' : 'A',	'GCK' : 'A',	'GCM' : 'A',
	'GCW' : 'A',	'GCS' : 'A',	'GCB' : 'A',	'GCD' : 'A',
	'GCH' : 'A',	'GCV' : 'A',	'GCN' : 'A',	'GGA' : 'G',
	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',	'GGR' : 'G',
	'GGY' : 'G',	'GGK' : 'G',	'GGM' : 'G',	'GGW' : 'G',
	'GGS' : 'G',	'GGB' : 'G',	'GGD' : 'G',	'GGH' : 'G',
	'GGV' : 'G',	'GGN' : 'G',	'GTA' : 'V',	'GTC' : 'V',
	'GTG' : 'V',	'GTT' : 'V',	'GTR' : 'V',	'GTY' : 'V',
	'GTK' : 'V',	'GTM' : 'V',	'GTW' : 'V',	'GTS' : 'V',
	'GTB' : 'V',	'GTD' : 'V',	'GTH' : 'V',	'GTV' : 'V',
	'GTN' : 'V',	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',
	'TAT' : 'Y',	'TAR' : '*',	'TAY' : 'Y',	'TCA' : 'S',
	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',	'TCR' : 'S',
	'TCY' : 'S',	'TCK' : 'S',	'TCM' : 'S',	'TCW' : 'S',
	'TCS' : 'S',	'TCB' : 'S',	'TCD' : 'S',	'TCH' : 'S',
	'TCV' : 'S',	'TCN' : 'S',	'TGA' : '*',	'TGC' : 'C',
	'TGG' : 'W',	'TGT' : 'C',	'TGY' : 'C',	'TTA' : 'L',
	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',	'TTR' : 'L',
	'TTY' : 'F',	'TRA' : '*',	'YTA' : 'L',	'YTG' : 'L',
	'YTR' : 'L',	'MGA' : 'R',	'MGG' : 'R',	'MGR' : 'R',
}

def translate(seq, frame=0):
	"""Translates a sequence using the standard genetic code"""

	pro = []
	for i in range(frame, len(seq), 3):
		codon = seq[i:i+3]
		if codon in GCODE: pro.append(GCODE[codon])
		else: pro.append('X')
	return ''.join(pro)

## File Readers ##

def getfp(filename):
	"""Returns a file pointer for reading based on file name"""
	if   filename.endswith('.gz'): return gzip.open(filename, 'rt')
	elif filename == '-':          return sys.stdin
	else:                          return open(filename)

def readfasta(filename):
	"""Simple fasta file iterator"""
	name = None
	seqs = []
	fp = getfp(filename)
	while True:
		line = fp.readline()
		if line == '': break
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

def readfastq(filename):
	"""Simple fastq file iterator"""
	fp = getfp(filename)
	while True:
		h = fp.readline()
		if h == '': break
		s = fp.readline()
		p = fp.readline()
		q = fp.readline()
		yield h, s, p, q
	fp.close()

class SAMbitflag:
	"""Class for sam bitflags"""
	def __init__(self, val):
		i = int(val)
		b = f'{i:012b}'
		self.read_unmapped = True if b[-3] == '1' else False
		self.read_reverse_strand = True if b[-5] == '1' else False
		self.not_primary_alignment = True if b[-9] == '1' else False
		self.supplementary_alignment = True if b[-12] == '1' else False
		self.otherflags = []
		for i in (1, 2, 4, 6, 7, 8, 10, 11):
			if b[-i] == '1': self.otherflags.append(i)

def cigar_to_exons(cigar, pos):
	"""Converts cigar strings to exon coorinate tuples"""
	exons = []
	beg = 0
	end = 0
	for match in re.finditer(r'(\d+)([\D])', cigar):
		n = int(match.group(1))
		op = match.group(2)
		if   op == 'M': end += n
		elif op == '=': end += n
		elif op == 'X': end += n
		elif op == 'D': pass
		elif op == 'I': end += n
		elif op == 'S': pass
		elif op == 'H': pass
		elif op == 'N':
			exons.append((pos+beg-1, pos+end-2))
			beg = end + n
			end = beg
	exons.append((pos+beg-1, pos+end-2))
	return exons

def readsam(filename):
	"""Simple sam file iterator, keeps 1-based coords"""
	fp = getfp(filename)
	for line in fp:
		if line == '': break
		if line.startswith('@'): continue
		f = line.split('\t')
		qname = f[0]
		bf = SAMbitflag(f[1])
		if bf.read_unmapped: continue
		chrom = f[2]
		pos   = int(f[3])
		cigar = f[5]
		st = '-' if bf.read_reverse_strand else '+'
		exons = cigar_to_exons(cigar, pos)
		yield {'chrom': chrom, 'qname': qname, 'flags': bf, 'cigar': cigar,
			'exons': exons, 'beg': exons[0][0], 'end': exons[-1][1],
			'strand': st, 'line': line}
	fp.close()

def readgff(filename):
	"""Simple gff file iterator, keeps 1-based coords"""
	fp = getfp(filename)
	for line in fp:
		if line.startswith('#'): continue
		f = line.split('\t')
		yield {'chrom': f[0], 'source': f[1], 'type': f[2],
			'beg': int(f[3]), 'end': int(f[4]), 'line': line}
		# chr, source, type, beg, end, score, strand, phase, attr
	fp.close()


## Data Functions ##

import xml.etree.ElementTree as ET

def descend_tree(node, prev):
	if len(node) == 0: return prev
	objects = []
	for item in node:
		obj = {'tag': item.tag}
		if item.text and re.match(r'\S',  item.text): obj['txt'] = item.text
		if item.attrib: obj['att'] = item.attrib
		contents = descend_tree(item, [])
		if len(contents) > 0: obj['has'] = contents
		objects.append(obj)
	return objects

def read_xml(fp):
	"""Reads an XML file into a Python data structure"""
	tree = ET.parse(fp)
	root = tree.getroot()
	data = {'tag': root.tag}
	if re.search(r'\S', root.text): data['txt'] = root.text
	if root.attrib: data['att'] = root.attrib
	contents = descend_tree(root, [])
	if contents: data['has'] = contents
	return data
