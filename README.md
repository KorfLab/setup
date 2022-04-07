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

## VM Installation ##

These instructions assume you will installing a Lubuntu Linux distribution on
a Windows computer using VirtualBox.

Stuff you will need:

+ Lubuntu https://lubuntu.me/
+ VirtualBox https://www.virtualbox.org/

Actions you will take:

1. Download files
2. Create a virtual machine
3. Boot into Lubuntu Desktop
4. Install Lubuntu
5. Install Linux additions
6. Update
7. Final tweaks

### 1. Download files ###

Download the latest Lubuntu distribution. The file will be named something like
"lubuntu-21.10-desktop-amd64.iso". It's about 2GB.

Download VirtualBox. It's much smaller. Run the installer.

### 2. Create a virtual machine ###

Click the "New" button to
create a new VM. You can name it anything. I use Lubuntu21. Choose a location
(I use default). The type is Linux and the Version is Ubuntu (64-bit).

Assign the VM 2G Memory. The install might not work well with less and doesn't
need any more. You can change the amount of memory and the number of CPUs later.

Create a virtual hard disk using the default VDI and dynamic allocation. Set
the size to 40G. Lubuntu will take up about 12G. Once you start
adding conda environments and data, you will start to use more. Setting the
limit at 40G prevents you from executing a runaway process that tries to use your
whole disk. Using the dynamic allocation uses only the amount you need, so if
you have 10G in your VM, your Windows will only be impacted by 10G.

### 3. Boot into Lubuntu Desktop ###

In "Oracle VM VirtualBox Manager" scroll down until you see "Storage". 
Click on the Optical Drive, and connect it to the Lubutu iso
image you downloaded earlier.

Press the "Start" button. Soon you will see a typical computer desktop that
looks a little like Windows.

### 4. Install Lubuntu ###

Double-click on the "Install Lubuntu" icon on the desktop.

Click "Next" a couple times. When in doubt use the default parameters.
When it shows you the option to Erase disk, click
the radio button. You cannot erase your Windows disk. This is erasing the
virtual disk you just made. Click "Next".

Enter your name and username any way you like. Click the box to log in
automatically. Your Windows OS already has a password. You don't need another
one to get the Linux running inside Windows. Click the "Install" buttons and
wait a few minutes while Lubuntu installs.

Click the Restart button when it asks you to. After a little while it will tell
you to remove the instllation medium and the press Enter. Just press Enter.

### 5. Install Linux additions ###

After you see the Lubuntu desktop again, click on the Devices menu at the top.
Select "Insert Guest Additions CD image...". It probably wont' autorun
properly, so we have to do this the manual way.

Click on the bird icon in the lower left of the screen. This is the Start menu. Under "System Tools"
you will find QTerminal. Run that. Right now, the Lunbuntu desktop may be really small.
We'll fix that later. To make sure you can see all the terminal output,
click the QTerminal's maximizing icon (looks like 2 triangles). 

Change directory to the location
of your optical drive. For me, it looks something like this.

	cd /media/ian/VBox_GAs_6.1.30

You need to run the post-install script as the super-user.

	sudo sh VBoxLinuxAdditions.run

Enter your password and wait for the script to complete. Shutdown the VM
clicking the Start menu and choosing Leave->Shutdown.

### 6. Update ###

Back in Oracle VM VirtualBox Manger, click on the Settings button. Under the System
tile, you can change the amount of memory and the number of processors. I typically
set the memory to 4G and the processors to 2. Depending on your situation, you might
allocate more or less. You can always change your mind later. Click OK.

Back at the main menu, scroll down to Storage. Click on the Optical Drive and remove
the remove the VBoxGuestAdditions.iso.

Press the Start button again. You should now be able to
click-n-drag the window to resize the desktop to whatever shape you want.

Under the Devices menu at the top, click "Shared Clipboard" and then choose 
Bidirectional. This will let you copy-paste from Windows to Linux and back.

You will use the QTerminal application all the time. To make it easy to get to,
click-n-drag its icon to the Menu Bar (it's in System Tools). 

Now let's make sure the OS
has all the latest patches. Go to Start Menu -> Preferences -> Apply Full Upgrade.
Enter your password and wait for it to complete. And then reboot... again.

### 7. Final teaks ###

The default text
editor is called FeatherPad, which can be found in the Accessories menu. You can
click-n-drag that too if you like. However, you might want to install something else.



Editors are somewhat personal things. I like FeatherPad okay, but I prefer Geany.
You can use the "System Tools" -> "Muon Package Manager" to install stuff, however
Geany isn't listed. But it can be installed via `apt`.

	sudo apt install geany

You can click-n-drag it from the "Start Menu" -> "Programming" to the Menu Bar.

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
