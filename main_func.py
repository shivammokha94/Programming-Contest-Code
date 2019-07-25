#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:02:24 2019

@author: smokha
"""

import utility
import pandas as pd
import os
import smsauth

user_data_path = 'user.csv'   #User data csv
data_path = 'data.csv'    #Form data csv
final_dataset = 'final_dataset.csv'    #Final dataset csv


if os.path.isfile(os.path.join(user_data_path)) == False:   #Create form data csv if not exists with no values
    ur_df = pd.DataFrame(columns=['username'])
    ur_df.to_csv(os.path.join(user_data_path), index = False)
  
if os.path.isfile(os.path.join(data_path)) == False:       #Create user data csv if not exists with no values
    usrdata_df = pd.DataFrame(columns=['id', 'phone_number', 'age', 'height_cm', 'weight_kg', 'gender', 'exercise_level', 'water_consumption', 'attitude_wat_consumption', 'opt_in', 'follow_up_seq'])
    with open(os.path.join(data_path), "w") as f:
        usrdata_df.to_csv(f, index = False)     




class hyderate():
    
    def __init__(self, username):  #Object initializations
        
        self.id_v = username
        
        self.number = utility.number_getter()
        if self.number is None:
            self.number = 0
            
        self.age = utility.age_getter()
        if self.age is None:                   # 0 value denotes missing
            self.age = 0
            
        self.height = utility.height_getter()
        if self.height is None:                # 0 value denotes missing
            self.height = 0
            
        self.weight = utility.wt_getter()
        if self.weight is None:                # 0 value denotes missing
            self.weight = 0
            
        self.gender = utility.gender_getter()
        if self.gender is None:               # Unknown denotes missing value
            self.gender = 'Unknown'
            
        self.exer_lev = utility.exercise_level_getter()  #0 is default
        if self.exer_lev is None:
            self.exer_lev = 0
            
        self.con_water = utility.consumption_water_getter()  #0 is default
        if self.con_water is None:
            self.con_water = 0
            
        self.att_wat = utility.att_water_con()      #0 is default
        if self.att_wat is None:   
            self.att_wat = 0
 
    
                
    def usr_check(username):    #Check if username exists
    
        ur_df = pd.DataFrame(pd.read_csv(os.path.join(user_data_path)))
    
        if str(username) in str(ur_df['username']):
            print("Username exists!")    #User exists, select options for user
            print("1. Edit existing data?")
            print("2. Opt-in/Opt-out of message service")
            print("3. Exit to main menu")
            ip = int(input("Select an option: "))
            
            if (ip == 1):
                hyderate.editer(username)  #Call to editer function
            elif(ip == 2):
                hyderate.num_check(username)   #Call to check if phone number exists
            elif(ip == 3):
                hyderate.main_menu()  #Return to main menu
            else:
                input("Invalid input...press Enter to return to main menu")   #Wrong option selection results back to main menu
                hyderate.main_menu()
        else:
            print("Username does not exist....Creating user")      #If user doesn't exist, create user and call form function
            ur_df = ur_df.append({'username': username}, ignore_index = True)
            ur_df.to_csv(os.path.join(user_data_path), index = False)
            print("Username created!")   
            input("Continue to Main menu....")
            hyderate.main(username)
    
    
    
    def editer(username):    #Edit user data if exists
        
        usrdata_df = pd.DataFrame(pd.read_csv(os.path.join(data_path)))
        
        found_df = pd.DataFrame()
        
        found_df = usrdata_df[usrdata_df['id'] == str(username)]
        
        print("User details are as follows:" )   #Show current user details
        print("1. Phone number ->", found_df['phone_number'].iloc[0])
        print("2. Age ->", found_df['age'].iloc[0])
        print("3. Height (in cm) ->", found_df['height_cm'].iloc[0])
        print("4. Weight (in kg) ->", found_df['weight_kg'].iloc[0])
        print("5. Gender ->", found_df['gender'].iloc[0])
        print("6. Execrise Level ->", found_df['exercise_level'].iloc[0])
        print("7. Water consumption ->", found_df['water_consumption'].iloc[0])
        print("8. Attitude towards consumption of water ->", found_df['attitude_wat_consumption'].iloc[0])
        print("9. Exit editer")
        ip3 = int(input("What would you like to edit?: "))
                                              #Select option for editing
        if(ip3 == 1):
            found_df['phone_number'].iloc[0] = utility.number_getter()
        elif(ip3 == 2):
            found_df['age'].iloc[0] = utility.age_getter()
        elif(ip3 == 3):
            found_df['height_cm'].iloc[0] = utility.height_getter()
        elif (ip3 == 4):
            found_df['weight_kg'].iloc[0] = utility.wt_getter()
        elif(ip3 == 5):
            found_df['gender'].iloc[0] = utility.gender_getter()
        elif(ip3 == 6):
            found_df['exercise_level'].iloc[0] = utility.exercise_level_getter()
        elif(ip3 == 7):
            found_df['water_consumption'].iloc[0] = utility.consumption_water_getter()
        elif(ip3 ==8):
            found_df['attitude_wat_consumption'].iloc[0] = utility.att_water_con()
        elif(ip3 == 9):
            hyderate.main_menu()
        else:
            input("Invalid input....press enter")
            hyderate.editer(username)
        
        usrdata_df = usrdata_df[usrdata_df['id'] != str(username)]   #Save edited data
             
        usrdata_df = pd.concat([usrdata_df, found_df], ignore_index = True, sort = False)
        
        usrdata_df.to_csv(os.path.join(data_path), index = False)
        
        print("Updates complete")
        ip2 = str(input("Edit more values?(y/n): "))   #Edit more data
        
        if (ip2.lower() == 'y' or ip2.lower() == 'yes'):
            hyderate.editer(username)
        elif (ip2.lower() == 'n' or ip2.lower == 'no'):
            hyderate.main_menu()
        else:
            input("Invalid input...press Enter to return to main menu") #Wrong option selection results back to main menu
            hyderate.main_menu()
            
    
        
    def create_user():    #Call to check username if exists in csv
        
        ur = input("Enter username:")
        hyderate.usr_check(ur)
        
    
    def save_data(usr_df):   #Save form data to csv
        
        print("Saving data")

        with open(os.path.join(data_path), 'a') as f:
            usr_df.to_csv(f, header=False, index = False)

        print("Save complete")
        input("Press Enter to continue...") 
        
        hyderate.main_menu()
   
     
    
    def user_disp(usr):     #Display user data
        
        print("Phone number ->", usr.number)
        print("Age ->", usr.age)
        print("Height (in cm) ->", usr.height)
        print("Weight (in kg) ->", usr.weight)
        print("Gender ->", usr.gender)
        print("Execrise Level ->", usr.exer_lev)
        print("Water consumption ->", usr.con_water)
        print("Attitude towards consumption of water ->", usr.att_wat)
  
    
    
    def num_check(username):  #Function to check if phone number exists
        
        usrdata_df = pd.DataFrame(pd.read_csv(os.path.join(data_path)))    
        found_df = pd.DataFrame()    
        found_df = usrdata_df[usrdata_df['id'] == str(username)]
        
        if found_df['phone_number'] is None:  
            print("Your phone number is not registered with us. Please fill in the phone number details")
            input("Returning to main menu")
            hyderate.main_menu()
            
        num = found_df['phone_number'].iloc[0]  #If phone number exists and is valid, send verification SMS
        if len(str(num)) == 10:
            smsauth.verify(num)
            
        else:
            input("Invalid Input. Returning to main menu")
            hyderate.main_menu()
        

    def binner(usrdata_df):    #Convert values to category variables
        
        ex_lev_bins = [0, 2, 3, 99]
        ex_labels = ['ex_0_1', 'ex_2_3', 'ex_4_plus']
        usrdata_df['ex_binned'] = pd.cut(usrdata_df['exercise_level'], bins = ex_lev_bins, labels = ex_labels)
        
        wat_cons_bins = [0, 5, 9, 99]
        wat_cons_labels =  ['wat_0_4', 'wat_5_8', 'wat_9_plus']
        usrdata_df['wat_binned'] = pd.cut(usrdata_df['water_consumption'], bins = wat_cons_bins, labels = wat_cons_labels)
        
        att_bins = [0, 4, 7, 10]
        att_labels = ['att_0_3', 'att_4_6', 'att_7_10']
        usrdata_df['att_binned'] = pd.cut(usrdata_df['attitude_wat_consumption'], bins = att_bins, labels = att_labels)
        
        usrdata_df = pd.get_dummies(data=usrdata_df, columns=['ex_binned', 'wat_binned', 'att_binned'])
        
        return usrdata_df
   
     
      
    def main(username):     #Form completion page 
        
        temp_df = pd.DataFrame(columns=['id', 'phone_number', 'age', 'height_cm', 'weight_kg', 'gender', 'exercise_level', 'water_consumption', 'attitude_wat_consumption', 'opt_in'])
        print("\nPlease complete the form...")
        usr = hyderate(username)
        print("\nForm complete....")
        hyderate.user_disp(usr)
        temp_df = temp_df.append({'id': str(usr.id_v), 'phone_number': int(usr.number), 'age': int(usr.age), 'height_cm': float(usr.height), 'weight_kg': float(usr.weight), 'gender': str(usr.gender), 'exercise_level': int(usr.exer_lev), 'water_consumption': int(usr.con_water), 'attitude_wat_consumption': int(usr.att_wat), 'opt_in': False, 'follow_up_seq': 0}, ignore_index=True)

        hyderate.save_data(temp_df)
 
    
     
    def final_ret():    #Final dataset csv
        
        usrdata_df = pd.DataFrame(pd.read_csv(os.path.join(data_path)))
        usrdata_df = hyderate.binner(usrdata_df)
        usrdata_df.to_csv(os.path.join(final_dataset), index = False)
        print("Final dataset stored at: ", os.path.join(final_dataset))
        input("Press Enter to continue....")
        hyderate.main_menu()
    
    
    
    def exitter():   #Exit program
        exit()
       
        
        
    def main_menu():    #Main menu
        
        print("Welcome to the main menu")
        print("1. Enter, edit data or opt-in to messenger service")
        print("2. Retrieve final dataset")
        print("3. Exit program")
        print("Select option (Press enter)")

        try:
            op = int(input("Select option: "))
            if (op == 1):
                hyderate.create_user()
            if (op == 2):
                hyderate.final_ret()
            if (op == 3):
                hyderate.exitter()
            else:
                print("Exiting")
        except:
            None

 
        

if __name__ == '__main__':
    hyderate.main_menu()
    