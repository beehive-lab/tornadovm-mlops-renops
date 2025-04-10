#!/bin/bash
docker compose -f $TORNADOVM_MLOPS_ROOT/mlops/docker-compose.yml --env-file $TORNADOVM_MLOPS_ROOT/mlops/config.env up --build -d
