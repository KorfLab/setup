Setup
=====

This is a best practices document to set up your programming environment in the
Korf Lab.

## VM vs. Laptop vs. Desktop vs. Cluster ##

It's best to do all of your code development and testing in a relateively small
Linux virtual machine. Any modern laptop or desktop is fine. Consider deleting
and recreating your VMs on a regular basis. If you can do this with little
interruption it means your code and data practices will be easily replicated by
others. If you cannot do this, you probably have some dangerous practices.

If you find you are running out of memory, or something is taking too long,
it's probably because you didn't create an appropriate test set. Development
always takes longer than you think it will, and creating a very small test set
at the start will pay off 10-fold in the future.

## VM Installation ##

These instructions assume you will be installing a Lubuntu Linux distribution 
on a Windows computer using VirtualBox. It's not very different with other 
distributions or MacOS.

Stuff you will need:

+ Lubuntu https://lubuntu.me
+ VirtualBox https://www.virtualbox.org

Actions you will take:

1. Download files
2. Create a virtual machine
3. Boot into Lubuntu Desktop
4. Install Lubuntu
5. Install Linux Guest Additions
6. Update
7. Install Anaconda
8. Final tweaks

### 1. Download files ###

Download the latest Lubuntu distribution. The file will be named something like
"lubuntu-21.10-desktop-amd64.iso". It's about 2GB.

Download VirtualBox. It's much smaller. Run the installer.

### 2. Create a virtual machine ###

Click the "New" button to create a new VM. You can name it anything. I use 
Lubuntu-21.10 because that's what I downloaded. Choose a location. Sometimes I 
use the default, but sometimes I choose an external drive. The type is Linux 
and the Version is Ubuntu (64-bit).

Assign the VM 2G Memory. The install might not work well with less and doesn't
need any more. You can change the amount of memory and the number of CPUs
later.

Create a virtual hard disk using the default VDI and dynamic allocation. Set 
the size to 40G. Lubuntu will take up about 12G. Once you start adding conda 
environments and data, you will start to use more. Setting the limit at 40G 
prevents you from executing a runaway process that tries to use your whole 
disk. Using the dynamic allocation uses only the amount you need, so if you 
have 10G in your VM, your Windows will only be impacted by 10G.

### 3. Boot into Lubuntu Desktop ###

In "Oracle VM VirtualBox Manager" scroll down until you see "Storage". Click on
the Optical Drive, and connect it to the Lubuntu iso image you downloaded
earlier.

Press the "Start" button. Soon you will see a typical computer desktop that
looks a little like Windows.

### 4. Install Lubuntu ###

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

### 5. Install Linux Guest Additions ###

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

### 6. Update ###

Back in Oracle VM VirtualBox Manger, click on the "Settings" button. Under the 
"System" tile, you can change the amount of memory and the number of 
processors. I typically set the memory to 4G and the processors to 2. Depending 
on your situation, you might allocate more or less. You can always change your 
mind later. Click OK.

Back at the main menu, scroll down to "Storage". Click on the Optical Drive and
remove the VBoxGuestAdditions.iso.

Press the Start button again. You should now be able to click-n-drag the window
to resize the desktop to whatever shape you want.

Under the "Devices" menu at the top, click "Shared Clipboard" and then choose
Bidirectional. This will let you copy-paste from Windows to Linux and back.

You will use the QTerminal application all the time. To make it easy to get to,
click-n-drag its icon to the Menu Bar at the bottom of the screen (the
application is in "System Tools").

Now let's make sure the OS has all the latest patches. Go to Start Menu ->
Preferences -> Apply Full Upgrade. Enter your password and wait for it to
complete. And then reboot... again.

### 7. Install Anaconda ###

Open Firefox in your VM and head to https://www.anaconda.com to download
Anaconda. Next open your QTerminal and navigate to your Downloads folder. Run
the shell script there (the example shown below might not be the same).

	cd Downloads
	sh Anaconda3-2021.11-Linux-x86_64.sh

Read the license agreement and answer yes to accept the terms. Use the default
location for the install by pressing Enter. It will take a little time to
install. When the installer asks if you want to initialize Anaconda3 by running
conda init, answer yes.

Close your terminal and open a new one. You should see `(base)` at the start of
each prompt. This means you're in the base `conda` environment. When you
install new bioinformatics programs or even programming languages, use `conda`
to do that for you.

For more information about `conda` see the KorfLab/learning-conda repo.

### 8. Final tweaks ###

You will probably want to put some aliases and environment variables in your
`.bashrc`. I append the following to the file (after the conda setup).

```
alias ls="ls -F"
alias cls="clear; ls"
alias lst="ls -lrth
alias ..="cd .."
alias gs="git status"
alias spit="ssh ikorf@spitfire.genomecenter.ucdavis.edu"
PATH=$PATH:$HOME/Code/bin
export PYTHONPATH=$PYTHONPATH:$HOME/Code/lib
export PERL5LIB=$PERL5LIB:$HOME/Code/lib
```

The default text editor is called FeatherPad, which can be found in the
Accessories menu. You can click-n-drag that to the Menu Bar if you like it.
However, you might want to install something else, as editors can be very
personal things.

## Directory Structure ##

If you've followed the directions above, your home directory will look
something like this:

	Desktop/
	Documents/
	Downloads/
	Music/
	Pictures/
	Public/
	Templates/
	Videos/
	anaconda3/

Let's create a directory for all of your programming.

	mkdir Code

The reason that `Code` is capitalized is to follow the "Directories are
capitalized" practice in your home directory. Inside your `Code` directory, we
will follow a more standard Unix practice of using lowercase everywhere. Change
directory to `Code` and create a couple of new directories.

	chdir Code
	mkdir bin
	mkdir lib

Now clone some repos.

	git clone https://github.com/KorfLab/setup
	git clone https://github.com/iankorf/MCB185-2022

Your directory structure should now look like this:

	Code/
		MCB185-2022/
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
	anaconda3/

Depending on your needs, you may also want the following repos. Again, `git
clone` these into your Code directory.

	git clone https://github.com/KorfLab/learning-conda
	git clone https://github.com/KorfLab/learning-snakemake
	git clone https://github.com/KorfLab/learning-go
	git clone https://github.com/KorfLab/learning-C
	git clone https://github.com/KorfLab/spitfire
	git clone https://github.com/KorfLab/datacore

## Unix and Python ##

We do all of our work in a Unix/Linux enviornment and Python is our default
language. You need to have a working knowledge of both. Ian teaches a
Unix/Python course every year called MCB185.

## Programs vs. Pipelines vs. Notebooks ##

There are 3 overlapping computer activities we tend to do.

1. Developing programs in Python, C, Go, etc
2. Running pipelines in Snakemake
3. Exploring data in R-Studio or Jupyter notebooks

### Software Development ###

You should already know Python before moving on to other languages.

To get started with go, see the https://github.com/KorfLab/learning-go

To get started with C, see the https://github.com/KorfLab/learning-C

### Running Pipelines ###

When analyzing large datasets, there are generally 3 tasks.

1. Installing other peoples' software - Conda
2. Developing the pipeline on a test set - Snakemake
3. Deploying the pipeline on a large dataset - Cluster

Pipelines are developed using Conda and Snakemake.

To get started with Conda, see https://github.com/KorfLab/learning-conda

To get started with Snakemake, see
https://github.com/KorfLab/learning-snakemake

To get started with the cluster, see https://github.com/KorfLab/spitfire

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
