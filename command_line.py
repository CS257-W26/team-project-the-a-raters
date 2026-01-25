'''
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
'''

'''Function for getting the data cooresponding to a specific country/date combination'''

'''Function for getting the data in the column "Agricultural Water Use (%)"'''

'''Function for getting the data in the column "Industrial Water Use (%)"'''

'''Function for getting the data in the column "Household Water Use (%)"'''
import csv
import sys
from enum import Enum
#FUNCTION 2

#FUNCTION 3

#MAIN
class DB(Enum):
    AQS_DS3 = "Data/AQUASTAT Dissemination System (3).csv"
    AQS_DS6 = "Data/AQUASTAT Dissemination System (6).csv"
    AQS_WR = "Data/AQUASTAT-Water Resources.csv"
    AQS_WU = "Data/AQUASTAT-Water Use.csv"
    CLEANED_GWC = "Data/cleaned_global_water_consumption 2.csv" 

def main():
    if len(sys.argv) <= 1:
        print("USAGE STATEMENT GOES HERE")
        return
    mode = sys.argv[1]
    match mode.lower(): #These are examples. Feel free to change them.
        case "-usageovertime":
            if len(sys.argv) <= 4:
                return
            waterUseTimeCompare(sys.argv[2],sys.argv[3],sys.argv[4])
        case "-usageproportional":
            pass
        #FUNCTION 2
        case "percapita":
            if len(sys.argv) != 4:
                print("Usage: python3 command_line.py perCapita <Country> <Year>")
                return
            try:
                value = get_per_capita_water_use(sys.argv[2], sys.argv[3])
                print(f"{alias(sys.argv[2])}'s Water Usage per Capita: {round(value, 2)} Liters per day")
            except ValueError as e:
                print(e)
        case "usagepercentage":
            print(get_usage_percentage(sys.argv[2],sys.argv[3],sys.argv[4]))
            return
        case _:
            print("USAGE STATEMENT GOES HERE")
            pass

    return
    waterUseTimeCompare("United States of America",2001,2003)

    '''Main.'''

    '''I've mostly just been doing tests here. 
    This whole section is pretty much to make sure the code I'm writing works'''
    countrydata = filterTagsDB(DB.CLEANED_GWC,["Argentina","2004"])


def openDB(database: DB):
    '''Returns an array for the spesificed database. EG: openDB(DB.AQS_DS3)'''
    arr = []
    with open(database.value,newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter = ',',quotechar="|")  
        for row in reader:
            arr.append(row)
        return(arr)    


def waterUseTimeCompare(country: str,year1: int,year2: int): ##Work in progress. Pulls from the wrong dataset right now.
    country = alias(country)

    time1 = filterTagsDB(DB.AQS_WR,[str(country),str(year1),"Exploitable water resources and dam capacity","Total exploitable water resources"])[0]
    time2 = filterTagsDB(DB.AQS_WR,[str(country),str(year2),"Exploitable water resources and dam capacity","Total exploitable water resources"])[0]

    
    water_use_y1 = time1[6]
    water_use_y2 = time2[6]
    print("Water usage in "+country+"\n")
    print(str(year1)+": "+water_use_y1+"x10^9 cubic meters/year")
    print(str(year2)+": "+water_use_y2+"x10^9 cubic meters/year")


def alias(var: str) -> str:
    """Used to make it so that country names don't have to be input perfectly."""
    match var.lower():
        case "usa" | "us" | "united states" | "united states of america" | "america":
            return "United States of America"
        case "uk" | "UK" | "united kingdom":
            return "United Kingdom:"
        case _:
            return var


def filterByTags(db:[],tags: []): 
    """"""
    arr = []
    for row in db: # How this works: For every row, assume it by default matches the requested tags. For all requested tags, check if it's in the row. If it's not, set matches to false, and break the loop. If it matches all, adds the row to the array.
        matches = True
        for tag in tags:
            if tag not in row:
                matches = False
                break
        if matches:
            arr.append(row)
            
    return arr

def filterTagsDB(database: DB, tags: []):
    """Takes a database (enum) and an array of string tags. Returns all matches from the spesified DB. EG: filterByTagsDB(DB.CLEANED_GWC,['USA','2001'])"""
    arr = openDB(database.value)
    return filterByTags(arr,tags)

def get_per_capita_water_use(country: str, year: str) -> float:
    '''Returns per capita water use (liters per day) for a given country and year'''

    '''Raises ValueError if country/year not found or year out of range'''
    if not year.isdigit() or not (2000 <= int(year) <= 2024):
        raise ValueError("Year must be between 2000 and 2024.")

    country = alias(country)
    data = openDB(DB.CLEANED_GWC)

    # Skip header row
    for row in data[1:]:
        if row[0] == country and row[1] == year: # match country and year
            try:
                return float(row[3])  # 4th column for per capita water use
            except ValueError:
                raise ValueError("Per capita value is missing or invalid.")

    raise ValueError("Country or year not found. Pick another country or pick years from 2000-2024.")

def get_usage_percentage(country: str, year: str, usagetype) -> float:
    '''Returns percentage for usage for a given country and year'''

    '''Raises ValueError if country/year not found or year out of range'''
    if not year.isdigit() or not (2000 <= int(year) <= 2024):
        raise ValueError("Year must be between 2000 and 2024.")

    country = alias(country)
    data = openDB(DB.CLEANED_GWC)

    # Skip header row
    for row in data[1:]:
        if row[0] == country and row[1] == year: # match country and year
            if usagetype == "Agricultural":
                try:
                    return float(row[4])  
                except ValueError:
                    raise ValueError("Per capita value is missing or invalid.")
            if usagetype == "Industrial":
                try:
                    return float(row[5])  
                except ValueError:
                    raise ValueError("Per capita value is missing or invalid.")
            if usagetype == "Household":
                try:
                    return float(row[6])  
                except ValueError:
                    raise ValueError("Per capita value is missing or invalid.")    

    raise ValueError("Country, year or usage type not found. Pick another country or pick years from 2000-2024 and make sure you are inputting 'Agriculture', 'Industrial' or 'Household'.")

if __name__=="__main__":
    main()




