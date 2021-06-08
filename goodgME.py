import requests
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "ml68SI6aMzOvbAmT39xepf1G8tQVCsDuxh9Qhai88kiH"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["D1","D2","D3","D4","D5","D6","D7","D8","S1","S2","S3","satisfaction_level","last_evaluation","number_project","average_montly_hours","time_spend_company","Work_accident","promotion_last_5years"]], "values": [[0,0,0,0,0,1,0,0,0,1,0,0.38,0.53,2,157,3,0,0]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/ce43ad2a-d14d-4a3c-b32e-a6269c4dc588/predictions?version=2021-06-07', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions = response_scoring.json()
pred = predictions['predictions'][0]['values'][0][0]

if(pred==0):
    print("he will not get exited")
    
else:
    print("he will get exited")