#!/bin/bash

#SBATCH --account=ds2002
#SBATCH --job-name=bookarray
#SBATCH --output=jobarray-book-%A_%a.out
#SBATCH --error=jobarray-book-%A_%a.err
#SBATCH --time=00:10:00
#SBATCH --partition=standard
#SBATCH --mem=8G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --array=1-5

cd /scratch/$USER/ds2002-jobruns/text-analysis

module load miniforge
source activate ds2002

INPUT="book-${SLURM_ARRAY_TASK_ID}.txt"
OUTPUT="results-${SLURM_ARRAY_TASK_ID}.csv"

python ~/ds2002-course/labs/07-hpc/process-book.py "$INPUT" "$OUTPUT"