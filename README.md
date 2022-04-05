Setup
=====

This is a best practices document to set up your programming environment in the
Korf Lab.

## VM vs. Laptop vs. Desktop vs. Cluster ##

It's best to do all of your code development and testing in a Linux virtual
machine.

+ If you make a mistake, you only messed up the VM
+ By developing in a limited environment, you decrease development time
+ By developing in multiple VMs, you increase portability

If you are running out of memory, or it's taking too long, it's probably because
you didn't create an appropriate test set. Development always takes longer than
you think it will, and creating a very small test set at the start will pay off
10-fold in the future.

## Directory Structure ##

By default, your Linux home directory structure looks something like this:

	Desktop
	Documents
	Downloads
	Music
	Pictures
	Public
	Templates
	Videos

Let's create a directory for all of your programming.

	mkdir Code

The reason that `Code` is capitalized is to follow the "Directories are 
capitalized" practice in your home directory. Inside your `Code` directory, we 
will follow a more standard Unix practice of using lowercase everywhere. Change 
directory to `Code` and create a couple of new directories.

	chdir Code
	mkdir bin
	mkdir lib

Now clone this repo.

	git clone https://github.com/KorfLab/setup

Your directory structure should now look like this:

	Code
		bin
		lib
		setup
	Desktop
	Documents
	Downloads
	Music
	Pictures
	Public
	Templates
	Videos

## Unix and Python ##

We do all of our work in a Unix/Linux enviornment and Python is our default 
language. You need to have a working knowledge of both. Ian teaches a 
Unix/Python course every year called MCB185. Use the latest version of the 
course. You can find it on GitHub.

## Unix Shell ##

Depending on your OS, shell, and possibly other stuff, your startup script will
have one of the following names.

+ `.bashrc`
+ `.bash_profile`
+ `.profile`
+ `.zshrc`

Edit your startup script to include a couple useful aliases and environment
variables.

	alias ls="ls -F"
	alias cls="clear; ls"
	alias lst="ls -lrt"
	PATH=$PATH:$HOME/Code/bin

The `PATH` environment variable already exists. The statement above tells your
shell to include your `Code/bin` as another place to look for executables.

The `PYTHONPATH` environment variable might not exist, which is why we have to
`export` it. The `~/Code/lib` directory is where we will put soft-links to
various Python libraries under development.

Restart your terminal after you edit your login script. This will ensure that
the changes take effect now and the next time you log in.

## Programs vs. Pipelines vs. Notebooks ##

There are 3 overlapping computer activities we tend to do.

1. Developing programs in Python, Go, etc
2. Running pipelines in Snakemake
3. Exploring data in R-Studio or Jupyter notebooks

### Software Development ###

Some of the work we do in the lab is writing novel programs in Python or Go 
(and much less frequently in other languages such as C and Perl). For these 
tasks we usually use text editors and terminals rather than IDEs. All software 
development and testing should be done in a VM on your laptop/desktop and not 
the cluster or spitfire.

To get started with go, see the https://github.com/KorfLab/learning-go

To get started with C, see the https://github.com/KorfLab/learning-C

### Running Pipelines ###

When analyzing large datasets, there are generally 3 tasks.

1. Installing other peoples' software - Conda
2. Developing the pipeline on a test set - Snakemake
3. Depoloying the pipeline on a large dataset - Cluster

Pipelines are developed using Conda and Snakemake.

To get started with Conda, see https://github.com/KorfLab/learning-conda

To get started with Snakemake, see https://github.com/KorfLab/learning-snakemake

If you want to run on the cluster, see https://github.com/KorfLab/spitfire

### Notebook Computing ###

We're not talking about laptops but rather R-Studio or Jupyter. These tools are 
great for exploring data, but are not a great way of distributing software. Use 
them where they are useful.

## Data##

Unfinished section about how to organize data.

## Backup ##

Unfinished section on how to backup stuff.
