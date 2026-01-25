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

#FUNCTION 2

#FUNCTION 3

#MAIN

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
        case "-percapita":
            pass
        case _:
            print("USAGE STATEMENT GOES HERE")
            pass

    return
    waterUseTimeCompare("United States of America",2001,2003)

    '''Main.'''

    '''I've mostly just been doing tests here. 
    This whole section is pretty much to make sure the code I'm writing works'''
    countrydata = loadCountry(openCGWC(),"Argentina")
    #print(countrydata)
    yeardata = loadYear(openCGWC(),"2004")
    #print(yeardata)
    doubledata = loadYear(loadCountry(openCGWC(),"Argentina"),"2004")
    #print(doubledata)
   

def openCGWC():
    '''Returns an array for cleaned_global_water_consumption 2.csv'''
    arr = []
    with open('Data/cleaned_global_water_consumption 2.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter = ',',quotechar="|")  
        for row in reader:
            arr.append(row)
        return(arr)
    
def openAquastatResources():
    '''Returns an array for AQUASTA-Water Resources.csv'''
    arr = []
    with open('Data/AQUASTA-Water Resources.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter = ',',quotechar="|")  
        for row in reader:
            arr.append(row)
        return(arr)

def openAquastatUse():
    '''Returns an array for AQUASTAT-Water Use.csv'''
    arr = []
    with open('Data/AQUASTA-Water Use.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter = ',',quotechar="|")  
        for row in reader:
            arr.append(row)
        return(arr)

    
def loadCountry(readera,country):
    '''Gets all data for a specific country in an array'''

    # NOTE: THIS ONLY WORKS IF THE COUNTRY IS IN COLUMN ZERO. I'M NOT SURE HOW TO FIX THIS ISSUE
    arr = []
    for row in readera:
        if row[0] == country:
            arr.append(row)
    return(arr)

def loadYear(readera,year):
    '''Gets all data for a specific year in an array'''

    # NOTE: THIS ONLY WORKS IF THE YEAR IS IN COLUMN ONE. I'M NOT SURE HOW TO FIX THIS ISSUE
    arr = []
    for row in readera:
        if row[1] == year:
            arr.append(row)
    return(arr)



def loadDataSparseCountry(country: str):
    arr = []
    with open('Data/AQUASTAT-Water Use.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter = ',',quotechar="|")
        for row in reader:
            if row[4] == country:
                arr.append(row)
    return arr

def loadDataSparseCountryWaterResource(country: str):
    arr = []
    with open('Data/AQUASTAT-Water Resources.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter = ',',quotechar="|")
        for row in reader:
            if row[4] == country:
                arr.append(row)
    return arr

def waterUseTimeCompare(country: str,year1: int,year2: int): ##Work in progress. Pulls from the wrong dataset right now.
    country = alias(country)
    time1 = loadByTags([str(country),str(year1),"Exploitable water resources and dam capacity","Total exploitable water resources"])[0]
    time2 = loadByTags([str(country),str(year2),"Exploitable water resources and dam capacity","Total exploitable water resources"])[0]
    
    water_use_y1 = time1[6]
    water_use_y2 = time2[6]
    print("Water usage in "+country+"\n")
    print(str(year1)+": "+water_use_y1+"x10^9 cubic meters/year")
    print(str(year2)+": "+water_use_y2+"x10^9 cubic meters/year")

    # print(str(time1))
    # print(str(time2))
    

def alias(var: str) -> str:
    """Used to make it so that country names don't have to be input perfectly."""
    match var.lower():
        case "usa":
            return "United States of America"
        case "us":
            return "United States of America"
        case "united states":
            return "United States of America"
        case "united states of america":
            return "United States of America"
        case "america":
            return "United States of America"
        case _:
            return var

def loadByTags(tags: []): 
    arr = []
    with open('Data/AQUASTAT-Water Resources.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter = ',',quotechar="|")
        for row in reader: # How this works: For every row, assume it by default matches the requested tags. For all requested tags, check if it's in the row. If it's not, set matches to false, and break the loop. If it matches all, adds the row to the array.
            matches = True
            for tag in tags:
                if tag not in row:
                    matches = False
                    break
            if matches:
                arr.append(row)
            
    return arr
    

    

if __name__=="__main__":
    main()




