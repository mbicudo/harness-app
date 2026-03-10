#!/usr/bin/env bash
# Publish harness-app image to Docker Hub.
# Usage: DOCKERHUB_USER=yourusername ./scripts/publish-dockerhub.sh

set -e

REPO="${DOCKERHUB_USER:?Set DOCKERHUB_USER (e.g. export DOCKERHUB_USER=myuser)}/harness-app"
TAG="${TAG:-latest}"

echo "Building image..."
docker build -t harness-app:"$TAG" .

echo "Tagging as $REPO:$TAG..."
docker tag harness-app:"$TAG" "$REPO:$TAG"

echo "Pushing to Docker Hub..."
docker push "$REPO:$TAG"

echo "Done. Image: $REPO:$TAG"
