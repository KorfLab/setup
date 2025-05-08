"""
Miscellaneous functions for common bioinformatics tasks.
"""

import gzip
import itertools
import json
import math
import random
import re
import sys

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
    if   filename.endswith('.gz'):
        return gzip.open(filename, 'rt', encoding='ISO-8859-1')
    elif filename == '-':
        return sys.stdin
    else:
        return open(filename)

def readfasta(filename):
	"""Simple fasta file iterator: yields defline, seq"""
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
	"""Simple fastq file iterator: yields 4 lines, removing @, +"""
	fp = getfp(filename)
	while True:
		h = fp.readline()
		if h == '': break
		if not h.startswith('@'): sys.exit('fastq format error')
		s = fp.readline()
		p = fp.readline()
		q = fp.readline()
		yield h[1:-1], s[:-1], p[1:-1], q[:-1]
	fp.close()

class SAM:
	"""Simple class for SAM records, 1-based coordinates, read-only"""
	def __init__(self, line):
		f = line.split('\t')

		# standard sam properties
		self.qname = f[0]
		self.flag = int(f[1])
		self.rname = f[2]
		self.pos = int(f[3])
		self.mapq = int(f[4])
		self.cigar = f[5]
		self.rnext = f[6]
		self.pnext = f[7]
		self.tlen = f[8]
		self.seq = f[9]
		self.qual = f[10]

		# flag properties
		self.multimap = self.flag & 1
		self.proper = self.flag & 2
		self.unmapped = self.flag & 4
		self.unmapped2 = self.flag & 8
		self.revcomp = self.flag & 16
		self.revcomp2 = self.flag & 32
		self.first = self.flag & 64
		self.last = self.flag & 128
		self.secondary = self.flag & 256
		self.filtered = self.flag & 512
		self.duplicate = self.flag & 1024
		self.supplementary = self.flag & 2048

		# aliases
		self.line = line[:-1]
		self.chrom = self.rname
		self.beg = self.pos
		self.end = self.beg
		for length, op in re.findall(r'(\d+)([MIDNSHP=X])', self.cigar):
			if op in "MDN=X": self.end += int(length)

	def __str__(self): return self.line # this is why read-only

def readsam(filename):
	"""Simple SAM file iterator, yields GFF objects"""
	fp = getfp(filename)
	for line in fp:
		if line.startswith('@'): continue
		yield SAM(line)
	fp.close()

class GFF:
	"""Simple class for GFF records, 1-based coordinates, read-only"""
	def __init__(self, line):
		f = line.split('\t')
		self.line = line[:-1]
		self.chrom = f[0]
		self.source = f[1]
		self.type = f[2]
		self.beg = int(f[3])
		self.end = int(f[4])
		self.score = None if f[5] == '.' else float(f[5])
		self.strand = f[6]
		self.phase = None if f[7] == '.' else int(f[7])
		self.attr = f[8]

	def __str__(self): return self.line # this is why read-only

def readgff(filename):
	"""Simple GFF file iterator, yields GFF objects"""
	fp = getfp(filename)
	for line in fp:
		if line.startswith('#'): continue
		yield GFF(line)
	fp.close()

def readblosum(filename):
	"""Reads blosum scoring matrix into 2D dictionary"""
	alphabet = []
	matrix = {}
	with open(filename) as fp:
		for line in fp:
			if line.startswith('#'): continue
			if line.startswith(' '):
				f = line.split()
				for c in f: alphabet.append(c)
			elif line:
				f = line.split()
				c1 = f[0]
				if c1 not in matrix: matrix[c1] = {}
				for c2, v in zip(alphabet, f[1:]):
					matrix[c1][c2] = int(v)
	return matrix


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
