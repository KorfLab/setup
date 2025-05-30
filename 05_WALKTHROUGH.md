Walkthrough
===========

This is a very drafty, short tutorial on sequence-based bioinformatics.

## Environment Check ##

Change directory to the `init` repo and try running the `benchmark` program in
`init/bin`.

```
cd init # might be ~/Code/init or ~init
bin/benchmark
```

If this command doesn't work, your enviornment is not set up correctly. Ask for
help if you can't solve it yourself.

- `PYTHONPATH` needs to be set to the location of `~/lib` or `~/Code/lib`
- `korflab.py` (or its alias) is where `PYTHONPATH` is looking

## seq-stats ##

From the `init` repo, run the `bin/seq-stats` program on some of the FASTA
files in the data directory.

```
bin/seq-stats data/at1pct.fa.gz
bin/seq-stats data/ce1pct.fa.gz
bin/seq-stats data/dm1pct.fa.gz
bin/seq-stats data/GCF_000005845.2_ASM584v2_protein.faa.gz
```

You should have noticed that the `at1pct.fa.gz` file has some nucleotide
ambiguity symbols. Also, the `GCF_000005845...` file is protein. Comparing the
nucleotide frequencies of the genome files, Arabidopsis (at...) is similar to
Caenorhabditis (ce...).

## kmer-tool ##

Try `kmer-tool` on the 1 percent genomes with a kmer size of 2. Using the
`--acgt` option ensures that all kmers use canonical letters only.

```
bin/kmer-tool data/at1pct.fa.gz 2
bin/kmer-tool data/ce1pct.fa.gz 2
bin/kmer-tool data/dm1pct.fa.gz 2 --acgt
```

While Arabidopsis may look similar at the single nucleotide level, they become
increasingly different with higher values of k. For some reason, Caenorhabditis
likes poly-A/T sequences more than Arabidopsis.

```
bin/kmer-tool data/at1pct.fa.gz 2 --acgt --compare data/ce1pct.fa.gz
bin/kmer-tool data/at1pct.fa.gz 3 --acgt --compare data/ce1pct.fa.gz | less
bin/kmer-tool data/at1pct.fa.gz 4 --acgt --compare data/ce1pct.fa.gz | less
```

## data-faker & model-tester ##

The next demo involves 2 separate tasks.

1. Create fake training data
2. Train and test various sequence models

### Part 1: data-faker

Running `data-faker` generates a bunch of sequences for training. You must
specify a directory for the files. `build` is a fine name because it will
generally be skipped by `git` if you have a `.gitignore` in your repo (the
`init` repo has this).

```
bin/data-faker build
zless build/acceptors.fa.gz
zless build/genes.fa.gz
```

This creates a bunch of files. Take a look at them. The overall scheme is as
follows:

- 50 nt exon1 
- 5 nt donor site GTAAG-ish
- 50 nt intron
- 5 nt acceptor site TTCAG-ish
- 50 nt exon2

In addition to FASTA files of each isolated component, you will also find files
that merge exons and introns.

- `exon-intron.fa.gz` 20 nt exon1 + donor + 20 nt intron
- `intron-exon.fa.gz` 20 nt intron + acceptor 20 nt exon2
- `genes.fa.gz` exon1 + don + intron + acc + exon2

Each file also has a negative file whose name has a pre-pended `neg`. In order
to make enough files for testing, you need `data-faker` to generate more
sequences. Given that most genomes have 20K genes and each gene may have
several exons, a dataset size of 10k sequences is realistic if one imagines
some filtering procedures.

```
bin/data-faker build --count 10000
```

### Part 2: model-tester

Given 45 nt of sequence, can 
