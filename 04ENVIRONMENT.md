Bioinformatics Environment
==========================

We do science and write code in a Unix/Linux environment.


Unix/Linux
----------

Most professional bioinformatics is done in a Unix/Linux environment. While
Windows now has built-in support for Linux (WSL), it's generally better to work
inside a Linux virtual machine (VM). There are other Unix CLI environments like
Cygwin, and Gitbash for Windows. They generally work most of the time.

Mac users have Unix built in (Darwin), and typically don't use VMs. By default,
MacOS does not install the developer tools, so you'll have to do that manually
to have programs like `git` by doing: `xcode-select --install`.

All of the clusters on campus run Linux. At some point your computational needs
will exceed your personal computer and you will need to use a cluster.

To install your CLI environment, see the latest MCB185 course materials.

Conda
-----

Bioinformatics software is frequently not well-maintained. For this reason, it
may not compile with the latest compilers and libraries. As a result, we must
build software with out-dated libraries that are known to work. The software we
use that manages these kinds of dependancies is `conda`. There are a confusing
number of things in the conda ecosystem like Anaconda, miniconda, microconda,
mamba, Mambaforge, and Miniforge. The current recommended distribution is
Miniforge3.

### Computer Instructions Analogy

Have you ever been given instructions for your computer on how to connect to a
VPN, install a printer, or update a driver? Have you noticed that half the time
the instructions are out of date? It could happen that your computer is older
than the instructions or that your computer is newer. Either way, the buttons,
windows, etc might look different or even be incompatible. Wouldn't it be
better if the directions "knew" which version of computer you had so that you
they actually applied to your computer? Of course that would be better, but it
would mean you would need multiple sets of instructions, each tailored to every
specific situation. Believe it or not, this is what Conda offers.

### Cooking Analogy

Programs depend on libraries. It's sort of like saying that pizza depends on
ingredients. In order to make pizza, you need ingredients like flour, salt,
olive oil, cheese, etc. Computer programs, like some recipies, can be very
picky. If the recipe calls for OO flour, can you substitute AP flour or bread
flour? If the recipe calls for 68 degree water, can you substitute boiling
water? It's hard to know until the recipe fails. Programs are the same way.
Sometimes they fail to work properly because the "chef" didn't specify the
ingredients exactly.

A "package manager" is software that ensures that your ingredients are exactly
as you specify. Suppose you have an awesome recipe for orange muffins that you
got from your grandmother. It calls for the artificial orange drink "Tang".
However, when you make the recipe it doesn't taste quite the same as you
remember. That's because the recipe was developed a long time ago, and Tang
today isn't the same as it used to be. If you want to make the original recipe,
you have to specify that "Tang" is actually "tang-1.0" and not the current
"tang-2.25". Thankfully, you can still import 1.0 from Mexico.

The recipe also calls for all-purpose flour. Your grandmother used to use Gold
Medal but you happen to have King Arthur. Do you need to try to replicate the
exact flour used at the time or will it work just fine with what you have? You
can imagine that specififying every single ingredient would be a pain. And it
is. So you just need to specify the things that have changed enough to break
the recipe.

A "package manager" specifies a "base" set of ingredients for you to cook with.
It provides you with sugar, salt, flour etc. If you need something very
specific, it will get that for you.

### Genomic Analysis Analogy

Imagine you're performing an RNA-seq analysis. There are 2 major steps in the
process:

1. Aligning the reads to the genome
2. Performing differential expression analysis

You last ran the pipeline 2 years ago and got a bunch of cool figures. However,
your PI lost some of the figures and wants you to regenerate them. So you run
the pipeline again and find that it doesn't work the same as it did. Why?

* The genome you aligned to may have been updated
* The alignment software may have been updated
* The pipeline software may have been updated
* The analysis software may have been updated

Updates are necessary to fix bugs. But those bugs may change the behavior of
the software in ways you didn't predict. It's easy to specify exactly which
genome sequence you were using as you probably saved it. But exactly what
version of Python, bowtie, Snakemake, etc? You probably didn't write those
down. Even if you did, each of those programs relies on 10-20 libraries that
you don't even know the names of.

### Installation

https://conda-forge.org/miniforge

Download the Miniforge3 installer for your OS and then run the installer.

Read the license agreement and answer "yes" (without quotes) to accept the
terms. Use the default location for the install by pressing Enter. It will take
a little time to install. When the installer asks if you want to initialize by
running conda init, answer "yes".

Close your terminal and open a new one. You should see `(base)` at the start of
the prompt. This means you're in the base `conda` environment. If you don't see
`(base)`, try `conda activate base`.

Spitfire
--------

Our "head node" for the cluster is `spitfire`. This is where we do large jobs
and submit jobs to the cluster. In order to get an account, you must first
request one by pointing your web browser to
`computing.genomecenter.ucdavis.edu`.

In the directions that follow, the value of `username` will be whatever your
actual user name is.

Once you have an account, you can `ssh` to log into `spitfire` or `scp` if
you want to copy files there.

```
ssh username@spitfire.genomecenter.ucdavis.edu
scp yourfile username@spitfire.genomecenter.ucdavis.edu:
```

The connection to your default home directory `/home/username` is designed to
time-out after a while. This means that any long jobs may fail. For this
reason, it is essential to move your `$HOME` to another mount point that is
stable.

In your given home directory, create a new `.profile` that contains the
following information. The first line sets your home directory to a new
location, which we'll make below. The second line makes sure you get out of
your current location and into your lab home. The third line activates your
login script, which we'll modify in a sec.

```
HOME=/share/korflab/home/username
cd
source .bashrc
```

As a member of the lab, you have access to `/share/korflab`. Create a new
directory in `/share/korflab/home/username` for yourself. This is your lab home
directory. Create a `.bashrc` in your home directory.

Now install conda as you did on your personal computer.

If you examine your `.bashrc` or `.zshrc` file, you will notice that the conda
installation modified it. It will look something like this (except with your
username and not `ikorf`). Don't modify this part ever.

```
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/share/korflab/home/ikorf/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/share/korflab/home/ikorf/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/share/korflab/home/ikorf/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/share/korflab/home/ikorf/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

Put your own login items **after** the conda setup. For example, you might find
the following modifications useful.

```
alias ls="ls -F"
alias rm="rm -i"
alias cp="cp -i"
alias mv="mv -i"
alias cls="clear; ls"

PATH=$PATH:$HOME/bin
export PYTHONPATH=$HOME/lib
```

Log out and back in again. Your prompt should have `(base)` at the front, which
indicates you're in the base conda environment.


Verifiy Setup
-------------

Let's make sure your computing environment works properly. Do these procedures
on your personal computer as well as your cluster home.

### home

Run the following command. If this doesn't report
`/share/korflab/home/username`, get help now.

```
echo $HOME
```

### git

Run the following command. If this doesn't work, get help now.

```
git clone https://github.com/KorfLab/datacore
```

### python

Run the following command. If this doesn't report `Python 3.10.10` or something
like that, get help now.

```
python3 --version
```

