# flask-js-mysql-crud
Simple Application using Flask, JavaScript and MySQL 

### Project Strcuture

```
├── Dockerfile
├── README.md
├── app.py
├── init.sql
├── k8s
│   ├── flask-deployment.yaml
│   ├── flask-service.yaml
│   ├── mysql-configmap.yaml
│   ├── mysql-deployment.yaml
│   └── mysql-service.yaml
├── mysql
│   └── Dockerfile
├── requirements.txt
├── static
│   ├── script.js
│   └── style.css
└── templates
    └── index.html
```

### Sample Run on Local Minikube

Building Docker Images 
```
docker build . -t octopent/flask-js-app:latest
docker build . -t octopnet/flask-js-app-mysql-db:latest
```
Starting Minikube Cluster and installing GUI 
```
minikube start
minikube dashboard
```
Applying yaml manifests to the cluster
```
kubectl apply -f k8s/ --recursive
```
Exposing flask-app service to be accessed on browser 
```
minikube service flask --url
```
