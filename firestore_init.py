# import firebase_admin
# from firebase_admin import credentials, firestore
# import os
# from dotenv import load_dotenv
# import json

# load_dotenv()

# # cred = credentials.Certificate('./serviceAccount.json')
# cred = os.getenv("CREDS")
# if not cred:
#     raise ValueError('The $CREDS environment variable was not found!')

# # Parse the JSON credentials from the environment variable
# creds_info = json.loads(cred)

# # Load the credentials using the service account
# credentials = credentials.Certificate(creds_info)


# app = firebase_admin.initialize_app(cred)
# db = firestore.client()


import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv
import json

# Load environment variables from the .env file
load_dotenv()

# Get the credentials from the environment variable
cred = os.getenv("CREDS")
if not cred:
    raise ValueError('The $CREDS environment variable was not found!')

# Parse the JSON credentials from the environment variable
creds_info = json.loads(cred)

# Load the credentials using the service account dictionary
cred = credentials.Certificate(creds_info)

# Initialize the Firebase app with the credentials
app = firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()
