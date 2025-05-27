The KorfLab Classics
====================

Aspiring bioinformatics programmers often ask me how they can improve their
skills. Like many other disciplines, a good place to start is by studying the
classics. Since bioinformatics is generally performed in a command line
Unix/Linux environment, you should have some familiarity with the CLI before
you begin. You also need to be a competent programmer. A good place to start is
MCB185. These things should be familiar to you.

- Importing and creating function libraries
- Unix-standard CLI libraries in your favorite language
- File I/O for normal and compressed files
- Building and navigating arbitrarily complex list-dict data structures
- JSON and YAML

Historically, most bioinformatics software was written in C or Perl. Today,
Python is a popular choice. Although less common, you may see some software
written in C++, Go, Java, Julia, Rust, etc. The language you use it up to you.
Good programmers know multiple languages.

- All programs should have a proper CLI (e.g. argparse in Python)
- Programs should not have hard-coded paths or values
- Programs should generally write to stdout
- Minimize external dependancies
- Follow the style guide for your language

## Contents ##

The programs should be completed in order as some depend on others.

- `randomseq` - generate random DNA and protein sequences
- `readfasta` - function to read FASTA files
- `seqstats` - provide statistics on FASTA files
- `skewer` - compute GC-skew and GC-composition in windows
- `dust` - mask low-complexity sequences
- `repeatblaster` - make a repeat masker using BLAST
- `translate` - translate DNA to protein
- `featureseq` - extract sequences from FASTA + GFF
- `introns` - extract introns from FASTA + GFF
- `imeter` - reimplement the IMEter
- `ga` - write a genetic algorithm to find optimal introns
- `pwm` - create and evaulate a position weight matrix
- `consensus` - make a consensus sequence with the IUPAC alphabet
- `mlp` - make a multi-layer perceptron
- `mm` - create and evaluate an nth order Markov model
- `blosum` - read a scoring matrix and compute its lambda
- `nw` - global alignment
- `sw` - local alignment
- `viterbi` - make an HMM and decode it
- `fb` - forward-backward decoding
- `csw` - local alignemnt in C
- `cvector` - make an infinitely growing array in C
- `cdictionary` - make a dictionary in C
- `ckmers` - make a kmer counter in C

## randomseq ##

Write a program that outputs random sequences. The user must specify the number
and length of sequences, and their type: nucleotide or amino acid.

For nucleotides, the default should be 25% each letter, but there should be an
option to specify the individual frequencies. The output format should be FASTA
by default but FASTQ optionally (with a way for the user to set the quality
values).

For amino acids, the default frequencies should be some well-known proteome,
such as E. coli, and there should be a way for the user to specify some other
frequencies (e.g. flat 5%). The output should be FASTA.

The FASTA identifier should be unique for each sequence, and there should be
some user-definable string on each identifier. Line lengths should be 80 by
default but this can be overridden with an option.

The programming here is very easy. The point of this exercise is to write a
simple yet thorough CLI.

## readfasta ##

Make a library that includes a function to read FASTA files. Use it for all of
your programs.

Reading FASTA files isn't particularly hard, but it can be done poorly. You
should not read the entire file into memory as some FASTA files can be huge.
Instead, you should read only one record at a time.

Many FASTA files are stored compressed, so being able to read a compressed file
is required, as is the ability to read from stdin.

You can find a number of examples of FASTA parsers in `KorfLab/bin/fasta` but
you must write your own from scratch.

## seqstats ##

Write a program that reports various statistics about a FASTA file.

- Total number of sequences and letters
- Min, max, mean, median, and N50 of sequence lengths
- Frequencies of each letter
- An option to report codon usage (assuming the sequences are all coding)

## skewer ##

Write a program the computes windowed GC-skew (G+C/G-C) and GC composition
along a genome sequence. The program should input FASTA and output BED. The
program should have a variable window size with some default value (e.g. 100).
Ideally, the window is computed efficiently (not recomputed in each window).

## dust ##

Write a low-complexity filter for nucleotide sequences. The output should be a
FASTA file. By default, low-complexity regions should be masked with Ns but you
should provide a command line switch for lowercase masking (often called
soft-masking). Again, don't recompute each window. Also provide an option to
output the low-complexity regions as GFF.

## repeatblaster ##

Write a repeat masking program using BLAST. The program takes as input a FASTA
file of the sequence to be masked as well as a library of known repetitive
elements. Each repetitive element should have its own specific thresholds (e.g.
length, percent identity, score).

