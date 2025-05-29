#!/bin/bash
#SBATCH --job-name=example1            # jobs should have unique names
#SBATCH --account=publicgrp            # use publicgrp by default
#SBATCH --partition=low                # use low by default
#SBATCH --output=jobs/example1.stdout  # relative path starts in $HOME
#SBATCH --error=jobs/example1.stderr   # relative path starts in $HOME
#SBATCH --nodes=1                      # generally we request 1
#SBATCH --ntasks-per-node=1            # 1 for simple tasks
#SBATCH --cpus-per-task=1              # depends on job
#SBATCH --mem=1M                       # depends on job
#SBATCH --time=1:05                    # days-hours:min:sec

#--- You will probably do these most of the time ---#
# module load conda
# conda activate something

# Various commands
ls $HOME
ls $HOME | wc
