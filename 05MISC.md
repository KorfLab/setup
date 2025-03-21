Miscellaneous Stuff
===================

+ Files & Backup
+ Directory Structure
+ CPUs, Cores, and Threads
+ Unix Quick Reference
+ Servers
+ Good Practices
+ Programs vs. Pipelines vs. Notebooks


Files & Backup
--------------

A combination of "kids these days" and abstract storage models mean that many
people today have no idea where or how their files are managed.

+ Local
+ Portable
+ Online
+ Auto-sync
+ Manual-sync
+ Backed up
+ Photos

### Local

Files that you download on a desktop, laptop, tablet, or phone are physically
located on your device. They might be in your Downloads directory, but maybe
not.

Files you create and save locally are at risk if your computer breaks down or
is stolen. Never create important files locally unless they are also being
sycnrhonized to the cloud.

### Portable

USB sticks and external drives are for convenience, backup, or temporary
builds. Everything on removable storage should pre-exist elsewhere. If your
only copy of something is on portable media, you might as well throw it away
now and avoid the pain of when you lose it later.

### Online

Some files are **only** available online: you can't get to them unless your
computer is connected to a network. By default, Google Docs files are only
available when you're connected to the Internet. Files such as these are
generally automatically backed up and archived. Even if you accidentally delete
the files, you can usually get them back.

Online files are great for you personal documents, but not for code or data.
Meaning, you _should_ write papers in Google Docs, but it's not the place to
store the human genome.

### Auto-sync

Some files exist **both** locally and in the cloud. If you use Box, Dropbox,
Google Drive, Mega, and other similar services, your files are periodically
synchronized with the cloud. You can work on your files offline, and when you
return to the network, they will sync. When there are multiple computers
working offline, the synchronization may result in lost data.

### Manual-sync

We use GitHub for all of our source code. This is synchronized manually when
you `git pull` and `git push`. When there are conflicts among various repos,
you have to resolve them manually. This is much better than lost or overwritten
data.

### Backed Up

Back up data, not code or documents. Documents should by synchronized with the
cloud. That's your backup. Data is often too large for cloud services. Back up
large data with some kind of backup service.

### Photos

Photos can take up an enormous amount of space. If you take a lot of pictures,
get some kind of photo storage service, possibly independent of your code and
documents.


Directory Structure
-------------------

Your PI organizes his files as shown below. You should probably do something
similar.

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
	+ Your PI stores data on an external SSD
+ Desktop
	+ Do whatever you like here, but my advice would be not to be messy
	+ Don't store code or data on your Desktop
+ Downloads
	+ This is for **temporary** files
	+ If what you downloaded was important, move it from here!


CPUs, Cores, and Threads
------------------------

A _CPU_ is a physical unit that does work on your computer. It's sort of like
an _engine_ in a plane. In the old days, planes had a single engine. Later,
more engines were added to improve performance. Similarly, a computer with
multiple CPUs can perform more work than one with a single CPU.

Most CPUs have multiple _cores_. Cores are like the _cylinders_ in internal
combustion engines. Most car engines have 4 cylinders, but there might be as
few as 1 or as many as 16. Similarly, CPUs have varying numbers of cores. Older
CPUs typically have 1 core, but modern CPUs may have 128.

The overall performance of a computer depends on the total number of cores and
how fast each core is. A computer with 4 CPUs, each with a single core may be
very similar to a computer with a single CPU and 4 cores. Also, they could be
very different. To determine the overall performance of a computer, you must
benchmark it using various standardized tasks.

### Multi-processing and Multi-threading

There are three very different kinds of computer tasks:

1. single-process - solo worker
2. multi-process - team of workers
3. multi-threaded - workers in a hive mind

A single-process task only uses one core at a time. Most of the programs you
write in Python are single-process tasks. It doesn't matter if you have 2 cores
or 256, your program runs only as fast as a single core. If your computer is
doing other things at the same time as running your program, like checking
email, downloading data, etc. your program could slow down. Having extra cores
allows your program to monopolize a single core and run at full speed.

A multi-process task teams up multiple cores to solve a single problem. For
example, if we went grocery shopping together, we could get it done faster if
we agreed that you get the milk and cheese, and I get the bread. Note that
while we are in separate parts of the store, we might pass a few text messages
to each other to add new items to the list or update each other on our
progress. Some multi-process jobs pass messages, while others just make an
initial agreement.

A multi-threaded task is like a multi-process task except that the people doing
the grocery shopping share a hive mind. Communication is nearly instanteous and
everyone has access to each others' shared memories and experiences.