## translate ##

Write a program that translates sequences. In `rna` mode, it finds the longest
protein in each sequence and reports this as the encoded protein. In `dna` mode
it finds all open reading frames longer than a threshold value (e.g. for use in
prokaryotes). In `rna` mode, the program should default to translating the top
strand, but there should be an option also including the bottom strand. In
`dna` mode, the program should find long open reading frames on both strands.

## featureseq ##

Write a program that reads a FASTA file and GFF file, and reports specific
features of the GFF in FASTA format. For example, if a user wants `exon`
features, then the program reports the sequences of all exons in FASTA format.
There should be an option `--plus` to convert all sequences to the plus strand.
There should also be an option for extracting `--extra` sequence on either side
of the feature.

## introns ##

Most GFF files do not include the position of introns as they can be inferred
from the exon coordinates. Add an option to extract introns to your
`featureseq` program above. If there are alternative isoforms, some introns may
be reported twice. Include an option to report only unique introns.

## imeter ##

Reproduce the original IMEter experiments.

- Split introns into proximal and distal groups
- Create tables of kmers for proximal and distal introns
- Create an IMEter program that scores sequences
- Validate against `data/db_IME_Rose_WT_introns.fa.gz`

## ga ##

Write a genetic algorithm to find introns with the highest possible scores.
Note that these may end up very GC-rich and no longer look like introns. So you
will have to simultaneously maximize IMEter score and intron composition.

## pwm ##

Make a PWM for splice sites and evaluate their performance with
cross-validation.

Donor

```
   A     C     G     T
1 0.000 0.000 1.000 0.000
2 0.000 0.000 0.000 1.000
3 0.657 0.049 0.123 0.171
4 0.534 0.139 0.058 0.269
5 0.207 0.095 0.494 0.204
```

Acceptor

```
   A     C     G     T
1 0.195 0.139 0.148 0.517
2 0.166 0.112 0.105 0.617
3 0.261 0.088 0.375 0.276
4 0.073 0.634 0.008 0.285
5 1.000 0.000 0.000 0.000
6 0.000 0.000 1.000 0.000
```

## consensus ##

Given a bunch of related nucleotide sequences (e.g. splice donor sites), create
a consensus sequence using the IUPAC letters.

## mlp ##

Make a multi-layer perceptron to recognize splice sites. Compare the
performance to PWM.

## mm ##

Make an nth order Markov model of exon and intron sequences and evaluate their
performance with cross-validation.

## blosum ##

Read a BLOSUM scoring matrix into a 2D structure. Compute lambda. Also compute
the average percent identity and percent similarity. The matrices are in the
`data` directory.

| Matrix   | Lambda | H      | Ident | Simil |
|----------|--------|--------|-------|-------|
| BLOSUM45 | 0.2248 | 0.2357 | 23.85 | 41.88 |
| BLOSUM62 | 0.3174 | 0.3905 | 30.08 | 48.80 |
| BLOSUM80 | 0.2268 | 0.6219 | 39.51 | 57.93 |

## nw ##

Write the classic Needleman-Wunsch algorithm for global alignment. There should
be options for nucleotide match-mismatch scoring or protein scoring matrices
depending on the sequence type (e.g. BLOSUM62).

## sw ##

Write the classic Smith-Waterman algorithm for local alignment. This is a minor
variant of Needlman-Wunsch.

## viterbi ##

Make an HMM and write a Viterbi decoder.

## fb ##

Make a forward-backward decoder for your HMM.

## cfasta ##

Write a function that reads FASTA files in C. If you have never programmed in C
before, this is a good place to start. Your code must not have memory leaks.
After this exercise, you will appreciate how convenient and how offensive the
following code is in python.

```python
for line in fp:
	seq += line.rstrip()
```

## csw ##

Write Smith-Waterman in C. The alignment must be in a function that you can
call over and over, and the program must not have memory leaks.

## cvector ##

Make a text vector in C (array of strings that grows dynamically as needed).
This will help you apprecaite the convenience of things like python lists.

## cdictionary ##

Make a dictionary in C. Use the text vector for the keys and an int for values.
This will help you appreciate the trade-offs of hashing algorithms (which isn't
something you get a chance to appreciate in python, for example). Use the
dictionary to count kmers in a fasta file.
