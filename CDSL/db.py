"""
Copyright (c) 2024 Nash Sun
"""

import os
import yaml

def date_format(date_str):
    """
    This function takes a date string in various formats and converts it to a dictionary.
    Supported formats: YYYY/M/D, YYYY/MM/DD, YYYY-M-D, YYYY-MM-DD
    """
    date_str = date_str.strip()
    date_str = date_str.replace("/", "-")
    parts = date_str.split("-")
    if len(parts[1]) == 1:
        parts[1] = "0" + parts[1]
    if len(parts[2]) == 1:
        parts[2] = "0" + parts[2]

    return parts[0] + "-" + parts[1] + "-" + parts[2]

def hour_format(time_str):
    """
    This function converts a 12-hour format time string to a 24-hour format time string.
    Supported formats: H:Mam, H:M am, H:MAM, H:M AM, etc.
    """
    time_str = time_str.strip().upper()
    if "AM" in time_str or "A.M." in time_str:
        period = "AM"
    else:
        period = "PM"
    time_str = time_str.replace("AM", "").replace("PM", "").replace("A.M.", "").replace("P.M.", "").strip()
    hour, minute = map(int, time_str.split(":"))

    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
    
    return f"{hour:02}:{minute:02}"

def insert_data(date_str, hour_str, event_str, location_str):
    """
    This function formats the input data and writes it to CDSL file.
    """
    date = date_format(date_str)
    hour = hour_format(hour_str)

    data = {
        "date": date,
        "time": hour,
        "event": event_str,
        "location": location_str
    }
        
    with open("./db.yaml", "a+", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(data=data, stream=f, allow_unicode=True)

def select_data(data_str):
    """
    This function reads the CDSL file and finds all the events in one day.
    """
    with open('./db.yaml', 'r', encoding='utf-8') as f:
        data = yaml.load_all(f.read(), Loader=yaml.FullLoader)
        result = []
        for i in data:
            if i["date"] == data_str:
                result.append([i["time"], i["event"], i["location"]])

    return result