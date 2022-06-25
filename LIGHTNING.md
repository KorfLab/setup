Lightning
=========

This document is about the Korflab high performance workstation: lightning.

## Why ##

lightning is designed to run AlphaFold and other CPU/GPU intensive tasks. There
is another lab computer, spitfire, that you might want to use instead. spitfire
has more RAM and more CPUs but lightning has faster CPUs. lightning is
appropriate for single-thread tasks that can't be paralleized and GPU computing,
such as AlphaFold.

## Lightning is ##

+ lightning.genomecenter.ucdavis.edu
+ CPU: 2 AMD Ryzen 7 5800X 8-Core Processor
+ GPU: nVidia 3090
+ RAM: 128G
+ Storage
	+ NVME:  
		+ 4 TB
		+ /dev/nvme0n1p2
		+ For AlphaFold databases only?
		+ Seems this is the only storage available
	

## Lightning is NOT ##

+ NOT part of the campus HPC
+ NOT connected to shared file systesms
+ NOT administered by Mike Lewis
+ NOT backed up
+ NOT running slurm
+ NOT for novice users

## How To ##

+ If you want an account on lightning, you must ask Ian
+ Create project directories on _path_to_HDD_
+ Do not modify anything under _af_path_
+ Check #lightning on slack to see who is running what and when

