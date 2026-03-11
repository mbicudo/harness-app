# Harness App

A simple Python (Flask) web app ready for Kubernetes deployment.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:8080

## Run tests

```bash
pip install -r requirements-dev.txt
python3 -m pytest
```

For CI (JUnit XML report): `python3 -m pytest --junitxml=test-results.xml`

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

**Prerequisites:** `kubectl` installed and a cluster (Minikube, Kind, GKE, EKS, AKS, etc.).

### Option A: Using the image from Docker Hub

1. **Set the image** in `k8s/deployment.yaml` to your Docker Hub image:

   ```yaml
   image: YOUR_DOCKERHUB_USER/harness-app:latest
   imagePullPolicy: Always
   ```

2. **Apply the manifests:**

   ```bash
   kubectl apply -f k8s/
   ```

3. **Check that the app is running:**

   ```bash
   kubectl get pods -l app=harness-app
   kubectl get svc harness-app
   ```

4. **Access the app** (choose one):

   - **Port-forward** (quick test from your machine):
     ```bash
     kubectl port-forward svc/harness-app 8080:80
     ```
     Then open http://localhost:8080

   - **LoadBalancer** (for cloud clusters): change `type: ClusterIP` to `type: LoadBalancer` in `k8s/service.yaml`, then `kubectl get svc harness-app` to get the external IP.

### Option B: Using a local image (e.g. Minikube)

1. Point your shell at the cluster’s Docker so the image is built inside the cluster:
   ```bash
   eval $(minikube docker-env)   # Minikube
   # or: kind export docker-env  # Kind
   docker build -t harness-app:latest .
   ```

2. In `k8s/deployment.yaml` keep:
   ```yaml
   image: harness-app:latest
   imagePullPolicy: IfNotPresent
   ```

3. Deploy and access as in Option A (steps 2–4).

## Endpoints

- `GET /` — Returns a JSON greeting.
- `GET /health` — Health check (used by Kubernetes liveness/readiness probes).
