#!/bin/bash

# Partition and GPU
#SBATCH -p gpu
#SBATCH --gres=gpu:A100:1

# Identification
#SBATCH -J JAX-bench-%j
#SBATCH -o JAX-bench-%j.log

pwd
date
echo "Running jax benchmark"
srun --container-name=jax python3 benchmark.py 10000 32
