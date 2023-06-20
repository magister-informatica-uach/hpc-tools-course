from collections import Counter
import socket
import time
import ray


@ray.remote
def get_ip():
    time.sleep(0.1)
    return socket.gethostbyname(socket.gethostname())


if __name__ == "__main__":

    ray.init()
    print(f"This cluster consists of {len(ray.nodes())} nodes in total {ray.cluster_resources()['CPU']} CPU resources in total")

    object_ids = [get_ip.remote() for _ in range(100)]
    ip_addresses = ray.get(object_ids)

    print('Tasks executed')
    for ip_address, num_tasks in Counter(ip_addresses).items():
        print(f'    {num_tasks} tasks on {ip_address}')
