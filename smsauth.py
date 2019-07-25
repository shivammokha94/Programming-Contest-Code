#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:26:13 2019

@author: smokha
"""
import os
import main_func
import pandas as pd
import random
from twilio.rest import Client

auth_dataset = 'auth.csv'
data_path = 'data.csv'

#Secure by storing in environment variables
#API key and token
account_sid = account_sid = '' ##Your account ID here
auth_token = auth_token = ''   #Your auth token here




def generate_code():  #Function to generate random value between 100,000 and 999,999
    
    return str(random.randrange(100000, 999999))


def send_sms(to_number, body):   #Function to send specified SMS to specified user
    
    twilio_number = ''   #Twilio phone numbers here
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body= body,
                     from_=twilio_number,
                     to=to_number
                 )

    return message.sid  #Return back message id



def check_api_csv(number, original_code):   #Code to verify the user phone number
    
    usrdata_df = pd.DataFrame(pd.read_csv(os.path.join(data_path)))   
    
    try:
        auth_df = pd.DataFrame(pd.read_csv(os.path.join(auth_dataset)))
    except:
        print("Internal error, try again later")

    found_df = auth_df[auth_df['number'].astype(str) == number]  
    
    if (found_df.count()[0] == 0):
        print("Number not found! Please retry later")
        
    if (found_df.count()[0] != 0):
        found__df_2 = found_df[found_df['code'].astype(str) == original_code]
        if found__df_2.count()[0] == 0:
            print("Code not found! Please retry later")
            
        if (found__df_2.count()[0] != 0):    #If code is confirmed, send a random follow up sequence
            print("Code confirmed")  
            found_df_3 = usrdata_df[usrdata_df['phone_number'].astype(str) == number]
            
            if (found_df_3['opt_in'].iloc[0] == True):   #Check if follow up sequence already exists
                print("You are already opted-in. Your follow up sequence is: ", found_df_3['follow_up_seq'].iloc[0])
                input("Press enter to return to the main menu")
                main_func.hyderate.main_menu()
                
            found_df_3['opt_in'].iloc[0] = True
            if found_df_3['opt_in'].iloc[0] == True:
                
                follow_seq = random.randint(1,3)    #Artificial accountability function HERE
                
                found_df_3['follow_up_seq'].iloc[0] = follow_seq
                text = 'Your follow up sequence is: ' + str(follow_seq)
                m_id_2 = send_sms(number, text)
                print("Message sent with message id: ", m_id_2)
                usrdata_df.loc[usrdata_df['phone_number'].astype(str) == str(number), 'opt_in'] = True
                usrdata_df.loc[usrdata_df['phone_number'].astype(str) == str(number), 'follow_up_seq'] = int(follow_seq)
                usrdata_df.to_csv(os.path.join(data_path), index = False)
                input("Press enter to return to main menu")
                main_func.hyderate.main_menu()
                
                if m_id_2 is not None:
                    print("Response recieved")   #Confirmation that follow up sequence is sent to the user
                else:
                    print("Message not sent, try again later")
        else:
            ip5 = input("Code not verified, try again?(Y/N): ")
            if (ip5.lower() == 'y' or ip5.lower() == 'yes'):   #Function call to try again if wrong code is recieved
                verify(number)
            elif (ip5.lower() == 'n' or ip5.lower == 'no'):
                main_func.hyderate.main_menu()
            
    
def verify(number):   #Function call to generate random code and send it to user. Once recieved, check the verification code and send follow up sequence
    
    usrdata_df = pd.DataFrame(pd.read_csv(os.path.join(data_path))) 
    found_df = usrdata_df[usrdata_df['phone_number'].astype(str) == str(number)]
    
    if found_df['opt_in'].iloc[0] == True:                             #Check if user wants to opt out
        print("You are already opted-in. Your follow up sequence is: ", found_df['follow_up_seq'].iloc[0])
        ip6 = input("You have already opted-in for the service. Opt out?(Y/N): ")  
        if (ip6.lower() == 'y' or ip6.lower() == 'yes'):        
            usrdata_df.loc[usrdata_df['phone_number'].astype(str) == str(number), 'opt_in'] = False   #Reset opt in and follow up sequence
            usrdata_df.loc[usrdata_df['phone_number'].astype(str) == str(number), 'follow_up_seq'] = 0
            usrdata_df.to_csv(os.path.join(data_path), index = False)
            print("Yo have opted out")
            input("Press enter to return to main menu")
            main_func.hyderate.main_menu()   #Return to main menu
        elif (ip6.lower() == 'n' or ip6.lower == 'no'):
            main_func.hyderate.main_menu()
    msg = 'To opt-in, please reply with the verification code on your phone.'  #If the user has not opted in, send verification code
    code = generate_code()
    m_id = send_sms(number, msg)
    print("Message sent to {} with message id {} " .format(number, m_id))    #Confirmation that verification code is sent to user
    print("YOUR VERIFICATION CODE IS: ", code)
    input("After you have responded on your phone, please press enter.")
    number = ''.join(e for e in str(number) if e.isalnum())
    check_api_csv(number, str(code))
