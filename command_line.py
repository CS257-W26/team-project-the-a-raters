'''
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
'''

'''Function for getting the data cooresponding to a specific country/date combination'''

'''Function for getting the data in the column "Agricultural Water Use (%)"'''

'''Function for getting the data in the column "Industrial Water Use (%)"'''

'''Function for getting the data in the column "Household Water Use (%)"'''
import csv


#FUNCTION 2

#FUNCTION 3

#MAIN

def main():
    '''Main.'''

    '''I've mostly just been doing tests here. 
    This whole section is pretty much to make sure the code I'm writing works'''
    countrydata = loadCountry(openCGWC(),"Argentina")
    print(countrydata)
    print("0000000000000000000000")
    yeardata = loadYear(openCGWC(),"2004")
    print(yeardata)
    print("0000000000000000000000")
    doubledata = loadYear(loadCountry(openCGWC(),"Argentina"),"2004")
    print(doubledata)
   

def openCGWC():
    '''Returns an array for cleaned_global_water_consumption 2.csv'''
    arr = []
    with open('Data/cleaned_global_water_consumption 2.csv',newline='') as csvfile:
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



def loadDataSparseCountry():
    arr = []
    with open('Data/AQUASTAT-Water Use.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter = ',',quotechar="|")
        for row in reader:
            if row[4] == "United States of America":
                print(str(row))



if __name__=="__main__":
    main()

