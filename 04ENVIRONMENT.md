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
will exceed your personal computer and you will need to use a cluster, which
means a Unix-like CLI.

To install a local CLI environment, you can:

- Buy a Mac
- Install Linux on an older PC
- Install VirtualBox and run some Linux distro (e.g. Lubuntu)
- Install Cygwin
- Use the Linux environment in Windows


Hive
----

To use the UCD cluster, get an account on Hive. Go to https://hippo.ucdavis.edu
and select the Hive cluster. Your sponsor is ikorfgrp.

Each user has a home directory with 20G. This is backed up. 20G is probably
enough for your needs, but if not, create a home-away-from-home in the shared
space `/quobyte/ikorfgrp/home`. To do that, you will need to redefine `$HOME`
to point to the new location. Note that nothing in `/quobyte/ikorfgrp` is
backed up.

Conda
-----

You should use Conda to install most CLI software both on your personal
computers and your Hive account.

To install Conda on your personal computer: https://conda-forge.org/miniforge

Conda is already provided on Hive via `module load conda`. You should probably
add this to your `.bash_profile`.

