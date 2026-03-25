FROM python:3.10-slim
ARG RUN_ID
RUN echo "Packaging model for Run ID: ${RUN_ID}"
RUN echo "Simulating: mlflow artifacts download --run-id ${RUN_ID}"
WORKDIR /app
COPY train.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV MODEL_RUN_ID=${RUN_ID}
CMD ["echo", "Model container ready"]