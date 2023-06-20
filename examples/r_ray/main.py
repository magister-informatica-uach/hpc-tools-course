import subprocess
import ray

@ray.remote(num_cpus=1)
def helper_function(id):
    result = subprocess.call(f"Rscript hello_world.r {id}", shell=True)
    return result

ray.init()
ray.get([helper_function.remote(k) for k in range(10)])
