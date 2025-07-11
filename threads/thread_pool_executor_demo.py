import time
from concurrent.futures import ThreadPoolExecutor as TP

def task():
    n = 0
    for x in range(10_000_000):
        n+=x
    return n

with TP() as pool:
    start = time.perf_counter()
    results = [pool.submit(task) for _ in range(6)]

print("Elapsed time:", time.perf_counter() - start)
print ([r.result() for r in results])

