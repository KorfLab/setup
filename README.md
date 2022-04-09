Setup
=====

This is a best practices document to set up your bioinformatics environment in
the Korf Lab.

## Overview ##

Some of these things sound painful. Not doing them will become more painful.

### Do ###

+ Develop and test software in a virtual machine
+ Manage your analyis software with conda
+ Create and perform functional tests regularly
+ Destroy and re-build your VMs from time to time

### Do Not ###

+ Do not develop software on the cluster, use a VM
+ Do not develop software in your main OS, use a VM
+ Do not install analysis software via the operating system, use conda

### Troubleshooting ###

If you find you are running out of memory, or something is taking too long,
it's probably because you didn't create an appropriate test set. Development
always takes longer than you think it will, and creating a very small test set
at the start will pay off 10-fold in the future.

## VM Installation ##

![Overview](layout.png)

These instructions assume you will be installing a Lubuntu Linux distribution
on a Windows computer using VirtualBox. It's not very different with other
distributions or MacOS.

Stuff you will need:

+ Lubuntu https://lubuntu.me
+ VirtualBox https://www.virtualbox.org

Actions you will take:

1. Download Files
2. Create Virtual Machine
3. Install Lubuntu
4. Install Anaconda
5. Post-install Tweaks

### 1. Download files ###

Download the latest Lubuntu distribution. The file will be named something like
"lubuntu-21.10-desktop-amd64.iso". It's about 2GB.

Download VirtualBox. It's much smaller. Run the installer.

### 2. Create Virtual Machine ###

Click the "New" button to create a new VM. You can name it anything. I use
Lubuntu-21.10 because that's what I downloaded. Choose a location. Sometimes I
use the default, but sometimes I choose an external drive. The type is Linux
and the Version is Ubuntu (64-bit).

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

### 3. Install Lubuntu ###

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
one to get the Linux running inside Windows. Click the "Install" buttons and
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

Enter your password and wait for the script to complete. Shutdown the VM
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

### 4. Install Anaconda ###

Open Firefox in your VM and head to https://www.anaconda.com to download
Anaconda. Next open your QTerminal and navigate to your Downloads folder. Run
the shell script there (the example shown below might not be the same).

	cd Downloads
	sh Anaconda3-2021.11-Linux-x86_64.sh

Read the license agreement and answer "yes" (without quotes) to accept the
terms. Use the default location for the install by pressing Enter. It will take
a little time to install. When the installer asks if you want to initialize
Anaconda3 by running conda init, answer "yes".

Close your terminal and open a new one. You should see `(base)` at the start of
each prompt. This means you're in the base `conda` environment. When you
install new bioinformatics programs or even programming languages, use `conda`
to do that for you.

For more information about `conda` see the KorfLab/learning-conda repo.

You can now remove the Anaconda install file from your Downloads folder.

### 5. Post-install Tweaks ###

You will use the QTerminal application all the time. To make it easy to get to,
click-n-drag its icon to the Menu Bar at the bottom of the screen (the
application is in "System Tools").

The default text editor is called FeatherPad, which can be found in the
Accessories menu. You can click-n-drag that to the Menu Bar if you like it.
However, you might want to install something else, as editors can be very
personal things.

Open the QTerminal application and create a new directory for your Code.

	mkdir Code

Make a couple directories there.

	chdir Code
	mkdir bin lib

Grab the KorfLab setup repository.

	git clone https://github.com/KorfLab/setup

You will probably want to put some aliases and environment variables in your
`.bashrc`. For example, I use these conveniences.

```
alias ls="ls -F"
alias lst="ls -lrth"
alias cls="clear; ls"
alias ..="cd .."
alias gs="git status"

PATH=$PATH:$HOME/Code/bin
export PYTHONPATH=$PYTHONPATH:$HOME/Code/lib
export PERL5LIB=$PERL5LIB:$HOME/Code/lib
```

You can copy-paste these to your login script or better yet, `source` them in
from the setup repo. Put a line like this at the end of `.bashrc`, after your
conda initialization.

	source $HOME/Code/setup/profile

-----------------------------------------------------------------------------

This part is optional. If you want to share files between your host OS and your
VM, you need to set up a shared folder. Why would you do this?

+ Your favorite editor is only available on your host OS
+ You have large-ish data files you don't want to copy the VM

Select the "Shared Folders" tile. Click on the folder with the + sign at the
far right to make a new shared folder.

The "Folder Path" is the folder on your host OS (Windows). Navigate to the
folder you want to share. If it doesn't exist, create it. The Folder Name
should auto-populate.

The "Mount Point" is where you want the folder to show up in your VM. For
example, you might use a mount point of `/home/$USER/MyStuff`, which would show
up in your Lubuntu home, or `/shared`, which would be off the filesystem root.

Check Auto-mount and Make Permanent. If the shared directory is strictly data,
you might mount it Read-only, but if it's code, then definitely not.

After clicking OK, you should be able to see the directory in your VM. However,
you don't have permission to use it. Add yourself to the vboxsf group with the
following command.

	sudo adduser $USER vboxsf

You have to restart for the changes to take effect.

-----------------------------------------------------------------------------

At some point, Lubuntu will ask you if you want to apply updates. Sure, it's
always a good idea. If you don't want to wait, you can go to Start Menu ->
Preferences -> Apply Full Upgrade.

## Directory Structure ##

Your directory structure should now look something like this:

	anaconda3/
	Code/
		bin/
		lib/
		setup/
	Desktop/
	Documents/
	Downloads/
	Music/
	Pictures/
	Public/
	Templates/
	Videos/

Do all of your software development and testing in the Code directory.

## Unix and Python ##

Everyone is expected to have a working knowledge of Unix and Python. If you
want to learn/review, `git clone` it from inside your Code directory.

	chdir ~/Code
	git clone https://github.com/iankorf/MCB185-2022

## Programs vs. Pipelines vs. Notebooks ##

There are 3 overlapping computer activities we tend to do.

1. Software development in Python, C, Go, etc
2. Running pipelines in Snakemake
3. Exploring data in R-Studio or Jupyter notebooks

### Software Development ###

You should already know Python before moving on to other languages.

To get started with go, see the https://github.com/KorfLab/learning-go

To get started with C, see the https://github.com/KorfLab/learning-C

### Running Pipelines ###

When analyzing large datasets, there are generally 3 tasks.

1. Installing other peoples' software - https://github.com/KorfLab/learning-conda
2. Developing the pipeline on a test set - https://github.com/KorfLab/learning-snakemake
3. Deploying the pipeline on a large dataset - https://github.com/KorfLab/spitfire

Pipelines are developed using Conda and Snakemake. Always install software with
Conda. Don't rely on the local environment. Develop your Snakemake pipelines on
a small test set in a VM, and not on the cluster. These practices ensure
maximum portability and reproducible data practices.

### Notebook Computing ###

We're not talking about laptops but rather R-Studio or Jupyter. These tools are
great for exploring data, but are not a great way of distributing software. Use
them where they are useful.

## Data ##

We have a repo for -omic data processing called datacore. If you are developing
a new dataset that will be useful to others, put the scripts and a small
selection of data in datacore. Don't fill up datacore or any repo with large
datafiles.

https://github.com/KorfLab/datacore

Data is generally kept in a completely separate place from code. If you have
scripts in the same directory with data, you're doing it wrong. Code belongs in
your github repos. On the cluster, we put data in `/share/korflab/projects`.
See the spitfire repo for more information.
