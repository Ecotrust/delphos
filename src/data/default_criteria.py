#Format: alternative name
#Note, type options are not needed for ration criteria

fisheries_default_criteria = [
    [
        "Community's current interest in MSC certification",
        "Ordinal",
        [["Yes",4],["Yes, but need more information",3],["Not sure",2],["No",1]], 
        "B"
    ],[
        "Catch volume (tons/yr)", 
        "Ratio", 
        "tons/yr", 
        "B"
    ],[
       "Number of years for which catch per unit effort data (or a comparable measure of abundance, such as landings data) are available", 
       "Ratio", 
       "years", 
       "B"
    ],[
       "Long-term trend in population abundance", 
       "Ordinal", 
       [["Up",4],["Flat",3],["Variable",2],["Down",1]], 
       "B"
    ],[
       "Understanding of population dynamics", 
       "Ordinal", 
       [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
       "B"
    ],[
       "Age at maturity OR life span", 
       "Ordinal", 
       [["Low/Short",3],["Medium/Moderate",2],["High/Long",1]], 
       "B"
    ],[
       "Bycatch", 
       "Ordinal", 
       [["None",4],["Minimum",3],["Moderate",2],["High",1]], 
       "B"
    ],[
       "Effect of fishery on the food web", 
       "Ordinal", 
       [["None",4],["Minimum",3],["Moderate",2],["High",1]], 
       "B"
    ],[
        "Interaction of fishing gear with the ecosystem", 
        "Ordinal", 
        [["None",4],["Minimum",3],["Moderate",2],["High",1]], 
        "B"
    ],[
        "Interaction with endangered species", 
        "Ordinal", 
        [["None",4],["Minimum",3],["Moderate",2],["High",1]], 
        "B"
    ],[
       "Local perception of the fishery's ecosystem impacts", 
       "Ordinal", 
       [["Without problems",4],["Unknown",3],["Controversial",2],["Bad",1]], 
       "B"
    ],[
       "Fishery management system", 
       "Ordinal", 
       [["Co-management",3],["National or Traditional",2],["None",1]], 
       "B"
    ],[
       "Sophistication of the management system", 
       "Ordinal", 
       [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
       "B"
       ],[
        "Management system's ability to cope with environmental fluctuations and natural catastrophes", 
        "Ordinal", 
       [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
        "B"
    ],[
       "Management system's resilience to political shifts", 
       "Ordinal", 
       [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
       "B"
    ],[
       "Compliance with international regulations for species conservation", 
       "Binary", 
       [["Compliant",1],["Not compliant",0]], 
       "B"
    ],[
       "Enforcement of fishery regulations", 
       "Ordinal", 
       [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
       "B"
    ],[
       "Fishers' level of organization", 
       "Ordinal", 
       [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
       "B"
    ],[
       "Community participation in fishery management", 
       "Ordinal", 
       [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
       "B"
    ],[
       "Number of people involved in the fishery", 
       "Ratio", 
       "people", 
       "B"
    ],[
       "Percentage of the human population within the coastal community that depends on the fishery for their food or livelihood (eg. '.10', '.75')", 
       "Ratio", 
       "percentage of population", 
       "B"
    ],[
       "Coastal development", 
       "Ordinal", 
       [["Highly developed and industrialized",1],["Developed",2],["Semi-rural",3],["Rural",4]], 
       "C"
    ],[
       "Socioeconomic level of fishing community", 
       "Ordinal", 
       [["Wealthy",4],["Average",3],["Poor",2],["Extremely poor",1]], 
       "B"
    ],[
       "Steps of the market chain controlled by fisherman", 
       "Ordinal", 
       [["Catching, processing and marketing",3],["Catching and processing",2],["Catching only",1]], 
       "B"
    ],[
       "National markets", 
       "Ordinal", 
       [["Existing",3],["Potential",2],["None",1]], 
       "B"
    ],[
       "International markets", 
       "Ordinal", 
       [["Existing",3],["Potential",2],["None",1]], 
       "B"
    ]
]

mpa_default_criteria = []

#for row in fisheries_default_criteria:
#    print row