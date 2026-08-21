# Kubernetes practice manifests

These manifests run the Flask feedback app and MySQL in the `flask-feedback`
namespace. They demonstrate a Namespace, Deployments, Services, ConfigMap,
Secret, PersistentVolume (PV), and PersistentVolumeClaim (PVC).

## 1. Build the Flask image

For Minikube, point Docker at Minikube's Docker daemon before building:

```bash
eval $(minikube docker-env)
docker build -t flask-feedback-app:latest .
```

For Kind, load a locally built image instead:

```bash
docker build -t flask-feedback-app:latest .
kind load docker-image flask-feedback-app:latest
```

## 2. Apply the resources

Run these from the repository root, in this order:

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/pv.yaml
kubectl apply -f k8s/pvc.yaml
kubectl apply -f k8s/mysql.yaml
kubectl apply -f k8s/flask.yaml
kubectl get all -n flask-feedback
```

The Flask app keeps retrying MySQL while the database starts. Wait until both
pods are ready:

```bash
kubectl get pods -n flask-feedback -w
```

## 3. Open the app

For any local cluster, this is the most portable method:

```bash
kubectl port-forward -n flask-feedback service/flask-app 5000:5000
```

Then visit `http://localhost:5000`.

The Flask image name is `flask-feedback-app:latest`; change it in `flask.yaml`
if you push it to a registry. `pv.yaml` deliberately uses `hostPath` and is only
for learning on a single-node cluster. The sample Secret has development-only
passwords—do not commit real credentials.
