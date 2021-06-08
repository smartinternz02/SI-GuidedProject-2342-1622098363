import numpy as np
from flask import Flask, request, render_template
import requests
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "ml68SI6aMzOvbAmT39xepf1G8tQVCsDuxh9Qhai88kiH"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
# NOTE: manually define and pass the array(s) of values to be scored in the next line
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("loll.html")
@app.route('/display',methods=['POST'])
def result():
    satisfaction_level=request.form['satisfaction_level']
    last_evaluation=request.form['last_evaluation']
    number_project=request.form['number_project']
    average_montly_hours=request.form['average_montly_hours']
    time_spend_company=request.form['time_spend_company']
    Work_accident=request.form['Work_accident']
    promotion_last_5years=request.form['promotion_last_5years']
    Department=request.form['Department']
    Salary=request.form['Salary']
    if (Department == "sales"):
            D1,D2,D3,D4,D5,D6,D7,D8 = 1,0,0,0,0,0,0,0
    if (Department == "accounting"):
            D1,D2,D3,D4,D5,D6,D7,D8 = 0,1,0,0,0,0,0,0    
    if (Department == "hr"):
            D1,D2,D3,D4,D5,D6,D7,D8 = 0,0,1,0,0,0,0,0    
    if (Department == "technical"):
            D1,D2,D3,D4,D5,D6,D7,D8 = 0,0,0,1,0,0,0,0    
    if (Department == "management"):
            D1,D2,D3,D4,D5,D6,D7,D8 = 0,0,0,0,1,0,0,0    
    if (Department == "product_mng"):
            D1,D2,D3,D4,D5,D6,D7,D8 = 0,0,0,0,0,1,0,0
    if (Department == "marketing"):
            D1,D2,D3,D4,D5,D6,D7,D8 = 0,0,0,0,0,0,1,0
    if (Department == "RandD"):
            D1,D2,D3,D4,D5,D6,D7,D8 = 0,0,0,0,0,0,0,1
        
        
    if (Salary == "low"):
            S1,S2,S3 = 0,1,0    
    if (Salary == "medium"):
            S1,S2,S3 = 0,0,1
    if (Salary == "high"):
            S1,S2,S3 = 1,0,0        
      
    t = [[int(D1),int(D2),int(D3),int(D4),int(D5),int(D6),int(D7),int(D8),int(S1),int(S2),int(S3),int(satisfaction_level),int(last_evaluation),int(number_project),int(average_montly_hours),int(time_spend_company),int(Work_accident),int(promotion_last_5years)]]    
    payload_scoring = {"input_data": [{"field": [["D1","D2","D3","D4","D5","D6","D7","D8","S1","S2","S3","satisfaction_level","last_evaluation","number_project","average_montly_hours","time_spend_company","Work_accident","promotion_last_5years"]], "values": t}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/ce43ad2a-d14d-4a3c-b32e-a6269c4dc588/predictions?version=2021-06-07', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions = response_scoring.json()
    pred = predictions['predictions'][0]['values'][0][0]

    if(pred==0):
            output = "Hurryyyyy! Employee will continue work with the company."
            print("he will not get exited")
    
    else:
            output = "Ooops! Employee will leave the company"
            print("he will get exited")
    return render_template("loll.html", y = output)    
    
    if __name__ == "__main__":
        app.run(debug=True)