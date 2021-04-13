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