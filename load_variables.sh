#!/bin/bash

if [ -z "$TORNADOVM_MLOPS_ROOT" ]; then
	export TORNADOVM_MLOPS_ROOT=$PWD
	echo "The root environmental variable of the repository is set."
else
	echo "Using $TORNADOVM_MLOPS_ROOT as the root environmental variable."
fi
