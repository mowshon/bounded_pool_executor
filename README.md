# Bounded Process&Thread Pool Executor
BoundedSemaphore for [ProcessPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor) & [ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor) from [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)

# What is the main problem?
If you use the standard module “**concurrent.futures**” and want to simultaneously process several million data, then a queue of workers will take up all the free memory.

If the script is run on a weak VPS, this will lead to a **memory leak**.



## BoundedProcessPoolExecutor VS ProcessPoolExecutor

# BoundedProcessPoolExecutor
**BoundedProcessPoolExecutor** will put a new worker in queue only when another worker has finished his work.

```python
from bounded_pool_executor import BoundedProcessPoolExecutor
from time import sleep
from random import randint

def do_job(num):
    sleep_sec = randint(1, 10)
    print('value: %d, sleep: %d sec.' % (num, sleep_sec))
    sleep(sleep_sec)

with BoundedProcessPoolExecutor(max_workers=5) as worker:
    for num in range(10000):
        print('#%d Worker initialization' % num)
        worker.submit(do_job, num)

```
### Result:
![BoundedProcessPoolExecutor](https://python-scripts.com/wp-content/uploads/2018/12/bounded.gif)

# Classic concurrent.futures.ProcessPoolExecutor
**ProcessPoolExecutor** inserts all workers into the queue and expects tasks to be performed as the new worker is released, depending on the value of `max_workers`.

```python
import concurrent.futures
from time import sleep
from random import randint

def do_job(num):
    sleep_sec = randint(1, 3)
    print('value: %d, sleep: %d sec.' % (num, sleep_sec))
    sleep(sleep_sec)

with concurrent.futures.ProcessPoolExecutor(max_workers=5) as worker:
    for num in range(100000):
        print('#%d Worker initialization' % num)
        worker.submit(do_job, num)
```

### Result:
![concurrent.futures.ProcessPoolExecutor](https://python-scripts.com/wp-content/uploads/2018/12/future-ProcessPoolExecutor.gif)
