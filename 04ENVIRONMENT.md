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

To install a local CLI environment, see the latest MCB185 course materials.


Hive
----

To use the UCD cluster, get an account on Hive. Go to https://hippo.ucdavis.edu
and select the Hive cluster. Your sponsor is ikorfgrp.

Each user has a home directory with enough space for their git repos and conda
environments. Don't use your home directory for large data files. We have
shared storage at `/quobyte/ikorfgrp`.


Conda
-----

You should use Conda to install most CLI software both on your personal
computers and your Hive account.

To install Conda on your personal computer: https://conda-forge.org/miniforge

Conda is already provided on Hive via `module load conda`.

