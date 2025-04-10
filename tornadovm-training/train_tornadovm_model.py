import os
import pandas as pd
import argparse
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn


def load_dummy_data():
    dataset_path = os.path.join(os.environ["TORNADOVM_TRAINING_PATH"], "tornadovm_training_dataset.csv")
    
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"CSV file not found at: {dataset_path}")
    
    df = pd.read_csv(dataset_path)
    return df


def train_model(X_train, y_train, X_val, y_val, classifier_id):
    with mlflow.start_run(run_name=f"DummyClassifier_C{classifier_id}"):
        mlflow.set_tag("model", f"DummyClassifier_C{classifier_id}")

        model = DummyClassifier(strategy="most_frequent")
        model.fit(X_train, y_train)

        y_pred = model.predict(X_val)
        acc = accuracy_score(y_val, y_pred)

        mlflow.log_param("classifier_id", classifier_id)
        mlflow.log_param("strategy", "most_frequent")
        mlflow.log_metric("accuracy", acc)

        mlflow.sklearn.log_model(model, artifact_path=f"model_classifier_{classifier_id}")

        print(f"[Classifier {classifier_id}] Dummy Accuracy: {acc:.4f}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--classifier", type=int, choices=[1, 2, 3],
                        help="Classifier ID (1=IGPU vs CPU, 2=GPU vs CPU, 3=FPGA vs CPU)")
    parser.add_argument("--all", action="store_true", help="Train all classifiers")
    args = parser.parse_args()

    mlflow.set_tracking_uri("http://127.0.0.1:5001")
    mlflow.set_experiment("task_classifier")

    classifier_ids = [1, 2, 3] if args.all or args.classifier is None else [args.classifier]

    df = load_dummy_data()
    X = df.drop("target_class", axis=1)
    y = df["target_class"]

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    for cid in classifier_ids:
        train_model(X_train, y_train, X_val, y_val, cid)


if __name__ == "__main__":
    main()

