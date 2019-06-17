#!/bin/bash

echo "Testing the environment setup..."

echo "Installed python:"
echo `python --version`

echo "Python path:"
echo `python -c "import sys; print(sys.path)"`

echo "Installed packages:"
echo `conda list`