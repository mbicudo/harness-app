"""Simple Flask web app for Kubernetes deployment."""
import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Home page."""
    return {"message": "This is my app content API response", "status": "ok"}


@app.route("/health")
def health():
    """Health check endpoint for Kubernetes probes."""
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
