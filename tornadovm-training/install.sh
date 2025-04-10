#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r $TORNADOVM_MLOPS_ROOT/tornadovm-training/requirements.txt
