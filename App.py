#pip install pandas / conda install pandas
#https://docs.google.com/spreadsheets/d/1Q2MeMpIaMMBrse4q38UTFy00uikDFNPfeweSde3RdFE/edit?usp=sharing
#App.setup()
#App.get_food(App.get_values())
#App.create_history()
#App.get_footprints(App.food, App.get_season(App.food), App.history)
import pandas as pd
import datetime
from datetime import date, datetime

def setup():
    global user
    global passowrd
    global veggie
    global home
    user = str(input("Hey there, what is your name?"))
    password = str(input("create a password:"))
    veggie = str(input("Are you vegetarian/vegan? (type:'yes' or 'no')"))
    home = str(input("Where do you live?"))

def get_values():
    df = pd.read_excel("C:/Users/Lui/Desktop/Leuphana/final_project_Tech_Basics/Tabelle_App.xlsx")
    return(df)

def get_food(df):
    global food
    try:
        search_food = input("What did you eat?")
        food = df[df["food"]==search_food]
        food=dict(food)
        return(food)
    except:
        print("Sorry, we can´t find your food, please try again.")

def get_season(food):
    seasonal_CO2 = 0
    if "yes" in food["fruit/vegetable"]:
            d = str(date.today())
            d = d[5:7]
            try:
                if d in str(food["season"]):
                    seasonal_CO2 = str(food["CO2 in season"])
                    seasonal_CO2 = seasonal_CO2[5:]
                    print(f"This food is in Season! Therefore, the CO2 footprint is {seasonal_CO2}")
            except:
                seasonal_CO2 = str(food["CO2 not in season"])
                seasonal_CO2 = seasonal_CO2[5:]
                print(f"This food is not in Season. Therefore, the CO2 footprint is {seasonal_CO2}")
    else:
        seasonal_CO2 = str(food["CO2 not in season"])
        seasonal_CO2 = seasonal_CO2[5:]
        print(f"The CO2 footprint of this foood is {seasonal_CO2}")
    return(seasonal_CO2)

def create_history():
    global history
    data = {"CO2":[0,0], "water":[0,0], "plastic":[0,0], "date": [date.today(), date.today()]}
    history = pd.DataFrame(data)
    return(history)

def get_footprints(food, CO2_val, history):
    CO2_footprint = 0
    water_footprint = 0
    plastic_footprint = 0
    CO2_footprint += float(CO2_val[:3])
    water_val= str(food["water"])
    water_val = float(water_val[5:9])
    water_footprint += water_val
    if "yes" in food["plastic"]:
        plastic_footprint += 1
    new_row = {"CO2": CO2_footprint, "water": water_footprint, "plastic": plastic_footprint, "date": date.today()}
    history = history.append(new_row, ignore_index=True)
    return(history)
