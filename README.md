# :computer: Algorithms

This repository contains data structures and algorithms in Python. 

## Tests

Tests were implemented using [unittest](https://docs.python.org/2/library/unittest.html), a Python Unit Testing framework based in JUnit.

To run all the tests, from `/data_structures` execute the following command:

```batch
python3 -m unittest discover tests -p "*Test.py"
```

To run a specific test execute:

```batch
python3 -m unittest tests.TEST_MODULE
```

If you want coverage you can use the same commands above, but replacing `python3` with `coverage run`. Coverage analysis is done by using [Coverage.py](https://coverage.readthedocs.io/).

If you want to run mutation tests, you can use [mutpy](https://github.com/mutpy/mutpy) by executing the following command:

```batch
mut.py \
--target src \
--unit-test tests \
--timeout-factor 1 \
--coverage \
--colored-output
```

An easier way to executing both coverage and mutation tests is running `./test_runnes.sh`.
