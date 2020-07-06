#!/bin/bash
rm -R .test_runner
mkdir .test_runner

# tests + coverage
coverage run -m unittest discover tests -p "*Test.py"
coverage report

# mutation testing
mut.py \
--target src \
--unit-test tests \
--timeout-factor 1 \
--coverage \
--colored-output

