"""
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
"""

import csv
import sys
from enum import Enum
# pylint: disable=unspecified-encoding, raise-missing-from, line-too-long
# FUNCTION 2

# FUNCTION 3


# MAIN
class DB(Enum):
    """Enum for databases"""

    AQS_DS3 = "Data/AQUASTAT Dissemination System (3).csv"
    AQS_DS6 = "Data/AQUASTAT Dissemination System (6).csv"
    AQS_WR = "Data/AQUASTAT-Water Resources.csv"
    AQS_WU = "Data/AQUASTAT-Water Use.csv"
    CLEANED_GWC = "Data/cleaned_global_water_consumption 2.csv"


def main():
    """Main func"""
    if len(sys.argv) <= 1:
        print_usage_statement()
        return
    mode = sys.argv[1]
    match mode.lower():  # These are examples. Feel free to change them.
        case "-usageovertime":
            if len(sys.argv) <= 4:
                print("Invalid arguments.")
                return
            water_use_time_compare(sys.argv[2], sys.argv[3], sys.argv[4])
        case "-percapita":
            if len(sys.argv) != 4:
                print("Usage: python3 command_line.py perCapita --country --year")
                return
            try:
                value = get_per_capita_water_use(sys.argv[2], sys.argv[3])
                print(
                    f"{alias(sys.argv[2])}'s Water Usage per Capita: \
                    {round(value, 2)} Liters per day"
                )
            except ValueError as e:
                print(e)
        case "-usageproportion":
            if len(sys.argv) != 4:
                print_usage_statement()
                return
            try:
                print(usage_proportion(sys.argv[2], sys.argv[3]))
            except ValueError as e:
                print(e)
        case _:
            print_usage_statement()

    return

def print_usage_statement():
    """Prints le usage statement"""
    print("Usage: python3 command_line.py -usageproportion --country --year")

def open_database(database: DB):
    """Returns an array for the spesificed database. EG: open_database(DB.AQS_DS3)"""
    if database not in list(DB):
        raise KeyError
    arr = []
    with open(database.value, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in reader:
            arr.append(row)
        return arr


def water_use_time_compare(country: str, year1: int, year2: int):
    """Compares the water use of a country between 2 years"""
    country = alias(country)

    time1 = filter_tags_database(
        DB.AQS_WR,
        [
            str(country),
            str(year1),
            "Exploitable water resources and dam capacity",
            "Total exploitable water resources",
        ],
    )
    time2 = filter_tags_database(
        DB.AQS_WR,
        [
            str(country),
            str(year2),
            "Exploitable water resources and dam capacity",
            "Total exploitable water resources",
        ],
    )

    if len(time1) == 0 or len(time2) == 0:
        raise KeyError
    time1 = time1[0]
    time2 = time2[0]

    water_use_y1 = time1[6].strip()
    water_use_y2 = time2[6].strip()
    water_use_time_compare_print(country,year1,year2,water_use_y1,water_use_y2)


def water_use_time_compare_print(country,year1,year2,wu1,wu2):
    """Prints the water use time compare"""
    print("Water usage in " + country, "\n")
    print(str(year1) + ": " + wu1 + "x10^9 cubic meters/year")
    print(str(year2) + ": " + wu2 + "x10^9 cubic meters/year")
    print("Difference:")
    print(str(int(wu2) - int(wu1)) + "x10^9 cubic meters/year")


def usage_proportion(country, year):
    """Returns the proportial usage of Agricultural, \
    Industrial and Household water usage in terms of percentage"""

    agc_percent = get_usage_percentage(country, year, "Agricultural")
    ind_percent = get_usage_percentage(country, year, "Industrial")
    hsh_percent = get_usage_percentage(country, year, "Household")

    print("Water usage in " + country + " in " + year + "\n")
    print("Agricultural:", round(agc_percent, 2), "%")
    print("Industrial:", round(ind_percent, 2), "%")
    print("Household:", round(hsh_percent, 2), "%")


def alias(var: str) -> str:
    """Used to make it so that country names don't have to be input perfectly."""
    match var.lower():
        case "usa" | "us" | "united states" | "united states of america" | "america":
            return "United States of America"
        case "uk" | "UK" | "united kingdom":
            return "United Kingdom:"
        case _:
            return var


def filter_by_tags(db: [], tags: []):
    """Finds all instances in a DB with certain string args"""
    arr = []
    for (
        row
    ) in (
        db
    ):
        matches = True
        for tag in tags:
            if tag not in row:
                matches = False
                break
        if matches:
            arr.append(row)

    return arr


def filter_tags_database(database: DB, tags: []):
    """Takes a database (enum) and an array of string tags. Returns all matches from\
    the spesified DB. EG: filter_by_tagsDB(DB.CLEANED_GWC,['USA','2001'])"""
    arr = open_database(database)
    return filter_by_tags(arr, tags)


def get_per_capita_water_use(country: str, year: str) -> float:
    """Returns per capita water use (liters per day) for a given country and year,\
    Raises ValueError if country/year not found or year out of range"""
    if not year.isdigit() or not 2000 <= int(year) <= 2024:
        raise ValueError("Year must be between 2000 and 2024.")

    country = alias(country)
    data = open_database(DB.CLEANED_GWC)

    # Skip header row
    for row in data[1:]:
        if row[0] == country and row[1] == year:  # match country and year
            try:
                return float(row[3])  # 4th column for per capita water use
            except ValueError:
                raise ValueError("Per capita value is missing or invalid.")

    raise ValueError(
        "Country or year not found. Pick another country or pick years from 2000-2024."
    )


def get_usage_percentage(country: str, year: str, usagetype) -> float:
    """Returns percentage for usage for a given country and year.\
    Raises ValueError if country/year not found or year out of range"""

    if not year.isdigit() or not 2000 <= int(year) <= 2024:
        raise ValueError("Year must be between 2000 and 2024.")

    country = alias(country)
    data = open_database(DB.CLEANED_GWC)

    # Skip header row
    for row in data[1:]:
        if row[0] == country and row[1] == year:  # match country and year
            if usagetype == "Agricultural":
                try:
                    return float(row[4])
                except ValueError:
                    raise ValueError("Value is missing or invalid.")
            if usagetype == "Industrial":
                try:
                    return float(row[5])
                except ValueError:
                    raise ValueError("Value is missing or invalid.")
            if usagetype == "Household":
                try:
                    return float(row[6])
                except ValueError:
                    raise ValueError("Value is missing or invalid.")

    raise ValueError(
        "Country, year or usage type not found. "
        "Pick another country or pick years from 2000-2024 and make sure you are inputting \
        'Agriculture', 'Industrial' or 'Household'."
    )


if __name__ == "__main__":
    main()
