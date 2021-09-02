import pandas as pd
import datetime
from datetime import date, datetime

global user
user = input("what is your name?")

def create_history():
    global history
    data = {"CO2":[0,0], "water":[0,0], "plastic":[0,0], "date": [str(date.today()), str(date.today())]}
    history = pd.DataFrame(data)
    return(history)

def calculate(history):
    td = str(date.today())
    today = history[td]
    if td != date.today():
        CO2_total = today["CO2"].sum()
        water_total = today["water"].sum()
        plastic_total = today["plastic"].sum()
        global daily_history
        totals = {"CO2":CO2_total, "water":water_total, "plastic":plastic_total, "date": td}
        daily_history = pd.DataFrame(totals)
        td = date.today()
        average_plastic=history["plastic",-7:].mean()
        if plastic_total < average_plastic:
            print(f"yay {user}, you reduced your plastic footprint in comparision to your average of the last 7 days!")
        average_CO2=history["CO2",-7:].mean()
        if CO2_total < average_CO2:
            print(f"fantastic, {user}! You reduced your CO2 footprint in comparision to your average of the last 7 days!")
        average_water=history["water",-7:].mean()
        if water_total < average_water:
            print(f"Splendid, {user}! You reduced your water footprint in comparision to your average of the last 7 days!")
