#!/bin/sh
################# Begin Slurm header ####################
#
# Give job a reasonable name
#SBATCH --job-name=real-world_covertype10
#
# Request number of nodes for job
#SBATCH --ntasks=1
#
# Maximum run time of job (hh:mm:ss)
#SBATCH --time=72:00:00
#
#SBATCH -p single
#
#SBATCH --mail-type=ALL
#
#SBATCH --mail-user=nadinegabrek@web.de
#
################ End Slurm header ######################

cd ..
cd ..
cd ..

python -m experiments.real-world.covertype.real-world_covertype10
