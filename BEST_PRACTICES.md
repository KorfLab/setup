Rules
=====

Rule #1: Create Test/Dev Data
-----------------------------

Before you start on a project, the most important thing to do is to build a
minimal dataset for development and testing. We call this our "test set" or
"dev set". We do this for several reasons.

+ Minimize debugging time
+ Functional tests
+ Tutorials

Software development takes much more time than you expect. The debugging stage
can be very long. In order to reduce the downtime between debugging sessions,
we need a small data set that can be processed very quickly.

Software changes over time. Even if we make no changes to our code, our
software depends on other software, which may change silently. In order to
ensure that our software continues to produce the same output as before, we
must perform "functional tests" that automatically compare the current output
to the previous, expected output.

When it comes time to distribute our software, there should be a tutorial that
shows how to use the software. The test data is useful here and also to ensure
that the software passes the functional tests at another location.

Making test data can take some time. For example, let's imagine your project
involves RNA-seq on the human genome. What is the proper test set? Not the
entire human genome and 10 RNA-seq libraries. The test set should fit neatly
into the github repository where the code lives. Ideally, the entire repo is
small. Under 100M is good. Under 10M is better. 1M is ideal. Creating a test
set for an RNA-seq project means making a miniaturized version of the human
genome and curating some reads that align to that part of the genome.
Obviously, the region of the genome matters. You probably want some areas with
high coverage and some areas with low coverage. It may take a week to create a
test set. And later, you may have to make a better one. This part of our work
is sort of like making reagents and calibrating instruments. It's a pain but
must be done to ensure reproducibility.


Rule #2: All Code in GitHub
---------------------------

All of the code you write should be managed in a GitHub repository. Generally,
there is no need to make it private.

Code should be documented in Markdown format. Make your Markdown files look
like final versions of documents and not just pre-processor code for HTML.

You should have a small sample of data with your programs for testing purposes.


Rule #3: Employ Standard Directory Structure
--------------------------------------------

Your directory structure should look something like this:

```
Code/
	bin/
		program@ -> ../something/program
	lib/
		library.py@ -> ../something/library.py
	datacore/
	setup/
	something/
		program*
		library.py
		favorite.fa@ -> ../../Data/favorite.fa
		favorite.gff@ -> ../../Data/favorite.gff
Data/
	favorite.fa
	favorite.gff
Desktop/
Documents/
Downloads/
OtherDirectories/
```

+ All of your source files belong in some directory, e.g. `Code`
	+ Programs you use frequently should be soft-linked to `Code/bin`
	+ Libraries you use frequently should be soft-linked to `Code/lib`
	+ Your `$PATH` and `$PYTHONPATH` should be set appropriately
+ Data should be stored somewhere
	+ You may want to soft-link files to project directories
	+ You should probably turn off OS-indexing in your data directory


Best Practices
==============

Prioritize Beauty
-----------------

A programming project has many facets.

+ Beautiful - it is visually appealing
+ Clear - it is easy to explain to others
+ Clever - it is intellectually appealing
+ Correct - it solves the problem as intended
+ Documented - it has documents for users and/or developers
+ Efficient - it doesn't use much memory
+ Extensible - it can be used for other projects
+ Fast - it doesn't take long to run
+ Friendly - it is bundled with a tutorial
+ Novel - it is the first of its kind
+ Robust - it has unit and/or functional tests
+ Simple - it is easy to understand

Biologists focus on their program being correct. They have a specific problem
to solve and want a solution to that problem. Being so focused on their problem
they tend to lose sight of the bigger picture that involves other users and
other developers.

Computer scientists focus their efforts on being clever, efficient, and novel.
Their goal is to prove how smart they are. They might not care about users or
other developers.

Scientific programming exists in an environment with transient users and
developers. Code must be developed in such a way that new users and new
developers can deploy and extend the project. Because of this, the code and
documentation must be simple and clear. Prioritize beauty. Beautiful code and
beautiful documents are clear and simple, and can easily be made correct,
friendly, and robust.


Managing Data
-------------

We have a repo for -omic data processing called datacore. If you are developing
a new dataset that will be useful to others, put the scripts and a small
selection of data in datacore. Don't fill up datacore or any repo with large
datafiles.

https://github.com/KorfLab/datacore

Data is generally kept in a completely separate place from code. If you have
scripts in the same directory with data, you're doing it wrong. Code belongs in
your github repos. On the cluster, we put data in `/share/korflab/projects`.
See the spitfire repo for more information.

In the same way that you have a `README.md` in every repo, you should also put
a `README.md` in every project directory that describes the intent and
contents.

------------------------------------------------------------------------------

Suppose I've written a new genome analysis program called `smash` that looks
something like this:

