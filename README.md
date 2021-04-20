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

