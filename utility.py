#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 12:17:40 2019

@author: smokha
"""

    
def age_getter():  #Function to get age
    
    counter = 0
    while True:  
        try:
            age = int(input("Enter age (2 - 99): "))
            if ((age >= 2) and (age <= 99)):
                return age
            else:
                print("Age not within range")
        except:
            print("Not a valid age")
        counter = counter + 1
        if (counter == 3):
            print("End age function after 3 invalid runs")
            break
 
       

def height_getter():   #Function to get height
    
    counter = 0
    while True:
        try:
            typ = str(input("Enter height. Type in -> Inches(in) or Centimeters(cm): "))
            typ = typ.lower()
            if (typ == 'cm' or typ == 'centimeters' or typ == 'centimeter'):
                height = float(input("Enter height in cm (60 - 244): "))
                if (height >= 60 and height <= 244):
                    return int(round(height, 2))
                else:
                    print("Invalid height range")
                    continue
                
            if (typ == 'inches' or typ == 'in' or typ == 'inch'):
                height = float(input("Enter height in inches (24 - 96): "))
                if (height >= 24 and height <= 96):
                    return int(round((2.54*height), 2))
                else: 
                    print("Invalid height range")
                    continue
                
            else:
                print("Invalid height type input")
        except:
            None
        counter = counter + 1
        if (counter == 3):
            print("End age height after 3 invalid runs")
            break
        
            

def wt_getter():   #Function to get weight
    
    counter = 0
    while True:
        try:
            typ = str(input("Enter weight. Type in -> Kilos(kg) or Pounds(lb): "))
            typ = typ.lower()
            if (typ == 'kg' or typ == 'kilo' or typ == 'kilos' or typ == 'kilograms' or typ == 'kilogram'):
                wt = float(input("Enter weight in kg (30 - 250): "))
                if (wt >= 30 and wt <= 250):
                    return int(round(wt, 2))
                else:
                    print("Invalid weight range")
                    continue
                
            if (typ == 'pounds' or typ == 'pound' or typ == 'lbs' or typ == 'lb'):
                wt = float(input("Enter weight in lbs (66 - 550): "))
                if (wt >= 30 and wt <= 550):
                    return int(round((0.4536*wt), 2))
                else: 
                    print("Invalid weight range")
                    continue
                
            else:
                print("Invalid weight type input")
        except:
            None
        counter = counter + 1
        if (counter == 3):
            print("End weight function after 3 invalid runs")
            break

        
        
def gender_getter():   #Function to get gender
    
    counter = 0
    while True:  
        try:
            sex = str(input("Enter gender (male (m)/female (f)): ")).lower()
            if (sex == 'm' or sex == 'male'):
                return str('male')
            if (sex == 'f' or sex == 'female'):
                return str('female')
            else:
                print("Invalid input")       
        except:
            None
        counter = counter + 1
        if (counter == 3):
            print("End gender function after 3 invalid runs")
            break
 
    

def exercise_level_getter():   #Function to get exercise level

    counter = 0
    while True:
        try:
            ex_level = int(input("Number of times you work out every week (0 - 99): "))
            if ((ex_level >= 0) and (ex_level <= 99)):
                return ex_level
            else:
                print("Exercise level not within range")
        except:
            print("Not a valid value")
        counter = counter + 1
        if (counter == 3):
            print("End function after 3 invalid runs")
            break
    


def consumption_water_getter():   #Function to get water consumption level

    counter = 0
    while True:
        try:
            con_wat = int(input("Consumption of water daily {in cups} (0 - 99): "))
            if ((con_wat >= 0) and (con_wat <= 99)):
                return con_wat
            else:
                print("Consumption level not within range")
        except:
            print("Not a valid value")
        counter = counter + 1
        if (counter == 3):
            print("End function after 3 invalid runs")
            break



def att_water_con():   #Function to get attitude towards water consumption
    
    counter = 0
    while True:
        try:
            att_wat = int(input("On a scale of 1 to 10, what's your attitude towards increasing water consumption?: "))
            if ((att_wat >= 0) and (att_wat <= 10)):
                return att_wat
            else:
                print("Value not within range")
        except:
            print("Not a valid value")
        counter = counter + 1
        if (counter == 3):
            print("End function after 3 invalid runs")
            break


def number_getter():
    
    counter = 0
    while True:
        try:
            ph_num = int(input("What's your phone number?: "))
            if (len(str((ph_num))) == 10):
                return ph_num
            else:
                print("Please enter a valid phone number")
        except:
            print("Not a valid value")
        counter = counter + 1
        if (counter == 3):
            print("End function after 3 invalid runs")
            break



#
#def get_vals():
#    
#    age = age_getter()
#    height = height_getter()  #in centimeters
#    wt = wt_getter()   #in kg
#    sex = gender_getter()    
#    ex_lev = exercise_level_getter()
#    con_wat = consumption_water_getter()
#    at_w = att_water_con()
#
#
#if __name__ == '__main__':
#    get_vals()
#    

