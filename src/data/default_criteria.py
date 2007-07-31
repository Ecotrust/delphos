#Format: alternative name
#Note, type options are not needed for ration criteria

fisheries_default_criteria = [
    ["Community's current interest in MSC certification","Ordinal",["Yes","Yes, but need more information", "Not sure", "No"], "B"],
    ["Catch volume (tons/yr)", "Ratio", "tons/yr", "B"],
    ["Number of years for which catch per unit effort data (or a comparable measure of abundance, such as landings data) are available", "Ratio", "years", "B"],
    ["Long-term trend in population abundance", "Ordinal", ["Up", "Flat", "Variable", "Down"], "B"],
    ["Understanding of population dynamics", "Ordinal", ["Good", "Mediocre", "Poor", "None"], "B"],
    ["Age at maturity OR life span", "Ordinal", ["Low/Short", "Medium/Moderate", "High/Long"], "B"],
    ["Bycatch", "Ordinal", ["None", "Minimum", "Moderate", "High"], "B"],
    ["Effect of fishery on the food web", "Ordinal", ["None", "Minimum", "Moderate", "High"], "B"],
    ["Interaction of fishing gear with the ecosystem", "Ordinal", ["None", "Minimum", "Moderate", "High"], "B"],
    ["Interaction with endangered species", "Ordinal", ["None", "Minimum", "Moderate", "High"], "B"],
    ["Local perception of the fishery's ecosystem impacts", "Ordinal", ["Without problems", "Unknown", "Controversial", "Bad"], "B"],
    ["Fishery management system", "Ordinal", ["Co-management", "National or Traditional", "None"], "B"],
    ["Sophistication of the management system", "Ordinal", ["Good", "Mediocre", "Poor", "None"], "B"],
    ["Management system's ability to cope with environmental fluctuations and natural catastrophes", "Ordinal", ["Good", "Mediocre", "Poor", "None"], "B"],
    ["Management system's resilience to political shifts", "Ordinal", ["Good", "Mediocre", "Poor", "None"], "B"],
    ["Compliance with international regulations for species conservation", "Binary", ["Compliant", "Not compliant"], "B"],
    ["Enforcement of fishery regulations", "Ordinal", ["Good", "Mediocre", "Poor", "None"], "B"],
    ["Fishers' level of organization", "Ordinal", ["Good", "Mediocre", "Poor", "None"], "B"],
    ["Community participation in fishery management", "Ordinal", ["Good", "Mediocre", "Poor", "None"], "B"],
    ["Number of people involved in the fishery", "Ratio", "people", "B"],
    ["Percentage of the human population within the coastal community that depends on the fishery for their food or livelihood (eg. '.10', '.75')", "Ratio", "percentage of population", "B"],
    ["Coastal development", "Ordinal", ["Highly developed and industrialized", "Developed", "Semi-rural", "Rural"], "C"],
    ["Socioeconomic level of fishing community", "Ordinal", ["Wealthy", "Average", "Poor", "Extremely poor"], "B"],
    ["Steps of the market chain controlled by fisherman", "Ordinal", ["Catching, processing and marketing", "Catching and processing", "Catching only"], "B"],
    ["National markets", "Ordinal", ["Existing", "Potential", "None"], "B"],
    ["International markets", "Ordinal", ["Existing", "Potential", "None"], "B"],
]

mpa_default_criteria = []

#for row in fisheries_default_criteria:
#    print row