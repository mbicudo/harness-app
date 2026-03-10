# Harness App

A simple Python (Flask) web app ready for Kubernetes deployment.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:8080

## Build and run with Docker

```bash
docker build -t harness-app:latest .
docker run -p 8080:8080 harness-app:latest
```

## Deploy on Kubernetes

1. Build the image. For **Minikube**: `eval $(minikube docker-env)` then build so the cluster can use the image. For a **remote cluster**, push to your registry and set the image in `k8s/deployment.yaml`.

   ```bash
   docker build -t harness-app:latest .
   # For a real cluster, tag and push, then set image in k8s/deployment.yaml:
   # docker tag harness-app:latest your-registry/harness-app:latest
   # docker push your-registry/harness-app:latest
   ```

2. Apply the manifests:

   ```bash
   kubectl apply -f k8s/
   ```

3. Expose the service (optional, for access from outside the cluster):

   ```bash
   kubectl port-forward svc/harness-app 8080:80
   ```

   Then open http://localhost:8080

## Endpoints

- `GET /` — Returns a JSON greeting.
- `GET /health` — Health check (used by Kubernetes liveness/readiness probes).
