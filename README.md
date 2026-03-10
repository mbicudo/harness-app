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

## Publish to Docker Hub

1. [Create a Docker Hub account](https://hub.docker.com/signup) and create a repository (e.g. `harness-app`).

2. Log in and push (replace `YOUR_DOCKERHUB_USER` with your username):

   ```bash
   docker login
   docker build -t harness-app:latest .
   docker tag harness-app:latest YOUR_DOCKERHUB_USER/harness-app:latest
   docker push YOUR_DOCKERHUB_USER/harness-app:latest
   ```

   Or use the script: `DOCKERHUB_USER=YOUR_DOCKERHUB_USER ./scripts/publish-dockerhub.sh`

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
