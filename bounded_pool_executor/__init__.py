import multiprocessing
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import threading


class _BoundedPoolExecutor:

    semaphore = None

    def acquire(self):
        self.semaphore.acquire()

    def release(self, fn):
        self.semaphore.release()

    def submit(self, fn, *args, **kwargs):
        self.acquire()
        future = super().submit(fn, *args, **kwargs)
        future.add_done_callback(self.release)

        return future


class BoundedProcessPoolExecutor(_BoundedPoolExecutor, ProcessPoolExecutor):

    def __init__(self, max_workers=None):
        super().__init__(max_workers)
        self.semaphore = multiprocessing.BoundedSemaphore(max_workers)


class BoundedThreadPoolExecutor(_BoundedPoolExecutor, ThreadPoolExecutor):

    def __init__(self, max_workers=None):
        super().__init__(max_workers)
        self.semaphore = threading.BoundedSemaphore(max_workers)
