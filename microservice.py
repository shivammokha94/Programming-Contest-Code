#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:50:52 2019

@author: smokha
"""

import os
import pandas as pd
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse



auth_dataset = 'auth.csv'    #Authentication dataset csv


if os.path.isfile(os.path.join(auth_dataset)) == False:   #Create authentication csv if not exists with no values
    auth_df = pd.DataFrame(columns=['number', 'code', 'timestamp'])
    auth_df.to_csv(os.path.join(auth_dataset), index = False)
    
    



app = Flask(__name__)   #Flask app initialization

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():             #Function to revieve user SMS and save data to auth.csv
    
    auth_df = pd.DataFrame(pd.read_csv(os.path.join(auth_dataset)))

    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    num = request.form['From']
    num = ''.join(e for e in str(num) if e.isalnum())  
    num = num[1:]
    msg_body = request.form['Body']
    
    try:
        msg_body = int(msg_body)
    except:
        msg_body = 0
    
    if int(msg_body)>= 100000 and int(msg_body)<= 999999:
        auth_df = auth_df.append({'number': str(num), 'code': str(msg_body), 'timestamp': pd.to_datetime('today')}, ignore_index=True)
        auth_df = auth_df.dropna()        
        auth_df = auth_df.groupby('number', as_index=False).max()   #Ensure no duplication occurs 
        auth_df.to_csv(os.path.join(auth_dataset), index = False)   #Code handles latest 2 verification codes for each number
        resp.message("Please respond with 'Yes' on your computer")  #Automated responses
    
    elif msg_body == 0:
        resp.message("Invalid response")  #Automated responses
        
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    
