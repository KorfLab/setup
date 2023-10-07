Miscellaneous Stuff
===================

Directory Structure
-------------------

Your PI organizes his files as shown below. You should probably do the same.

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

+ All repos are in the `Code` directory
	+ Personal programs are soft-linked to `Code/bin`
	+ Personal libraries are soft-linked to `Code/lib`
	+ `$PATH` and `$PYTHONPATH` are set appropriately
+ Data is stored "elsewhere"
	+ Data files are backed up
	+ Data files are not writable
	+ Data files are frequently soft-linked to code directories
	+ Data directories have OS-indexing turned off


Login Customization
-------------------

You should modify your login script. See the `profile` for inspiration.


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


Cluster
-------

+ Use `nice` if you're using a lot of resources
+ Use `top` or `htop` to monitor resources
+ Use ^C to kill a job in the foreground
+ Use ^Z to sleep a job in the foreground
+ Use `fg` to start a sleeping job in the foreground
+ Use `bg` to start a sleeping job in the background
+ Use `ps` to show jobs here or `ps -lu <username` to show all your jobs
+ Use `kill -9 <jobid>` to kill a job


Git password persistence
------------------------

To make your GitHub Personal Access Token persist (so you don't have to
copy-paste it again and again).

```
git config --global user.name "username"
git config --global credential.helper store
```


datacore
--------

We have a repo for -omic data processing called datacore. This is a good place
to go for some of your dev data. If you are developing a new dataset that will
be useful to others, put the scripts and a small selection of data in datacore.
Don't fill up datacore or any repo with large datafiles.

https://github.com/KorfLab/datacore



IPC
---

IPC means interprocess communication. In Perl, if you want to capture the
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
The formula requires that `a` is the larger (less negative) of the two operands,
and the operands are swapped in the formula if otherwise.

```
def sumlogp2(a, b, mag=40):
	assert(a <= 0)
	assert(b <= 0)
	if abs(a - b) > mag: return max(a, b)
	if a < b: return math.log2(1 + 2**(a - b)) + b
	return math.log2(1 + 2**(b - a)) + a
```

Of course, if you're working in Python, you can use `numpy.logaddexp2(a, b)` to
do the same calculation. But not every language has this built in. Also, the
numpy version is slightly slower than the pure python.


Some useful scripts
-------------------

The `bin` directory contains a couple of useful scripts (maybe more useful to
modify than to use as is).

+ `memcheck` looks through the `proc` filesystem to examine memory
+ `parallelize` runs a file of command lines in parallel on multiple CPUs
+ `redundancey_check` looks for identical files in the filesystem


Unix Quick Reference
--------------------


| Token   | Function
|:--------|:-------------------------------------|
| .       | your current directory (see pwd)
| ..      | your parent directory
| ~       | your home directory (also $HOME)
| ^C      | send interrupt signal
| ^D      | send end-of-file character
| tab     | tab-complete names
| *       | wildcard - matches everything
| \|      | pipe output from one command to another
| >       | redirect output to file


| Command   | Example       | Intent                        |
|:----------|:--------------|:------------------------------|
| `cat`     | `cat > f`     | create file f and wait for keyboard (see ^D)
|           | `cat f`       | stream contents of file f to STDOUT
|           | `cat a b > c` | concatenate files a and b into c
| `cd`      | `cd d`        | change to relative directory d
|           | `cd ..`       | go up one directory
|           | `cd /d`       | change to absolute directory d
| `chmod`   | `chmod 644 f` | change permissions for file f in octal format
|           | `chmod u+x f` | change permissions for f the hard way
| `cp`      | `cp f1 f2`    | make a copy of file f1 called f2
| `cut`     | `cut -f 2,3`  | cut columns out of a file
| `date`    | `date`        | print the current date
| `df`      | `df -h .`     | display free space on file system
| `du`      | `du -h ~`     | display the sizes of your files
| `git`     | `git add f`   | start tracking file f
|           | `git commit -m "message"` | finished edits, ready to upload
|           | `git push`    | put changes into repository
|           | `git pull`    | retrieve latest documents from repository
|           | `git status`  | check on status of repository
| `grep`    | `grep p f`    | print lines with the letter p in file f
| `gzip`    | `gzip f`      | compress file f
| `gunzip`  | `gunzip f.gz` | uncompress file f.gz
| `head`    | `head f`      | display the first 10 lines of file f
|           | `head -2 f`   | display the first 2 lines of file f
| `history` | `history`     | display the recent commands you typed
| `htop`    | `htop`        | more extensive version of `top`
| `kill`    | `kill 1023`   | kill process with id 1023
| `less`    | `less f`      | page through a file
| `ln`      | `ln -s f1 f2` | make f2 an alias of f1
| `ls`      | `ls`          | list current directory
|           | `ls -F`       | show file types
|           | `ls -Fl`      | list with file details
|           | `ls -Fla`     | also show invisible files
|           | `ls -Flta`    | sort by time instead of name
| `man`     | `man ls`      | read the manual page on `ls` command
| `mkdir`   | `mkdir d`     | make a directory named d
| `more`    | `more f`      | page through file f (see less)
| `mv`      | `mv foo bar`  | rename file foo as bar
|           | `mv foo ..`   | move file foo to parent directory
| `nano`    | `nano`        | use the nano text file editor
| `pwd`     | `pwd`         | print working directory
| `rm`      | `rm f1 f2`    | remove files f1 and f2
|           | `rm -r d`     | remove directory d and all files beneath
|           | `rm -rf /`    | destroy your computer
| `rmdir`   | `rmdir d`     | remove directory d
| `sort`    | `sort f`      | sort file f alphabetically by first column
|           | `sort -n f`   | sort file f numerically by first column
|           | `sort -k 2 f` | sort file f alphabetically by column 2
| `tail`    | `tail f`      | display the last 10 lines of file f
|           | `tail -f f`   | as above and keep displaying if file is open
| `tar`     | `tar -cf ...` | create a compressed tar-ball (-z to compress)
|           | `tar -xf ...` | decompress a tar-ball (-z if compressed)
| `time`    | `time ...`    | determine how much time a process takes
| `top`     | `top`         | display processes running on your system
| `touch`   | `touch f`     | update file f modification time (create if needed)
| `wc`      | `wc f`        | count the lines, words, and characters in file f
| `screen`  | `screen -S ...`   | start a virtual terminal


Please Don't
------------

+ Attach uncompressed genome data to emails
+ Send hires photos of your computer screen when asking for help
+ Copy-paste code from program to program

