# Parallelexec 

#### Parallelexec is a Python module that provides decorators and methods to easily run multiple functions concurrently.

## Installation
#### Use pip
````commandline
pip install parallelexec
````
## Usage 
````python
from parallelexec import ParallelExec

@ParallelExec.thread(join=True)
def fun():
    ...
````

#### Better yet, check `examples/`
## License 
#### This is under The [Public Domain](/UNLICENSE)