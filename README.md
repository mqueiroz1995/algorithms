# :computer: Algorithms

This repository contains data structures and algorithms in Python. 

## Tests

Tests were implemented using [unittest](https://docs.python.org/2/library/unittest.html), a Python Unit Testing framework based in JUnit.

To run all the tests, execute:

```batch
python -m unittest discover data_structures.tests -p "*Test.py"
```

To run a specific test execute:

```batch
python -m unittest data_structures.tests.TEST_FILE
```

If you want coverage you can use the same commands above, but replacing `python` with `coverage run`. Coverage analysis is done by using [Coverage.py](https://coverage.readthedocs.io/).

If you want to run mutation tests, you can use [mutpy](https://github.com/mutpy/mutpy) by executing the following command:

```batch
python MUTPY_PATH\mut.py ^
--target data_structures.src ^
--unit-test data_structures.tests ^
--report-html .test_runner ^
--coverage
```