### Processes vs. Threads

It's a little confusing that the word _processor_ and _process_ mean very
different things. Processor used to mean CPU, but it now usually means core. A
process is a program that is currently running (taking up memory and using CPU
cycles to do work).

Every process on your computer has a unique process id (PID). You can see this
in the first column when you run `top`. Every process starts out as a single
thread, meaning it interacts with a single core. A process can use multiple
cores by creating additional worker threads. Each worker is part of a hive mind
with a connection back to the original thread.

A process can also create child processes, which is known as forking. The
parent and children each have their own memory, and must communicate with each
other by passing messages. Many bioinformatics tasks involve a single parent
that spawns multiple children who never communicate to each other. The
technical term for this is "embarrassingly parallel".

There are times when workers end up arguing over the same resource. For
example, two children might fight over access to a single network connection.
Two workers in a hive mind have the exact same problem. When this happens, they
must somehow agree to who goes first and how long you can monopolize the
resource. A worker that is waiting for access to a resource is _blocked_. A
computer with 256 cores may be doing nothing if all of the cores are waiting
for the network to unblock.

### Python Notes

Python isn't truly a multi-threaded language. While it does have the concept of
threads (shared memory among workers), the threads don't act independently of
each other. If you want Python to go faster, you must use multi-processing, not
multi-threading. That said, if Python is too slow, you might be better off
using a faster language.

### Benchmarking Notes

The overall performance of a computer depends on its single-cpu perfomance and
multi-core performance. Some programs run on a single thread (most of your
Python code), while other programs run on multiple threads  (e.g. BLAST). In
order to compare two computers, you must measure (1) single thread performance
(2) multi-thread performance and (3) count the number of CPUs. The Passmark
website is a good place to go to examine the performance of various parts of
your computer.


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




Good Practices
--------------

### Login Customization

You should modify your login script. See the `profile` for inspiration.

### Jobs

+ Use `nice` if you're using a lot of resources
+ Use `top` or `htop` to monitor resources
+ Use `/usr/bin/time` to examine resources after a job is done
+ Use ^C to kill a job in the foreground
+ Use ^Z to sleep a job in the foreground
+ Use `fg` to start a sleeping job in the foreground
+ Use `bg` to start a sleeping job in the background
+ Use `ps` to show jobs here or `ps -lu <username` to show all your jobs
+ Use `kill -9 <jobid>` to kill a job

### Batch Jobs

Use `xargs` to parallelize running a bunch of simple jobs. If you're making
some kind of pipeline, use Snakemake or the equivalent. Here's an example
`xargs` command line with an explanation.

```
find smallgenes/ -name "*.fa" -type f -printf "%f\n" | xargs -P 5 -I {} ./geniso2 smallgenes/{} models/worm.splicemodel --out temp/{}.gff
```

The first part of this command sends all of the filenames in the `smallgenes`
directory to stdout.

`find smallgenes -name "*.fa" -type f -printf "%f\n"`

`xargs` reads the filenames and creates command lines with the contents. The
`-I {}` is used to set up a default placeholder `{}` for the incoming filename.
This is used both for the name of the input file and the output file. Jobs can
be parallelized with `-P` (the example has 5 processes).


### Git Password Persistence

To make your GitHub Personal Access Token persist (so you don't have to
copy-paste it again and again).

```
git config --global user.name "username"
git config --global credential.helper store
```

Another way to make your repo more convient to access is to bind your PAT
directly to your repo.

```
git clone https://{username}:{pat}@github.com/{organization}/{repo}.git
```

### datacore

We have a repo for -omic data processing called datacore. This is a good place
to go for some of your dev data. If you are developing a new dataset that will
be useful to others, put the scripts and a small selection of data in datacore.
Don't fill up datacore or any repo with large datafiles.

https://github.com/KorfLab/datacore2024 (or whatever the year is)

### IPC

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

### Summing probabilities in log-space

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


### Some useful scripts

The `bin` directory contains a couple of demonstration scripts for
inspirtation.

+ `benchmark` is a python-based benchmarking program
+ `memcheck` looks through the `proc` filesystem to examine memory
+ `parallelize` runs a file of command lines in parallel on multiple CPUs
+ `redundancy_check` looks for identical files in the filesystem

The `lib` directory contains libraries that may be generally useful.

+ `korflab.py` has some sequence operations


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
Snakemake on a test set in your VM, not the cluster. Once you are ready to
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
them where they are useful, but most of the time, we write software designed
for the CLI.
