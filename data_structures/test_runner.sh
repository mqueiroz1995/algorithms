#!/bin/bash
rm -R .test_runner
mkdir .test_runner

# tests + coverage
coverage run -m unittest tests
coverage report -m
coverage html -d .test_runner/coverage

# mutation testing
mut.py \
--target src \
--unit-test tests \
--timeout-factor 1 \
--coverage \
--colored-output

