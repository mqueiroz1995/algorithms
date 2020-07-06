#!/bin/bash

echo $@

# mutation testing
mut.py \
    --target src \
    --unit-test tests \
    --mutation-number $@ \
    --show-mutants \
    --colored-output