from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='bounded_pool_executor',
    version='0.0.3',
    description='Bounded Process&Thread Pool Executor',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
