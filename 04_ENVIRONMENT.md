Bioinformatics Environment
==========================

We do science and write code in a Unix/Linux environment.

## Unix/Linux ##

Most professional bioinformatics is done in a Unix/Linux environment. While
Windows now has built-in support for Linux (WSL), it's generally better to work
inside a Linux virtual machine (VM). There are other Unix CLI environments like
Cygwin, and Gitbash for Windows. They generally work most of the time.

Mac users have Unix built in (Darwin), and typically don't use VMs. By default,
MacOS does not install the developer tools, so you'll have to do that manually
to have programs like `git` by doing: `xcode-select --install`.

All of the clusters on campus run Linux. At some point your computational needs
will exceed your personal computer and you will need to use a cluster, which
means a Unix-like CLI.

To install a local CLI environment, you can:

- Buy a Mac
- Install Linux on an older PC
- Install VirtualBox on PC and run some Linux distro (e.g. Lubuntu)
- Install Cygwin on PC
- Use the Linux environment in Windows

Modify your login script (see `init/etc/profile` for inspiration).

Use `top` or `htop` to monitor resources live. Use `/usr/bin/time -v` to
examine resources after a job is done. The normal `time` command doesn't do
this. You may have to install `/usr/bin/time` via conda.

If `git` asks for you personal access token again and again, use the following
command to make it persist: `git config --global credential.helper store`.

## Hive ##

To use the UCD cluster, get an account on Hive. Go to https://hippo.ucdavis.edu
and select the Hive cluster. Your sponsor is ikorfgrp.

Each user has a home directory with 20G. This is backed up. 20G is probably
enough for your needs, but if not, create a home-away-from-home in the shared
space `/quobyte/ikorfgrp/home`. To do that, you will need to redefine `$HOME`
to point to the new location. Note that nothing in `/quobyte/ikorfgrp` is
backed up.

If you are about to run a job on the cluster and don't know how much RAM and
disk space your job will use, you shouldn't run the job. Step away from the
keyboard until such time as you can be a responsible user.

How can you determine what resources will be required without running the job
in the first place? By doing experiments on a smaller scale and observing what
happens as the scale increases. To observe the resources used, prepend
`/usr/bin/time -v` to your job (which may not be installed by default).

For testing purposes, you may find `bin/mysbatch` useful for running mock slurm
jobs on the cluster. There is an example slurm file in
`data/sbatch-example.slurm`.

Once you are running jobs on the cluster, `squeue --me` is how you see the
status of your jobs (running, queued, etc). You can also view all the other
jobs on the cluster and even get the data in json.

## Conda ##

You should use Conda to install most CLI software both on your personal
computers and your Hive account.

To install Conda on your personal computer: https://conda-forge.org/miniforge

Conda is already provided on Hive via `module load conda`. You should probably
add this to your `.bash_profile`. Even the the `module` system has a lot of
bioinformatics software already installed, you should avoid using it if
possible. Why? Because the module system isn't easily replicated by you or
others on computers elsewhere.

## Personal Computers ##

You are expected to do some work on your personal computer(s) (see Rule #2).
Most operating systems have directories for Desktop, Documents, Downloads, etc.
Where should you put your code and experiments? All of my Git repositories are
inside a Code directory. Experiments with that code are generally in a `build`
directory, since that is ignored by Git.

```
Code/
	bin/
		benchmark@ -> ../init/bin/benchmark
	lib/
		korflab.py@ -> ../init/lib/korflab.py
	init/
		bin/
			benchmark
		lib/
			korflab.py
Desktop/
Documents/
Downloads/
```

- All repos are in the `Code` directory
- `$PATH` includes `Code/bin` and I softlink files to that directory
- `$PYTHONPATH` includes `Code/lib` and I softlink files to that directory
- Large datafiles are always kept compressed

## Style Guide ##

In general, we rabidly follow the style guides of the languages we write in.
These "rules" apply to all languages:

- Don't use language-specific constructs just because you can
- Follow the 80 column rule (lines should be less than 80 characters)
- Variables are nouns, functions are verbs
- The larger the scope of a variable, the longer the name
- The larger the scope of a function, the shorter the name
- Use tabs for left-side indentation unless the language says NO
- Never hard-code file or directory paths
- Avoid global variables
- De-nest conditionals
- Avoid ISA inheritence or limit to 1 level
- Python specifics
	- We use tabs for indentation (if you must use spaces find another lab)
	- Use `argparse` for CLI
	- Use `if __name__ == '__main__'` only if you know why
	- Limit dunders and decorators
	- Annotations are cool, but documentation is cooler
- R specifics
	- Use tidyverse syntax only (tibbles not data.frames)
	- Use snake_case for variables and MixedCase for functions
- C specifics
	- Tabs and one true brace
	- Everything is a pointer to a struct
- Other Languages
	- C++: what's wrong with plain old C?
	- Java: system.out.println("hell no");
	- Javascript: FFS no
	- Julia: we tried that and it wasn't that great
	- Lua: really? let's discuss
	- Rust: maybe
	- SQL: as long as it's followed by lite
