Walkthrough
===========

WARNING: document in progress and in a very drafty state!

This is a short tutorial on some sequence-based bioinformatics. It's all CLI
but no programming required.

- Environment Checks
- Sequences
- Compositions
- BLAST
- Clustalw
- Sequencing read alignment

- Motif-finding
- Multiple alignment
- Trees
- RNA-Seq
- ChIP-Seq

- Sequence Models - train and test classic sequence models (and peceptron)
	- training
	- cross-validation
	- pwm
	- nmm
	- wam
	- mlp

## Environment Checks ##

Let's make sure everything is set up correctly. Presumably, you have followed
the directions in `04_Environment.md` and have the following configured:

- Unix/Linux CLI (with development tools installed on Mac)
- Conda installed
- Your directory structure organized
- You have `git clone https://github.com/KorfLab/init`
- You are doing this on more than one computer (Rule #2)
	- Your main computer
	- Hive (or some other remote computer)
	- Maybe a VM in your main computer or a spare computer

### Conda Base Environment

Your shell prompt should show `(base)` at the start. If this is not the case,
try `conda activate`. If that doesn't work, you didn't install mini-forge
(conda) correctly and you need to get help before proceeding.

### Install walkthrough Conda Environment

Install the _walkthrough_ conda environment from `init/etc`.

```
conda env create -f etc/conda-walkthrough.yml
conda activate walkthrough
```

If this fails for some reason, seek help. It must succeed to continue.

### /usr/bin/time

When we write programs or run programs from others, we often want to know how
much computer resources are being used. `top` works for live monitoring, but
doesn't tell you aggregate figures. The shell keyword `time` tells you how much
CPU your process used, but not how much memory. To get this information, you
must use `/usr/bin/time`, which may not be installed on your system by default
(but you just installed it via conda). The syntax on Mac and Linux is slightly
different. The examples below show `/usr/bin/time` being used to monitor the
`ls` command.

```
/usr/bin/time -lp ls  # mac
/usr/bin/time -v ls   # linux
```

### benchmarks

Change directory to the `init` repo and try running the `benchmark` program in
`init/bin`.

```
cd init
bin/benchmark
```

If this command doesn't work, your enviornment is not set up correctly. Ask for
help if you can't solve it yourself.

- `PYTHONPATH` needs to be set
- `korflab.py` (or its alias) is where `PYTHONPATH` is looking

Assuming the `benchmark` worked, it reports a value that describes how fast
your computer runs Python. The value depends on several things:

- What else is running on your computer
- The version of Python you have (default vs. conda)
- The operating system
- If you computer is running on battery vs. plugged in (laptop)
- If you are working inside a VM

It's not a very good benchmark! Here are some typical values.

- 350 top of the line CPU circa 2025
- 200-300 Apple Silicon circa 2025
- 150-250 typical PC circa 2025
- 100 pre-2020 computer
- 50 Chromebook

## Sequences ##

This walkthrough shows you how to do various bioinformatics tasks with
sequences, so we had better find some sequences to play with. Conveniently, you
can find some in the `init/data` directory.

```
cd data
```

### zless

A good way to examine sequence file is with `zless`. Why `zless` instead of
regular `less`? Because most sequence files are stored compressed. Don't
uncompress FASTA files unless you have a really good reason (e.g. there's a
program you need to run that requires an uncompressed file because it uses
`seek()` for random access).

Never open up a sequence file in your editor unless you plan to edit it. You
would have to have a very good reason to edit a sequence file. Most data files
should have read-only permissions to prevent accidental editing. Also, they
should be compressed, so your editor wouldn't be the right choice for that
anyway. To ensure that everything in the `data` directory has read-only
permission, do the following:

```
chmod 444 *.gz
```

Now examine some of the sequence files.

```
zless ce1pct.fa.gz
zless GCF_000005845.2_ASM584v2_protein.faa.gz
```

In `zless`, the space bar and the `f` key advance foward a page at a time. The
`b` key goes backwards. If you want to search for something, use the `/` key.
The `?` key does a reverse search.

### seq-stats

Sequence files can be huge and browsing them with `zless` might not be very
efficient. So let's use a program to give us a summary of what's in a FASTA
file. From the `init` repo, run the `bin/seq-stats` program on some of the
FASTA files in the data directory.

```
../bin/seq-stats at1pct.fa.gz
../bin/seq-stats ce1pct.fa.gz
../bin/seq-stats dm1pct.fa.gz
../bin/seq-stats GCF_000005845.2_ASM584v2_protein.faa.gz
```

You should have noticed that the `at1pct.fa.gz` file has some nucleotide
ambiguity symbols. Also, the `GCF_000005845...` file is protein. If you examine
the nucleotide frequencies of the genome files, you will find that Arabidopsis
(at...) is similar to Caenorhabditis (ce...). They are relatively both AT-rich.

### kmer-gizmo

Even when sequences have the similar compositions, it doesn't mean they are
"speaking the same language". For example, English and French have very similar
letter frequencies. And yet the words are very different. This is also true in
DNA. For example, gene prediction algorithms rely on differences between exons
and introns. We can start to explore these differences by examining kmer
frequencies.

Try `kmer-gizmo` on the 1 percent genomes with a kmer size of 2. Using the
`--acgt` option ensures that all kmers use canonical letters only.

```
../bin/kmer-gizmo at1pct.fa.gz 2
../bin/kmer-gizmo at1pct.fa.gz 2 --acgt
../bin/kmer-gizmo ce1pct.fa.gz 2
../bin/kmer-gizmo dm1pct.fa.gz 2
```

While Arabidopsis and Caenorhabditis may look similar at the single nucleotide
level, they become increasingly different with higher values of k. For some
reason, Caenorhabditis likes poly-A (or poly-T) sequences more than
Arabidopsis.

```
../bin/kmer-gizmo at1pct.fa.gz 2 --acgt --compare ce1pct.fa.gz
../bin/kmer-gizmo at1pct.fa.gz 3 --acgt --compare ce1pct.fa.gz | less
../bin/kmer-gizmo at1pct.fa.gz 4 --acgt --compare ce1pct.fa.gz | less
```

## build ##

Create a `build` directory for your work. `git` ignores directories and files
with specific names, and `build` is one of those. We'll do all of our work in
the `build` directory so we don't pollute the repo with extra files.

```
mkdir build
```

## BLAST ##

### makeblastdb

To make a blast database, use the `makeblastdb` command. The program doesn't
read compressed files, so you have to `gunzip -c` the FASTA file and then tell
`makeblastdb` that the data is coming from stdin. This is what the `-` means.
When using stdin, you also have to give the database a title and an output
file name.

```
/usr/bin/time -v gunzip -c GCF_000005845.2_ASM584v2_protein.faa.gz\
	| makeblastdb -in - -dbtype prot -out build/ecoli\
	-title ecoli -parse_seqids
```

You could also do this another way:

1. Uncompress the FASTA file into a new FAST file called `ecoli`
2. Run `makeblastdb` on the FASTA file
3. Remove the uncompressed file

### blastdbcmd

A BLAST database is more organized than a FASTA file. You can therefore
retrieve specific sequences by name (this was what the `-parse_seqids` option
allowed). Try the following command:

```
blastdbcmd -db build/ecoli -entry NP_414608.1
``

Now save it to a file:

```
/usr/bin/time -v  blastdbcmd -db build/ecoli -entry NP_414608.1\
	> build/NP_414608.1.fa
```

### blastp

Let's search the `NP_414608.1.fa` file against the `ecoli` database with
`blastp`.

```
/usr/bin/time -v  blastp -db build/ecoli -query build/NP_414608.1.fa\
	> build/blast.out
```

Use `less` to examine the output file. You'll see that the protein matches
several other "ABC transporters" in E. coli. It must be a large-ish gene
family. If you look at the end of the report (shift-G) you will see that some
of the alignments at the end aren't very long or high scoring. They also have
high E-values (expected by chance). Let's run `blastp` again and set the
E-value lower (1e-5) so that we only see good matches.

```
/usr/bin/time -v  blastp -db build/ecoli -query build/NP_414608.1.fa\
	-evalue 1e-5 > build/blast.out
```

Now let's get all of those sequence identifiers using `blastdbcmd`.

```
/usr/bin/time -v  grep "^>" build/blast.out | cut -f 1 -d " " |\
	cut -f2 -d ">" > build/abc.txt
```

Examine `pids` with less and then run `blastcmd` to get all the sequences.

```
blastdbcmd -db ecoli -entry_batch abc.txt > abc.fa
```

## Clustalw ##

Now that we have a bunch of related sequences, let's make a multiple alignment
with `clustalw`.

```
clustalw -infile=abc.fa -outfile=abc.aln
```

Examine the file with `less`.



-----------------------------------------------------------------------------


## Sequence Models ##

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
