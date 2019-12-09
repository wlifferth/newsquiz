from google.cloud import firestore

def write_to_cloud(headline):
    global firestore_client
    if firestore_client is None:
        firestore_client = firestore.Client()

    headline_vars = vars(headline)
    headline_vars['datetime_published'] = headline_vars['datetime_published'].strftime("%m/%d/%Y, %H:%M:%S")
    doc_ref = firestore_client.collection('headline').document(headline_vars['uid'])
    print(doc_ref.set(headline_vars))