```
#!/usr/bin/env python3
import argparse
import grimoire
# the rest of the code...
```

Suppose I want to run `smash` on some genomes. I'm no longer doing code
development, but analysis. Therefore, my actions don't really belong in the
`Code` directory. So I make a new directory for the project off the home
directory.

```
(base) ian@virtualbox: mkdir ~/Smashing
(base) ian@virtualbox: cd ~/Smashing
(base) ian@virtualbox: smash ~/Data/genomes/hg19.fa > smash.out
```

In order to get all of this to work, `smash` must be in my executable path.
Since `smash` depends on `grimoire`, it follows that `grimoire` must be in my
library path. If you followed the KorfLab/setup, you already have `Code/bin` in
your `PATH` and `Code/lib` in your `PYTHONPATH`. You can alias files to those
directories to make them visible to the shell and Python.

Your directory layout should look like this:

```
anaconda3/
Code/
	bin/
		smash@ -> ../smashrepo/smash
	lib/
		grimoire@ -> ../grimoire/grimoire
	grimoire/
	setup/
	smashrepo/
		smash*
Data/
	genomes/
		hg19.fa
Desktop/
Documents/
Downloads/
Smashing/
	smash.out
```

Managing data is different from code. Data can be large and expensive to
generate. It should backed up or mirrored somewhere, and it should have
read-only permissions to prevent it from being changed.

If you're doing development and working with VMs, don't copy data to each VM.
Create a read-only shared folder. In the listing above, it may look like `Data`
is in the directory, but it is not. It's just the mount point for a shared
folder.


Programs vs. Pipelines vs. Notebooks
------------------------------------

There are 3 overlapping computer activities we tend to do.

1. Software development in Python, C, Go, etc
2. Running pipelines in Snakemake
3. Exploring data in R-Studio or Jupyter notebooks

### Software Development

You should already know Python before moving on to other languages. Our overall
philosophy is that code should be simple and beautiful. Please see the
algorithms repo https://github.com/KorfLab/algorithms.

### Running Pipelines

When analyzing large datasets, there are generally 3 tasks: installing
software, developing a pipeline, deploying a pipeline. Always install software
with Conda. Don't rely on the local environment. Pipelines are developed in
Snakemake on a test set in you VM, not the cluster. Once you are ready to
deploy a pipeline, then you can run on the cluster.

Pipelines are developed using Conda and Snakemake. Develop your Snakemake
pipelines on a small test set in a VM, and not on the cluster. These practices
ensure maximum portability and reproducible data practices.

1. Conda - https://github.com/KorfLab/learning-conda
2. Snakemake - https://github.com/KorfLab/learning-snakemake
3. Cluster - https://github.com/KorfLab/spitfire

### Notebook Computing

We're not talking about laptops but rather R-Studio or Jupyter. These tools are
great for exploring data, but are not a great way of distributing software. Use
them where they are useful.



Tricks
======

A collection of random tricks and tips to help you.

+ Getting `git` to remember your password
+ Inter-process communication in Python and Perl
+ Summing probabilities in log-space


Git password persistence
------------------------

To make your GitHub Personal Access Token persist (so you don't have to
copy-paste it again and again).

```
git config --global user.name "username"
git config --global credential.helper store
```


IPC
---

That stands for interprocess communication. In Perl, if you want to capture the
output of a command and store it in a variable, you simply use backticks. This
works with scalars to store the entire file or with arrays to store
line-by-line.

```
my $thing = `ls -a`
my @stuff = `ls -a`
```

It's a bit more complex to do this in Python.

```
from subprocess import run
stuff = run('ls -a', shell=True, capture_output=True).stdout.decode().split('\n')
```


Summing probabilities in log-space
----------------------------------

Since multiplying probabilities over and over can lead to underflow errors, we 
tend to do math in log-space. Summing log-probabilities can be probematic 
because you can't simply de-log the numbers, sum them, and then return the log. 
Here's one solution, which is to transform the log to a higher power, then do 
the math, then transform back to a lower power. The function below also 
short-circuits and returns the higher number if the numbers are too dissimilar.
The formula requires that a is the larger (less negative) of the two operands,
and the operands are swapped in the formula if otherwise.

```
def sumlogp2(a, b, mag=40):
	assert(a <= 0)
	assert(b <= 0)
	if abs(a - b) > mag: return max(a, b)
	if a < b: return math.log(1 + 2**(a - b)) + b
	return math.log2(1 + 2**(b - a)) + a
```

Of course, if you're working in Python, you can use `numpy.logaddexp2(a, b)` to 
do the same calculation. But not every language has this built in. Also, the 
numpy version is slightly slower than the pure python.
