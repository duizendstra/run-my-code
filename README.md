# run-my-code
A journey through the Google Cloud Platform

create the project
```
export PROJECT_ID=run-my-code-$RANDOM-$RANDOM
gcloud projects create $PROJECT_ID  --name="Run my code" 
gcloud projects describe $PROJECT_ID
```

```
gcloud config set project $PROJECT_ID
```

```
BILLING_ACCOUNT_ID=$(gcloud beta billing accounts list --format="value(name)")
gcloud beta billing projects link $PROJECT_ID  --billing-account=$BILLING_ACCOUNT_ID
```


```
gcloud services enable compute.googleapis.com
```

```
gcloud services list
```

```
gcloud compute images list
```

```
export REGION=europe-west3
gcloud config set compute/region $REGION
```

```
export ZONE=europe-west3-a
gcloud config set compute/zone $ZONE
```

```
gcloud compute instances create hello-deventer --image-family=debian-10 --image-project=debian-cloud --tags http-server,https-server
```

```
gcloud compute ssh hello-deventer
sudo apt update
sudo apt install git
git --version
git clone https://github.com/duizendstra/run-my-code.git
```


### Docker
docker run busybox date
gcloud auth configure-docker

gcloud services enable cloudbuild.googleapis.com
gcloud builds submit --tag gcr.io/$PROJECT_ID/hello-deventer:latest

### Google Kubernetes Engine
gcloud services enable container.googleapis.com
gcloud container clusters create hello-deventer --num-nodes=1
gcloud container clusters get-credentials hello-deventer
kubectl create deployment hello-deventer --image=gcr.io/$PROJECT_ID/hello-deventer:latest
kubectl expose deployment hello-deventer --type LoadBalancer --port 80 --target-port 5000
kubectl get pods
kubectl get service hello-deventer
kubectl delete service hello-deventer
gcloud container clusters delete hello-deventer
