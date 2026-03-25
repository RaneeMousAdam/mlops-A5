import os
import sys
import mlflow

with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

print(f"Checking Run ID: {run_id}")

tracking_uri = os.environ.get("MLFLOW_TRACKING_URI", "file:./mlruns")
mlflow.set_tracking_uri(tracking_uri)

try:
    client = mlflow.tracking.MlflowClient()
    run = client.get_run(run_id)
except Exception as e:
    print(f"Could not retrieve run: {e}")
    sys.exit(1)

accuracy = run.data.metrics.get("accuracy")
if accuracy is None:
    print("ERROR: accuracy metric not found!")
    sys.exit(1)

print(f"Model Accuracy: {accuracy}")

if accuracy < 0.85:
    print(f"FAILED: {accuracy:.4f} is below 0.85. Halting.")
    sys.exit(1)
else:
    print(f"PASSED: {accuracy:.4f} meets threshold. Ready for deployment.")