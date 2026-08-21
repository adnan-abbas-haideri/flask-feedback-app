# Kubernetes practice manifests

These manifests run the Flask feedback app and MySQL in the `flask-feedback`
namespace. They demonstrate a Namespace, Deployments, Services, ConfigMap,
Secret, PersistentVolume (PV), and PersistentVolumeClaim (PVC).

## 1. Flask image

The deployment pulls the Flask image from Docker Hub:

```text
adnan313/flask-feedback-app:latest
```

If you push a versioned image in the future (for example, `v1`), update the
tag in `k8s/flask.yaml` before applying the manifests.

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

The Flask image is configured in `flask.yaml`. `pv.yaml` deliberately uses
`hostPath` and is only for learning on a single-node cluster. The sample Secret
has development-only passwords—do not commit real credentials.
