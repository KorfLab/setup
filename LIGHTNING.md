Lightning
=========

This document is about the Korflab high performance workstation: lightning.

## Why ##

lightning is designed to run AlphaFold and other CPU/GPU intensive tasks. There
is another lab computer, spitfire, that you might want to use instead. Both
machines have 256G RAM and approximately the same aggregate performance. However
lightning has 1/4 of the CPUs and a 24GB GPU. This means that lightning is
appropriate for single-thread tasks that can't be paralleized and GPU computing,
such as AlphaFold.

## Lightning is ##

+ lightning.genomecenter.ucdavis.edu
+ CPU:
+ GPU:
+ RAM: 256G
+ Storage
	+ SSD:
		+ 1 TB
		+ Mount path
		+ Operating system and home directories
	+ HDD:
		+ 2 TB
		+ Mount path
		+ Use for all projects
	+ NVME:  
		+ 4 TB
		+ Mount path
		+ For AlphaFold databases only

## Lightning is NOT ##

+ NOT part of the campus HPC
+ NOT connected to shared file systesms
+ NOT administered by Mike Lewis
+ NOT backed up
+ NOT running slurm
+ NOT for novice users

## How To ##

+ If you want an account on lightning, you must ask
+ Create project directories on _path_to_HDD_
+ Do not modify anything under _af_path_
+ Check #lightning on slack to see who is running what and when

