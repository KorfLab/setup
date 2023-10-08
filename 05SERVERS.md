Servers
=======

How to connect to the various servers.


Manifest
--------

| Computer  | RAM  | Cores | Notes
|:----------|:----:|:-----:|:-------------------
| spitfire  | 256G |   64  | shared general use
| lightning | 128G |   16  | private AlphaFold
| soon...   | 2TB  |  128  | shared general use


spitfire
--------

spitfire is connected the the LSCC0 cluster. It is used for general computing
needs.

+ spitfire.genomecenter.ucdavis.edu
+ CPU: 4 AMD Opteron 6380 16-Core Processor
+ RAM: 256G
+ Storage: LSCC0 network storage /share/korflab


lightning
---------

lightning is an isolated workstation designed to run AlphaFold and other
CPU/GPU intensive tasks. It has fewer CPUs than spitfire, but each one is much
faster. It is therefore useful for single-CPU-intensive tasks.

+ lightning.genomecenter.ucdavis.edu
+ CPU: 2 AMD Ryzen 7 5800X 8-Core Processor
+ GPU: nVidia 3090
+ RAM: 128G
+ Storage: 4TB NVME (most used for AlphaFold)

### Lightning is NOT

+ NOT part of the campus HPC (don't ask them for help)
+ NOT connected to shared file systesms
+ NOT backed up
+ NOT running slurm
+ NOT for novice users

