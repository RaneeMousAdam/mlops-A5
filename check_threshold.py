import mlflow
import sys

mlflow.set_tracking_uri("mlruns")

with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

run = mlflow.get_run(run_id)
accuracy = run.data.metrics["accuracy"]

print(f"Accuracy: {accuracy}")

if accuracy < 0.85:
    print("*_*Model failed")
    sys.exit(1)
else:
    print("*~*Model passed")