# Title
Global Water Sources v Spending

# Sustainable Development Goal(s)
Responsible consumption & production
Clean water & sanitation

# Features
* Ability to compare how a country obrains its water resources v. how they spend those resources (interactable visual graph)
* Interactable Global Map w/ data
* Small dictionary (not the coding kind, the kind where you ask about the meanings of terms)

## Feature 1: Identify proportonality of country's water usage

* Person responsible: Lloyd
* User story: I input Canada to see what percentage of it's water is going to Agricultutal usage, Industrial usage and Household usage and find that the cooresponding percentages for the most recent year are 57%, 26.7%, 26.4%
* Acceptance Criteria: User can input "country usage_breakdown" and it responds with the dats (accurate for the current year) of "Agricultral: []%, Industrial: []%, Household: []%

## Feature 2: Interactable Visual Graphss

* Person responsible: Paul
* User story: As someone intersted in Japan's water usage, I want to compare Japan's total drinking water consumption to freshwater reserves in 2018, so that I can see how much of their reserve is being used for people's needs.
* Acceptance Criteria: 
    - User can input a country, type of water usage, type of water reserve, and a year
    - The numbers pulled from dataset will corresspond to the user's input and be displayed.
    - With the inputs given in the specific command format, the output accurately reflects consumption vs. reserves.

## Feature 3: Small Dictionary of Terminology
* Person responsible: Jay
* User story: Click on the term "groundwater" and it tells you "Groundwater is the water present beneath Earth's surface in rock and soil pore spaces and in the fractures of rock formations" (taken from wikipedia, i assume wed write our own definitions)
* Acceptance Criteria: A feature where you click on a specific term that is used in this project (such as "industrial usage", "agricultural usage", "surface water", "ground water", etc.) and gives you it's cooresponding definition

# Datasets Metadata
URL: https://data.apps.fao.org/aquastat/?lang=en
Downloaded: 01/12/26
Authorship: Food and Agriculture Organization
Name: FAO AQUASTAT Dissemination System
Terms and Conditions: https://www.fao.org/contact-us/terms/en

URL: https://www.kaggle.com/datasets/atharvasoundankar/global-water-consumption-dataset-2000-2024
Downloaded:  01/12/26
Authorship: Atharva Soundankar
Name: Global Water Consumption Dataset (2000-2024) 🌍💧
Terms and Conditions: CC0:Public Domain

# Mock up
Sketches have been included.

# Data story
Hi! Lloyd typing! 
Originally Jay wanted to do something involving water waste due to cooling. When me and Paul met, we were talking about this water thing and began to do research. This research eventually led me to realize that the word "withdrawl" was being used in a confusing way, both as "where water is being taken from" and "where water is being used". Thus came the idea to start comparing those two datapoints. 

The first dataset was found mostly by me attempting to track down "breakdowns of what kinds of water sources people get water from" and this was not only essentially the only global data on the subject but also incredibly verbose about practically everything you could want to know on the subject. The second was found significantly earlier in the search but it covers data in more general terms than the first (the over-complexity of the first is arguably it's biggest flaw and we are not even using the whole thing.)