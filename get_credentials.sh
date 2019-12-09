gcloud iam service-accounts keys create credentials.json --iam-account project-owner@newsquiz.iam.gserviceaccount.com
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/credentials.json"
echo $GOOGLE_APPLICATION_CREDENTIALS
