# tornadovm-mlops-renops
This repository shows how a ML model for TornadoVM can be trained using MLOPs and use the RENOPS scheduler to schedule the training process.

# 1. Clone the repository
```bash
git clone https://github.com/stratika/tornadovm-mlops-renops.git
```

# 2. Move into the project directory
```bash
cd tornadovm-mlops-renops
```

# 3. Load environment variables
```bash
source load_variables.sh
```

# 4. Start the MLOps container
```bash
./mlops/start_mlops_container.sh
```

### i. You can open the MLFlow window to see any ML training tasks
```bash
google-chrome http://127.0.0.1:5001/
```

# 5. Run the training of the TornadoVM model with RENOPS

### i. The first time install the Python dependencies for the training
```bash
./tornadovm-training/install.sh
```

### ii. Configure the script with the required RENOPS arguments and train the model
```bash
./tornadovm-training/run_renops_tornadovm.sh
2025-04-10 12:44:45.031 | INFO     | renops.main:run:36 - RUNNING RENOPS SCHEDULER...
/home/thanos/repositories/TANGO/MLOPs/tornadovm-mlops-renops/tornadovm-training/.venv/lib/python3.11/site-packages/renops/main.py:117: DeprecationWarning: '--optimise-price' is deprecated and will be removed in future versions. Use '--optimise price' instead.
  warnings.warn(
2025-04-10 12:44:45.031 | INFO     | renops.main:run:154 - Location specified, shifting in time...
2025-04-10 12:44:45.359 | WARNING  | renops.geolocation:_get_location_params:34 - Location is set to auto, IP will be used to detect location! found: Athens, GR
2025-04-10 12:44:46.291 | INFO     | renops.scheduler:run:193 - Task has to be finished by: 2025-11-04 12:44:46
2025-04-10 12:44:46.291 | INFO     | renops.scheduler:run:201 - No renewable window whitin a given deadline!
2025-04-10 12:44:46.291 | INFO     | renops.scheduler:_print_info_for_instant_execution:177 - Current energy price is: 16.66 EUR/MWh
2025-04-10 12:44:46.291 | INFO     | renops.scheduler:run:247 - Executing action now at 2025-04-10 12:44:46.291761
2025-04-10 12:44:46.291 | INFO     | renops.scheduler:run:249 - ----------------------------------------------------
2025/04/10 12:44:47 INFO mlflow.tracking.fluent: Experiment with name 'task_classifier' does not exist. Creating a new experiment.
2025/04/10 12:44:49 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.
[Classifier 1] Accuracy: 0.5882, ROC AUC: 0.9167
🏃 View run ExtraTreesClassifier_C1 at: http://127.0.0.1:5001/#/experiments/1/runs/cb46265d74504e1684943715395e0358
🧪 View experiment at: http://127.0.0.1:5001/#/experiments/1
2025/04/10 12:44:51 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.
[Classifier 2] Accuracy: 0.9444, ROC AUC: 1.0000
🏃 View run ExtraTreesClassifier_C2 at: http://127.0.0.1:5001/#/experiments/1/runs/0b03ba84df3748f39367dfd82bb2668a
🧪 View experiment at: http://127.0.0.1:5001/#/experiments/1
2025/04/10 12:44:52 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.
[Classifier 3] Accuracy: 0.9444, ROC AUC: 0.9250
🏃 View run ExtraTreesClassifier_C3 at: http://127.0.0.1:5001/#/experiments/1/runs/464146b4a3274ed2bcff9b7c5c55f609
🧪 View experiment at: http://127.0.0.1:5001/#/experiments/1
```

### iii. Observe the MLFlow window and see the tracked information for the trained model
![Screenshot from 2025-04-10 12-47-37](https://github.com/user-attachments/assets/8163595a-9327-423f-a440-06c2df7e1f6a)

![Screenshot from 2025-04-10 12-48-09](https://github.com/user-attachments/assets/7aac0053-c00d-41a7-95fd-2fb91c6cdb3c)

# 6. Stop the MLOps container
```bash
./mlops/start_mlops_container.sh
```
