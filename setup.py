from setuptools import setup

setup(
    name='bounded_pool_executor',
    version='0.0.1',
    description='Bounded Process&Thread Pool Executor',
    url='http://github.com/mowshon/bounded_pool_executor',
    keywords='concurrent futures ProcessPoolExecutor ThreadPoolExecutor Semaphore memory leak',
    author='Mowshon',
    author_email='mowshon@yandex.ru',
    license='MIT',
    packages=['bounded_pool_executor'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)
