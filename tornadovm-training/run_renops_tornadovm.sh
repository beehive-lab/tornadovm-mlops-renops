#!/bin/bash
export TORNADOVM_TRAINING_PATH=$TORNADOVM_MLOPS_ROOT/tornadovm-training
source $TORNADOVM_TRAINING_PATH/.venv/bin/activate
export RENOPSAPI_KEY="TANGO_DEMO_KEY"

renops-scheduler $TORNADOVM_TRAINING_PATH/train_tornadovm_model.py -la -r 30 -d 24 -v --optimise price
deactivate
