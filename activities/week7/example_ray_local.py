import sys
from functools import partial
from timeit import timeit
import numpy as np
import ray


def slow_function(id, data_length):
    np.random.seed(id)
    data = np.random.randn(data_length)
    return np.mean((data-np.mean(data))**2)

# https://docs.ray.io/en/latest/ray-core/tasks.html#ray-remote-functions
@ray.remote(num_cpus=1)
def slow_function_ray(id, data_length):
    np.random.seed(id)
    data = np.random.randn(data_length)
    return np.mean((data-np.mean(data))**2)


if __name__ == "__main__":
    assert len(sys.argv) == 3, "Llamar como python example_joblib n_data, n_files"
    n_data, n_files = [int(arg) for arg in sys.argv[1:]]
    repetitions = 10
    profile = partial(timeit, globals=globals(), number=repetitions)
    slow_function_partial = partial(slow_function, data_length=n_data)
    # Sequential computation
    result_seq = [slow_function_partial(k) for k in range(n_files)]
    time_seq = profile('[slow_function_partial(k) for k in range(n_files)]')
    # Parallel computation
    ray.init()
    # https://docs.ray.io/en/latest/ray-core/scheduling/index.html#ray-scheduling
    ray_fn_parallel = slow_function_ray.options(scheduling_strategy="DEFAULT")
    result_par = ray.get([ray_fn_parallel.remote(k, n_data) for k in range(n_files)])
    time_par = profile("ray.get([ray_fn_parallel.remote(k, n_data) for k in range(n_files)])")
    # Reporting
    print("Sequential (seq) vs Ray (par)")
    print(f"Same result?: {np.allclose(result_seq, result_par)}")
    print(f"Time seq: {time_seq/repetitions:0.4f} s")
    print(f"Time par: {time_par/repetitions:0.4f} s")
    print(f"Speed up: {time_seq/time_par}")
