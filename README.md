# TornadoVM-MLOps-RENOPS

This repository shows how a ML model for TornadoVM can be trained using: 
- MLOPs to track the training properties.
- [RENOPS scheduler](https://pypi.org/project/renops-scheduler/) to schedule the training process when cost is lower.

## 1. Clone the repository
```bash
git clone https://github.com/stratika/tornadovm-mlops-renops.git
```

## 2. Move into the project directory
```bash
cd tornadovm-mlops-renops
```

## 3. Load environment variables
```bash
source load_variables.sh
```

## 4. Start the MLOps container
```bash
./mlops/start_mlops_container.sh
```

### i. You can open the MLFlow window to see any ML training tasks
```bash
google-chrome http://127.0.0.1:5001/
```

## 5. Run the training of the TornadoVM model with RENOPS

### i. The first time install the Python dependencies for the training
```bash
./tornadovm-training/install.sh
```

### ii. Configure the script with the required RENOPS arguments and train the model
```bash
./tornadovm-training/run_renops_tornadovm.sh 
2025-04-10 15:33:20.444 | INFO     | renops.main:run:36 - RUNNING RENOPS SCHEDULER...
2025-04-10 15:33:20.444 | INFO     | renops.main:run:154 - Location specified, shifting in time...
2025-04-10 15:33:20.717 | WARNING  | renops.geolocation:_get_location_params:34 - Location is set to auto, IP will be used to detect location! found: Athens, GR
2025-04-10 15:33:21.545 | INFO     | renops.scheduler:run:193 - Task has to be finished by: 2025-11-04 15:33:21
2025-04-10 15:33:21.545 | INFO     | renops.scheduler:run:201 - No renewable window whitin a given deadline!
2025-04-10 15:33:21.545 | INFO     | renops.scheduler:_print_info_for_instant_execution:177 - Current energy price is: 9.64 EUR/MWh
2025-04-10 15:33:21.545 | INFO     | renops.scheduler:run:247 - Executing action now at 2025-04-10 15:33:21.545432
2025-04-10 15:33:21.545 | INFO     | renops.scheduler:run:249 - ----------------------------------------------------
2025/04/10 15:33:24 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.
[Classifier 1] Dummy Accuracy: 0.0000
🏃 View run DummyClassifier_C1 at: http://127.0.0.1:5001/#/experiments/1/runs/0e2e67bfd0ce4299b415ee845d69bbf2
🧪 View experiment at: http://127.0.0.1:5001/#/experiments/1
2025/04/10 15:33:26 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.
[Classifier 2] Dummy Accuracy: 0.0000
🏃 View run DummyClassifier_C2 at: http://127.0.0.1:5001/#/experiments/1/runs/29dd92dc14604a25bf2e68c3bdca9c12
🧪 View experiment at: http://127.0.0.1:5001/#/experiments/1
2025/04/10 15:33:28 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.
[Classifier 3] Dummy Accuracy: 0.0000
🏃 View run DummyClassifier_C3 at: http://127.0.0.1:5001/#/experiments/1/runs/fd2fe292aa87462383a1d7aa326c6dd8
🧪 View experiment at: http://127.0.0.1:5001/#/experiments/1
```

### iii. Observe the MLFlow window and see the tracked information for the trained model
![Screenshot from 2025-04-10 15-40-50](https://github.com/user-attachments/assets/3f7377fa-2af4-4a3f-96b5-388fd4457cd8)

![Screenshot from 2025-04-10 15-41-17](https://github.com/user-attachments/assets/2e153b9a-d2f1-411c-81a3-fc2f6d021f5c)


## 6. Stop the MLOps container
```bash
./mlops/stop_mlops_container.sh
```

# Acknowledgments
This work is funded by the European Union's Horizon Europe programme under grant agreement No 101070052 and the UK Reseach and Innovation Horizon Europe guarantee scheme grant No 10039107 ([TANGO](https://tango-project.eu/)).

## License

This project uses a two-licenses scheme. The `mlops` folder is licensed under the GNU Affero General Public License v3.0. Whereas, the `tornadovm-training` folder is licensed under Apache 2.0.

| Module                         | License                                                                                                                                                                          |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mlops                          | [![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://github.com/beehive-lab/tornadovm-mlops-renops/blob/main/mlops/LICENSE)                    |
| tornadovm-training             | [![License: Apache 2](https://img.shields.io/badge/License-Apache%202.0-red.svg)](https://github.com/beehive-lab/tornadovm-mlops-renops/blob/main/tornadovm-training/LICENSE)    |

