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
    loadDataSparseCountry()
def loadDataSparseCountry():
    arr = []
    with open('Data/AQUASTAT-Water Use.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter = ',',quotechar="|")
        for row in reader:
            if row[4] == "United States of America":
                print(str(row))

if __name__=="__main__":
    main()