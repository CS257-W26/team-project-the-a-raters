[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/w6LgLvZq)
# CS257-TeamTemplate
Template for long-term team projects for CS257 Software Design

## Features

### Feature 1: Identify Proportionality of Country's Water Usage
This feature allows users to see the breakdown of a country's water usage by sector (Agricultural, Industrial, and Household) for the most recent available year.

**Command:** `python3 command_line.py usageProportional --country`  
**Example:** `python3 command_line.py usageProportional Canada`  
**Output:** Agricultural: 57%, Industrial: 26.7%, Household: 26.4% (for the most recent year)

### Feature 2: Country Per Capita Water Usage
This feature provides the average water usage per capita for a specified country and year.

**Command:** `python3 command_line.py perCapita --country --year`  
**Example:** `python3 command_line.py perCapita Japan 2018`  
**Output:** Japan's Water Usage per Capita: 290.58 Liters per day

If the year or country is not available, an error message will suggest selecting another country or years from 2000-2024.

### Feature 3: Water Usage Over Time
This feature compares a country's water usage between two specified years, showing the values for each year and the change over time.

**Command:** `python3 command_line.py --country --year1 --year2`  
**Example:** `python3 command_line.py US 2022 2025`  
**Output:** Water usage for 2022: , Water usage for 2025:, Change:

## How to Use the Commands
Type in `python3 command_line.py` followed by the appropriate arguments for the feature you want to use, separated by spaces.  
For example: `python3 command_line.py perCapita Brazil 2020`
