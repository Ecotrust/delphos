#Format: alternative name
#Note, type options are not needed for ration criteria

fisheries_default_criteria = [
    [
        "Fishers current interest to start a certification program",
        "Ordinal",
        [["Yes",4],["Yes, but need more information",3],["Not sure",2],["No",1]], 
        "B"
    ],[
        "Level of understanding of population dynamics", 
        "Ordinal",
        [["Good",4],["Mediocre",3],["Poor",2],["None",1]],  
        "B"
    ],[
       "Level of community participation in fishery management", 
        "Ordinal",
        [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
       "B"
    ],[
       "By catch level", 
       "Ordinal", 
       [["None",4],["Minimum",3],["Moderate",2],["High",1]],
       "B"
    ],[
       "Gear ecosystem interactions", 
       "Ordinal", 
       [["None",4],["Minimum",3],["Moderate",2],["High",1]], 
       "B"
    ],[
       "Fishery interaction with endangered species", 
       "Ordinal", 
       [["None",4],["Minimum",3],["Moderate",2],["High",1]], 
       "B"
    ],[
       "Coastal development", 
       "Ordinal", 
       [["Highly industrialized and developed",1],["Developed",2],["Semi-rural",3],["Rural",4]], 
       "C"
    ],[
       "Local perception of fishery's impact on the ecosystem", 
       "Ordinal", 
       [["None",4],["Minimum",3],["Moderate",2],["High",1]], 
       "B"
    ],[
        "Fisheries management system", 
        "Ordinal", 
        [["Co-management",3],["National or Traditional",2],["None",1]], 
        "B"
    ],[
        "Level of sophistication of the management system", 
        "Ordinal", 
        [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
        "B"
    ],[
       "Management system ability to cope with environmental fluctuations and natural catastrophes shifts", 
       "Ordinal", 
       [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
       "B"
    ],[
       "Management system resilience to political shifts", 
       "Ordinal", 
       [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
       "B"
    ],[
       "Enforcement of fisheries regulations", 
       "Ordinal", 
       [["Good",4],["Mediocre",3],["Poor",2],["None",1]],  
       "B"
    ],[
       "Compliance with international regulations for species conservation", 
       "Binary", 
       [["Species are listed in IUCN, CITES",2],["Species are not listed",1]], 
       "B"
    ],[
       "Steps of the market chain controlled by fishermen", 
       "Ordinal", 
       [["Catching, processing and marketing",3],["Catching and processing",2],["Catching only",1]], 
       "B"
    ],[
       "National market", 
       "Ordinal", 
       [["Existing",3],["Potential",2],["None",1]], 
       "B"
    ],[
       "International market of the species", 
       "Ordinal", 
       [["Existing",3],["Potential",2],["None",1]],
       "B"
    ],[
       "Fishers level of organization", 
       "Ordinal", 
       [["Good",4],["Mediocre",3],["Poor",2],["None",1]],
       "B"
    ],[
        "Volume of production", 
        "Ratio", 
       ["tons/yr"], 
        "B"
    ],[
       "Number of people involved in the fishery", 
       "Ratio", 
       ["# of people"], 
       "B"
    ]
]

mpa_default_criteria = []

#for row in fisheries_default_criteria:
#    print row