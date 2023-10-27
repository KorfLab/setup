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


VM Installation for Windows Computer
------------------------------------

Q: Which Linux distribution should I use?

A: It doesn't really matter. The Linux distributions designed for older
hardware use less resources. Lubuntu and Linux Lite are two excellent choices.

These instructions assume you will be installing a Lubuntu Linux distribution
on a Windows computer using VirtualBox. It's not very different with other
distributions.

Stuff you will need:

+ Lubuntu https://lubuntu.me
+ VirtualBox https://www.virtualbox.org

Actions you will take:

1. Download Files
2. Create Virtual Machine
3. Install Lubuntu

### Troubleshooting

If you follow the instructions below and you get stuck, ask for help.

Some Windows computers are not set up for virtualization. You may need to
change some BIOS settings.

### 1. Download files

Download the latest Lubuntu or equivalent distribution. The file will be named
something like "lubuntu-21.10-desktop-amd64.iso". It's about 2GB.

Download VirtualBox. It's much smaller. Run the installer.

### 2. Create Virtual Machine

Click the "New" button to create a new VM. You can name it anything. I used
Lubuntu-21.10 because that's what I downloaded. Choose a location. Sometimes I
use the default, but sometimes I choose an external drive. The type is Linux and
the Version is Ubuntu (64-bit).

Assign the VM 2G Memory. The install might not work well with less and doesn't
need any more. You can change the amount of memory and the number of CPUs
later.

Create a virtual hard disk using the default VDI and dynamic allocation. Set
the size to 40G. Because of the dynamic allocation, you will only use about 10G
in Windows. For software development and testing purposes, you will probably
not need more than 40G. You might think it's a good idea to set the limit
higher just in case, but it's easy to write a program that spams output and
fills up your filesystem with junk. In such cases, it's better to have 40G of
junk than 500G.

### 3. Install Lubuntu

In "Oracle VM VirtualBox Manager" scroll down until you see "Storage". Click on
the Optical Drive, and connect it to the Lubuntu iso image you downloaded
earlier.

Press the "Start" button. Soon you will see a typical computer desktop that
looks a little like Windows.

Double-click on the "Install Lubuntu" icon on the desktop.

Click "Next" a couple times. When in doubt use the default parameters. When it
shows you the option to Erase disk, click the radio button. You cannot erase
your Windows disk. This is erasing the virtual disk you just made. Click
"Next".

Enter your name and username any way you like. Click the box to log in
automatically. Your Windows OS already has a password. You don't need another
one to get to the Linux running inside Windows. Click the "Install" buttons and
wait a few minutes while Lubuntu installs.

Click the Restart button when it asks you to. After a little while it will tell
you to remove the instllation medium and then press Enter. Just press Enter.

------------------------------------------------------------------------------

After you see the Lubuntu desktop again, click on the Devices menu at the top.
Select "Insert Guest Additions CD image...". It probably wont' autorun
properly, so we have to do this the manual way.

Click on the bird icon in the lower left of the screen. This is the Start Menu.
Under "System Tools" you will find "QTerminal". Run that. Right now, the
Lunbuntu desktop may be really small. We'll fix that later. To make sure you
can see all the terminal output, click the QTerminal's maximizing icon (looks
like 2 triangles).

Change directory to the location of your optical drive. For me, it looks
something like this.

	cd /media/ian/VBox_GAs_6.1.30

You need to run the post-install script as the super-user.

	sudo sh VBoxLinuxAdditions.run

Enter your password and wait for the script to complete. Shutdown the VM by
clicking the Start Menu and choosing Leave->Shutdown.

-----------------------------------------------------------------------------

Back in Oracle VM VirtualBox Manger, Select the "Settings" button.

Select the "General" tile and then click on the "Advanced" tab. Set the Shared
Clipboard to Bidirectional.

Select the "System" tile, you can change the amount of memory and the number of
processors. For software development, you can keep the 2G RAM and 1 CPU, but if
you're doing pipeline development, you may want more RAM and more CPUs. You
should always leave Windows about 4G RAM and 2 CPUs.

Select the "Storage" tile. Click on the Optical Drive and remove the
VBoxGuestAdditions.iso.

-----------------------------------------------------------------------------

Press the Start button again. Things that now work.

+ Resize the screen by click-n-drag to whatever you like
+ Copy-paste from Windows to Linux and back

-----------------------------------------------------------------------------

This part is optional. If you want to share files between your host OS and your
VM, you need to set up a shared folder. Why would you do this?

+ You have large-ish data files you don't want to copy to the VM
+ Your favorite editor is only available on your host OS

Select the "Shared Folders" tile. Click on the folder with the + sign at the
far right to make a new shared folder.

The "Folder Path" is the folder on your host OS (Windows). Navigate to the
folder you want to share. If it doesn't exist, create it. The Folder Name
should auto-populate.

The "Mount Point" is where you want the folder to show up in your VM. For
example, if you wanted to share a data directory from your host OS, you might
use a mount point of `/home/$USER/Data`, which would show up in your Lubuntu
home, or `/data`, which would be off the filesystem root.

Check Auto-mount and Make Permanent. If the shared directory is strictly data,
you might mount it Read-only, but if it's code, then definitely not.

After clicking OK, you should be able to see the directory in your VM. However,
you don't have permission to use it. Add yourself to the vboxsf group with the
following command.

	sudo adduser $USER vboxsf

You have to restart for the changes to take effect.


Conda
-----

Bioinformatics software is frequently not well-maintained. For this reason, it
may not compile with the latest compilers and libraries. As a result, we must
build software with out-dated libraries that are known to work. The software we
use that manages these kinds of dependancies is Conda (which is distributed
either as Anaconda or Miniconda). Package management is a complex topic, so it
will be explained using a couple analogies.

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

Download and install Miniconda or Anaconda. Anaconda comes pre-configured with
a bunch of analysis software built-in. Miniconda is a stripped down version
with the bare necessities. I prefer to start with Miniconda and add packages
when I need them. Follow the directions on the website.

+ Miniconda - https://docs.conda.io/projects/miniconda/en/latest
+ Anaconda - https://www.anaconda.com

Read the license agreement and answer "yes" (without quotes) to accept the
terms. Use the default location for the install by pressing Enter. It will take
a little time to install. When the installer asks if you want to initialize by
running conda init, answer "yes".

Close your terminal and open a new one. You should see `(base)` at the start of
the prompt. This means you're in the base `conda` environment. If you don't see
`(base)`, you're not using `conda`. Stop whatever you're doing, get help, and
fix the problem before moving on.

For more information on using conda, see
https://github.com/KorfLab/learning-conda


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

Now install Miniconda as you did on your personal computer, and also install
`mamba` if you like.

If you examine your `.bashrc` file, you will notice that the conda installation
modified it. It will look something like this (except with your username and
not `ikorf`). Don't modify this part ever.

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

### conda/mamba

If your prompt doesn't start with `(base)`, get help now.

Create a new environment and install some software to make sure it works.

```
conda create --name blast
conda activate blast
```

You should now see `(blast)` instead of `(base)`. To install BLAST programs in
this environment, do the following command.

```
mamba install -c bioconda blast-legacy
```

Try running `blastall`. You should see a long usage statement.
