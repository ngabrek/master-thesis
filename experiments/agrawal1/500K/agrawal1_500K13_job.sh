#!/bin/sh
################# Begin Slurm header ####################
#
# Give job a reasonable name
#SBATCH --job-name=agrawal1_500K13
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

python -m experiments.agrawal1.500K.agrawal1_500K13