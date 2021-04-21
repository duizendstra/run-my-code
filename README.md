# run-my-code
A journey through the Google Cloud Platform Compute services

### Preperation
This document is part of the repository https://github.com/duizendstra/run-my-code

### Google Cloud Shell
Open the cloud shell at https://ide.cloud.google.com

Open a terminal and clone the repository
```
git clone https://github.com/duizendstra/run-my-code
```

Set the root directory
```
export RUN_MY_CODE_HOME=$HOME/run-my-code
```

### Google Cloud Project

Create the Google Cloud Project
```
export PROJECT_ID=run-my-code-$RANDOM-$RANDOM
gcloud projects create $PROJECT_ID  --name="Run my code" 
gcloud projects describe $PROJECT_ID
gcloud config set project $PROJECT_ID
```
Enable billing
```
BILLING_ACCOUNT_ID=$(gcloud beta billing accounts list --format="value(name)")
gcloud beta billing projects link $PROJECT_ID  --billing-account=$BILLING_ACCOUNT_ID
```

### Compute Engine
Enable the Compoute Engine service and list the images
```
gcloud services enable compute.googleapis.com
gcloud services list
gcloud compute images list
```

Set the region and zone
```
export REGION=europe-west3
gcloud config set compute/region $REGION
export ZONE=europe-west3-a
gcloud config set compute/zone $ZONE
```

Create the firewall rules
```
gcloud compute --project=$PROJECT_ID firewall-rules create default-allow-http \
   --direction=INGRESS --priority=1000 --network=default \
   --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 \
   --target-tags=http-server

gcloud compute --project=$PROJECT_ID firewall-rules create default-allow-https \
   --direction=INGRESS --priority=1000 --network=default \
   --action=ALLOW --rules=tcp:443 --source-ranges=0.0.0.0/0 \
   --target-tags=https-server
```

Create the compute instance
```
gcloud compute instances create hello-deventer \
    --image-family=debian-10 \
    --image-project=debian-cloud \
    --tags http-server,https-server
```

SSH into the instance
```
gcloud compute ssh hello-deventer
```
Install Python and Flask
```
sudo apt update
sudo apt install python3-pip
sudo pip3 install flask gunicorn
``` 
Install Git
```
sudo apt install git
git clone --branch master https://github.com/duizendstra/run-my-code.git
```
Run the application
```
cd ~/run-my-code/google-compute-engine
export FLASK_APP=wsgi.py
export FLASK_ENV=production
sudo gunicorn --workers 4 --bind 0.0.0.0:80 wsgi:app
```

Exit out of the SSH session
```
exit
```

### Build the container
Using local Docker
```
docker run busybox date
gcloud auth configure-docker
```
Using Cloud Build
```
gcloud services enable cloudbuild.googleapis.com
cd $RUN_MY_CODE_HOME/google-kubernetes-engine
gcloud builds submit --tag gcr.io/$PROJECT_ID/hello-deventer:latest
```
### Google Kubernetes Engine

Create the cluster
```
gcloud services enable container.googleapis.com
gcloud container clusters create hello-deventer-gke --num-nodes=1
gcloud container clusters get-credentials hello-deventer-gke
```

Deploy the app  
! change project id in deployment file
```
kubectl apply -f deployment.yaml
kubectl get deployments
kubectl get pods
```

Deploy the service
```
kubectl apply -f service.yaml
kubectl get services
```

Create the deployment
```
kubectl create deployment hello-deventer --image=gcr.io/$PROJECT_ID/hello-deventer:latest
kubectl expose deployment hello-deventer --type LoadBalancer --port 80 --target-port 5000
kubectl get pods
kubectl get service hello-deventer
```
Cleanup
```
kubectl delete service hello-deventer
gcloud container clusters delete hello-deventer-gke
```

### Cloud run

Enable the service
```
gcloud services enable run.googleapis.com
gcloud config set run/platform managed
gcloud config set run/region $REGION
```

Build the container and deploy
```
cd $RUN_MY_CODE_HOME/google-cloud-run
gcloud builds submit --tag gcr.io/$PROJECT_ID/hello-deventer
gcloud run deploy --image gcr.io/$PROJECT_ID/hello-deventer --platform managed
```

### Google App Engine

```
gcloud app create --project=$PROJECT_ID --region=$REGION
cd $RUN_MY_CODE_HOME/google-app-engine
gcloud app deploy
```

### Cloud Functions
```
gcloud services enable cloudfunctions.googleapis.com
```

```
cd $RUN_MY_CODE_HOME/google-cloud-functions
gcloud functions deploy hello-deventer \
   --entry-point hello_deventer \
   --runtime python37 --trigger-http \
   --allow-unauthenticated
```