# *-* coding: utf-8 *-*

#===============================================================================
# Delphos - a decision-making tool for community-based marine conservation.
# 
# @copyright	2007 Ecotrust
# @author		Tim Welch
# @contact		twelch at ecotrust dot org
# @license		GNU GPL 2 
# 
# This program is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.  The full license for this distribution
# has been made available in the file LICENSE.txt
#
# $Id: default_criteria.py 83 2007-10-12 04:51:30Z timw $
#
# @summary - optional fisheries english criteria data to load into a new delphos 
# project on creation. Format: name, type, options, cost/benefit. Note, 
# type options are not needed for ratio criteria
#===============================================================================

fisheries_english_default_criteria = [
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
       [["Compliant",2],["Not compliant",1]], 
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
       "Percentage of the human population within the coastal community that depends on the fishery for their food or livelihood (eg. '10', '75')", 
       "Ratio", 
       "percentage of population", 
       "B"
    ],[
       "Coastal development", 
       "Ordinal", 
       [["Rural",4],["Semi-rural",3],["Developed",2],["Highly developed and industrialized",1]], 
       "B"
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




fisheries_spanish_default_criteria = [
    [
        u"Interés actual de la comunidad en la certificación del MSC",
        u"Ordinal",
        [[u"Sí",4],[u"Sí, pero necesita más información",3],[u"No está segura",2],[u"No",1]], 
        u"B"
    ],[
        u"Volumen de captura (toneladas/año)", 
        u"Ratio", 
        u"toneladas/año", 
        u"B"
    ],[
       u"Número de años para los cuales hay datos disponibles sobre el esfuerzo por unidad", 
       u"Ratio", 
       u"años", 
       u"B"
    ],[
       u"Tendencia a largo plazo de la abundancia de la población", 
       u"Ordinal",
       [[u"Al alza",4],[u"Estable",3],[u"Variable",2],[u"A la baja",1]], 
       u"B"
    ],[
       u"Comprensión de la dinámica de la población", 
       u"Ordinal", 
       [[u"Buena",4],[u"Mediocre",3],[u"Deficiente",2],[u"Ninguna",1]], 
       u"B"
    ],[
       u"Edad en la madurez o esperanza de vida", 
       u"Ordinal", 
       [[u"Baja/corta",3],[u"Media/moderada",2],[u"Alta/larga",1]], 
       u"B"
    ],[
       u"Captura incidental", 
       u"Ordinal", 
       [[u"Ninguna",4],[u"Mínima",3],[u"Moderate",2],[u"Alta",1]], 
       u"B"
    ],[
       u"Efecto de la pesquería en la cadena alimentaria", 
       u"Ordinal", 
       [[u"Ninguna",4],[u"Mínima",3],[u"Moderate",2],[u"Alta",1]], 
       u"B"
    ],[
        u"Interacción del equipo de pesca con el ecosistema", 
        u"Ordinal", 
        [[u"Ninguna",4],[u"Mínima",3],[u"Moderate",2],[u"Alta",1]], 
        u"B"
    ],[
        u"Interacción con las especie en peligro de extinción", 
        u"Ordinal", 
        [[u"Ninguna",4],[u"Mínima",3],[u"Moderada",2],[u"Alta",1]], 
        u"B"
    ],[
       u"Percepción local del efecto que tiene la pesquería en el ecosistema", 
       u"Ordinal", 
       [[u"Sin problemas",4],[u"Desconocida",3],[u"Polémica",2],[u"Negativa",1]], 
       u"B"
    ],[
       u"Sistema de gestión de la pesquería", 
       u"Ordinal", 
       [[u"Co-gerencia",3],[u"Nacional o tradicional",2],[u"Ninguna",1]], 
       u"B"
    ],[
       u"Sofisticación del sistema de gestión", 
       u"Ordinal", 
       [[u"Buena",4],[u"Mediocre",3],[u"Deficiente",2],[u"Ninguna",1]], 
       u"B"
       ],[
        u"Capacidad del sistema de gestión para hacer frente a las fluctuaciones ambientales y las catstrofes naturales", 
        u"Ordinal", 
       [[u"Buena",4],[u"Mediocre",3],[u"Deficiente",2],[u"Ninguna",1]], 
        u"B"
    ],[
       u"Resistencia del sistema de gestión a los cambios políticos", 
       u"Ordinal", 
       [[u"Buena",4],[u"Mediocre",3],[u"Deficiente",2],[u"Ninguna",1]], 
       u"B"
    ],[
       u"Cumplimiento de las regulaciones internacionales para la conservación de las especies", 
       u"Binary", 
       [[u"Las cumplen",2],[u"No las cumplen",1]], 
       u"B"
    ],[
       u"Aplicación de las regulaciones de la pesquería", 
       u"Ordinal", 
       [[u"Buena",4],[u"Mediocre",3],[u"Deficiente",2],[u"Ninguna",1]], 
       u"B"
    ],[
       u"Nivel de organización de los pescadores", 
       u"Ordinal", 
       [[u"Buena",4],[u"Mediocre",3],[u"Deficiente",2],[u"Ninguna",1]], 
       u"B"
    ],[
       u"Participación de la comunidad en la gestión de la pesquería", 
       u"Ordinal", 
       [[u"Buena",4],[u"Mediocre",3],[u"Deficiente",2],[u"Ninguna",1]], 
       u"B"
    ],[
       u"Número de las personas implicadas en la pesquería", 
       u"Ratio", 
       u"personas", 
       u"B"
    ],[
       u"Porcentaje de la población humana dentro de la comunidad costera que depende de la pesquería para su alimento o sustento (eg. '.10', '.75')", 
       u"Ratio", 
       u"Porcentaje de la población", 
       u"B"
    ],[
       u"Desarrollo costero", 
       u"Ordinal", 
       [[u"Rural",4],[u"Semi-rural",3],[u"Desarrollado",2],[u"Altamente desarrollado e industrializado",1]], 
       u"B"
    ],[
       u"Nivel socioeconómico de la comunidad de la pesca", 
       u"Ordinal", 
       [[u"Rico",4],[u"Promedio",3],[u"Pobre",2],[u"Extremadamente pobre",1]], 
       u"B"
    ],[
       u"Etapas de la cadena del mercado controlada por los pescadores", 
       u"Ordinal", 
       [[u"Captura, procesamiento y comercialización",3],[u"Captura y procesamiento",2],[u"Captura solamente",1]], 
       u"B"
    ],[
       u"Mercados nacionales", 
       u"Ordinal", 
       [[u"Existentes",3],[u"Potenciales",2],[u"Ninguna",1]], 
       u"B"
    ],[
       u"Mercados internacionales", 
       u"Ordinal", 
       [[u"Existentes",3],[u"Potenciales",2],[u"Ninguna",1]], 
       u"B"
    ]
]



mpa_communities_english_default_criteria = [
    [
        "Defined users with legal access rights to the fishing area",
        "Ordinal",
        [["Strong",4],["Mediocre",3],["Poor",2],["Open Access Resources",1]], 
        "B"
    ],[
        "Resilience in the fishing management system regarding political change in the country's authority structure",
        "Ordinal",
        [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
        "B"
    ],[
        "Community interest and willingness to establish a network of fully-protected marine reserves",
        "Ordinal",
        [["Yes",4],["Yes, but need more information",3],["Indecisive",2],["Against",1]], 
        "B"
    ],[
        "Community involvement in fishing management",
        "Ordinal",
        [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
        "B"
    ],[
       "Balance in benefit distribution of fishing exploitation", 
       "Binary", 
       [["Balanced",2],["Unbalanced",1]], 
       "B"
    ],[
        "Fishers levels of organization",
        "Ordinal",
        [["High",3],["Medium",2],["Low",1]], 
        "B"
    ],[
        "Number of fishers working in the fishing area", 
        "Ratio", 
       ["# of fishers"], 
        "C"
    ],[
        "Community's investment capacity in fully-protected marine reserves",
        "Ordinal",
        [["High",3],["Average",2],["Low",1]], 
        "B"
    ],[
        "Level of ecosystem's scientific knowledge",
        "Ordinal",
        [["High",3],["Medium",2],["Low",1]], 
        "B"
    ],[
        "Coastal Development",
        "Ordinal",
        [["Underdeveloped",4],["Developing",3],["Developed",2],["Highly Industrialized and Developed",1]], 
        "C"
    ],[
        "Area being considered for establishing a network of community reserves (sq.km OR km of coastline)", 
        "Ratio", 
       ["sq.km or km of coastline"], 
        "B"
    ],[
        "Connectivity of the possible network of the fully-protected community marine reserves in a regional system of fully-protected marine reserves",
        "Ordinal",
        [["Appropriate",4],["Moderately Appropriate",3],["Hardly Relevant",2],["Isolated",1]], 
        "B"
    ],[
        "Number of essential habitats for highly migratory species (# of habitats)", 
        "Ratio", 
       ["# of habitats"], 
        "B"
    ],[
        "Representation of different habitats in the biogeographic region (# of habitats)", 
        "Ratio", 
       ["# of habitats"], 
        "B"
    ],[
       "Opportunity to connect (by being adjacent) this marine area with a terrestrial protected area", 
       "Binary", 
       [["Present",2],["Absent",1]], 
       "B"
    ],[
       "Is a zone part of a high priority conservation site according to another national or international project?", 
       "Binary", 
       [["Yes",2],["No",1]], 
       "B"
    ],[
        "Number of species included in national or international lists under any special protection category (# of species)", 
        "Ratio", 
       ["# of species"], 
        "B"
    ],[
        "Number of species subject to fishing exploitation (# of species)", 
        "Ratio", 
       ["# of species"], 
        "B"
    ],[
        "Zone's vulnerability to natural disasters",
        "Ordinal",
        [["None",3],["Medium",2],["High",1]], 
        "C"
    ],[
       "Does UNESCO consider the zone a Human Heritage Site?", 
       "Binary", 
       [["Yes",2],["No",1]], 
       "B"
    ],[
       "Is the zone considered part of a culturally significant national category?",
       "Binary",  
       [["Yes",2],["No",1]], 
       "B"
    ],[
       "Is there a native culture with a limited territorial representation living in this zone or using it as priority for fishing or extracting natural resources?",
       "Binary",  
       [["Yes",2],["No",1]], 
       "B"
    ],[
       "Is the fishing culture for this zone part of any maritime culture with a limited geographic representation?",
       "Binary",  
       [["Yes",2],["No",1]], 
       "B"
    ],[
       "Are there sites with archaeological value in the zone?",
       "Binary", 
       [["Yes",2],["No",1]], 
       "B"
    ],[
       "Does this zone have an exceptional aesthetic value?",
       "Binary", 
       [["Yes",2],["No",1]], 
       "B"
    ],[
       "Does this zone have an exceptional educational value?",
       "Binary", 
       [["Yes",2],["No",1]], 
       "B"
    ]
]

mpa_communities_english_default_criteria = [
    [
        "Defined users with legal access rights to the fishing area",
        "Ordinal",
        [["Strong",4],["Mediocre",3],["Poor",2],["Open Access Resources",1]], 
        "B"
    ],[
        "Resilience in the fishing management system regarding political change in the country's authority structure",
        "Ordinal",
        [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
        "B"
    ],[
        "Community interest and willingness to establish a network of fully-protected marine reserves",
        "Ordinal",
        [["Yes",4],["Yes, but need more information",3],["Indecisive",2],["Against",1]], 
        "B"
    ],[
        "Community involvement in fishing management",
        "Ordinal",
        [["Good",4],["Mediocre",3],["Poor",2],["None",1]], 
        "B"
    ],[
       "Balance in benefit distribution of fishing exploitation", 
       "Binary", 
       [["Balanced",2],["Unbalanced",1]], 
       "B"
    ],[
        "Fishers levels of organization",
        "Ordinal",
        [["High",3],["Medium",2],["Low",1]], 
        "B"
    ],[
        "Number of fishers working in the fishing area", 
        "Ratio", 
       ["# of fishers"], 
        "C"
    ],[
        "Community's investment capacity in fully-protected marine reserves",
        "Ordinal",
        [["High",3],["Average",2],["Low",1]], 
        "B"
    ],[
        "Level of ecosystem's scientific knowledge",
        "Ordinal",
        [["High",3],["Medium",2],["Low",1]], 
        "B"
    ],[
        "Coastal Development",
        "Ordinal",
        [["Underdeveloped",4],["Developing",3],["Developed",2],["Highly Industrialized and Developed",1]], 
        "C"
    ],[
        "Area being considered for establishing a network of community reserves (sq.km OR km of coastline)", 
        "Ratio", 
       ["sq.km or km of coastline"], 
        "B"
    ],[
        "Connectivity of the possible network of the fully-protected community marine reserves in a regional system of fully-protected marine reserves",
        "Ordinal",
        [["Appropriate",4],["Moderately Appropriate",3],["Hardly Relevant",2],["Isolated",1]], 
        "B"
    ],[
        "Number of essential habitats for highly migratory species (# of habitats)", 
        "Ratio", 
       ["# of habitats"], 
        "B"
    ],[
        "Representation of different habitats in the biogeographic region (# of habitats)", 
        "Ratio", 
       ["# of habitats"], 
        "B"
    ],[
       "Opportunity to connect (by being adjacent) this marine area with a terrestrial protected area", 
       "Binary", 
       [["Present",2],["Absent",1]], 
       "B"
    ],[
       "Is a zone part of a high priority conservation site according to another national or international project?", 
       "Binary", 
       [["Yes",2],["No",1]], 
       "B"
    ],[
        "Number of species included in national or international lists under any special protection category (# of species)", 
        "Ratio", 
       ["# of species"], 
        "B"
    ],[
        "Number of species subject to fishing exploitation (# of species)", 
        "Ratio", 
       ["# of species"], 
        "B"
    ],[
        "Zone's vulnerability to natural disasters",
        "Ordinal",
        [["None",3],["Medium",2],["High",1]], 
        "C"
    ],[
       "Does UNESCO consider the zone a Human Heritage Site?", 
       "Binary", 
       [["Yes",2],["No",1]], 
       "B"
    ],[
       "Is the zone considered part of a culturally significant national category?",
       "Binary",  
       [["Yes",2],["No",1]], 
       "B"
    ],[
       "Is there a native culture with a limited territorial representation living in this zone or using it as priority for fishing or extracting natural resources?",
       "Binary",  
       [["Yes",2],["No",1]], 
       "B"
    ],[
       "Is the fishing culture for this zone part of any maritime culture with a limited geographic representation?",
       "Binary",  
       [["Yes",2],["No",1]], 
       "B"
    ],[
       "Are there sites with archaeological value in the zone?",
       "Binary", 
       [["Yes",2],["No",1]], 
       "B"
    ],[
       "Does this zone have an exceptional aesthetic value?",
       "Binary", 
       [["Yes",2],["No",1]], 
       "B"
    ],[
       "Does this zone have an exceptional educational value?",
       "Binary", 
       [["Yes",2],["No",1]], 
       "B"
    ]
]

#Problems
#4, 7 multiple versions, one quantitative if possible, one qualitative.  Use whichever you want
#3, 6, 9 are these criteria or just instructions for consulting experts?  if a criterion what type?  what options?
#Load them and then look at the potential values for each one.  Make sure they make sense.  A higher value will always "score" better than a lower value for the same criteria.  For example 'illegal fishing', the 'Constant' option will score highest and the 'None' option will score lowest.  I assumed that a region with more illegal fishing is a better candidate than one with less and should score higher.  Does that make sense to you?  If it doesn't you can simply create  a new criteria flipping the rank value for each option.
#Do a single criteria analysis with 2 alternatives and make sure the criteria behaves as it should.
#For qualitative I assigned a value to each option, which you can see in the options/units column of the criteria table.  An option with a higher value will score better in analysis than an option with a lower value.  Make sure each one makes sense, there is a possibility I interpreted a criterion wrong and it will score the opposite of what you expected.  To visually check can alwyas
#For every criteria type a higher value will score better in analysis 
#particularly costs
#29 visibility made a benefit
mpa_regions_english_default_criteria = [
    [
        "Total number of species", 
        "Ratio", 
        ["# of species"], 
        "B"
    ],[
        "Number of species included in national or international listings under a special protection category", 
        "Ratio", 
        ["# of species"], 
        "B"
    ],[
        "Density or abundance of each species included in national or international listings under a special protection category (A) (actual value)", 
        "Ratio", 
        ["density/abundance"], 
        "B"
    ],[
        "Density or abundance of each species included in national or international listings under a special protection category (B)",
        "Ordinal",
        [["High",4],["Medium",3],["Low",2],["None",1]], 
        "B"
    ],[
        "Number of key species", 
        "Ratio", 
        ["# of species"], 
        "B"
    ],[
        "Density or abundance of each key species (A) (actual value)", 
        "Ratio", 
        ["density/abundance"], 
        "B"
    ],[
        "Density or abundance of each key species (B)",
        "Ordinal",
        [["High",4],["Medium",3],["Low",2],["None",1]], 
        "B"
    ],[
        "Density or abundance of each species subject to fishing exploitation (A) (actual value)", 
        "Ratio", 
        ["density/abundance"], 
        "B"
    ],[
        "Density or abundance of each species subject to fishing exploitation (B)", 
        "Ordinal",
        [["High",4],["Medium",3],["Low",2],["None",1]], 
        "B"
    ],[
        "Percentage of fishing production extracted by the community from each site with respect to total production (eg. 0, 28, 100)", 
        "Ratio", 
        ["percentage"], 
        "B"
    ],[
        "Number of critical environments (substrates) at the site", 
        "Ratio", 
        ["# of environments"], 
        "B"
    ],[
        "Cover (density) of each environment within every site (A) (percentage)", 
        "Ratio", 
        ["percentage"], 
        "B"
    ],[
        "Cover (density) of each environment within every site (B)", 
        "Ordinal",
        [["High: 80-100%",4],["Medium: 50-79%",3],["Low: <50%",2],["None",1]], 
        "B"
    ],[
        "Size of every environment within each site (A) (area, eg. sq.mi)", 
        "Ratio", 
        ["area"], 
        "B"
    ],[
        "Size of every environment within each site (B)", 
        "Ordinal",
        [["High",4],["Medium",3],["Low",2],["None",1]], 
        "B"
    ],[
        "Number of depth ranges", 
        "Ratio", 
        ["# of ranges"], 
        "B"
    ],[
        "Number of sites within every critical environment selected", 
        "Ratio", 
        ["# of sites"], 
        "B"
    ],[
        "Presence of currents for larval diffusion", 
        "Ordinal",
        [["High",4],["Medium",3],["Low",2],["None",1]], 
        "B"
    ],[
        "Presence of currents for larval retention", 
        "Ordinal",
        [["High",4],["Medium",3],["Low",2],["None",1]], 
        "B"
    ],[
        u"Resilience to natural disasters or climatic changes (i.e. El Niño) ", 
        "Ordinal",
        [["High",4],["Medium",3],["Low",2],["None",1]], 
        "B"
    ],[
        "Total area per each site (eg. sq.mi)", 
        "Ratio", 
        ["area sq.mi"],
        "B"
    ],[
        "Percentage of area proposed as reserve, with respect to the total fishing area (eg. 13, 40, 100)", 
        "Ratio", 
        ["% of area"],
        "B"
    ],[
        "Distance from the nearest reserve (miles, km)", 
        "Ratio", 
        ["miles/km"],
        "B"
    ],[
        "Number of critical environments included in each site", 
        "Ratio", 
        ["# of environments"],
        "B"
    ],[
        "Number of critical environments considered within different potential networks of marine reserves", 
        "Ratio", 
        ["# of environments"],
        "B"
    ],[
        "Cover (density) of each critical environment within each site (A) (area, eg. sq.mi)", 
        "Ratio", 
        ["area"], 
        "B"
    ],[
        "Cover (density) of each critical environment within each site (B)", 
        "Ordinal",
        [["High: 80-100%",4],["Medium: 50-79%",3],["Low: <50%",2],["None",1]], 
        "B"
    ],[
        "Feasibility to conduct assessments", 
        "Ordinal",
        [["High",4],["Medium",3],["Low",2],["None",1]], 
        "C"
    ],[
        "Currents to conduct assessments (A)", 
        "Ordinal",
        [["High: always present",1],["Medium: 50% of time",2],["Low: 25% of time",3],["None",4]], 
        "C"
    ],[
       "Currents to conduct assessments (B) (presence or absence)",
       "Binary",  
       [["Yes",1],["No",2]], 
       "C"
    ],[
       "Currents to conduct assessments (C) (speed)",
        "Ratio", 
        ["speed"], 
        "C"
    ],[
       "Depth to conduct assessments (maximum depth)",
        "Ratio", 
        ["depth"], 
        "C"
    ],[
        "Visibility to conduct assessments (A)", 
        "Ordinal",
        [["High: always adequate",4],["Medium: adequate 50% of time",3],["Low: adequate 25% of time",2],["Visibility not adequate",1]], 
        "B"
    ],[
       "Visibility to conduct assessments (B) (presence or absence)",
       "Binary",  
       [["Yes",2],["No",1]], 
       "B"
    ],[
       "Visibility to conduct assessments (C) (average visibility value eg. sq.mi)",
        "Ratio", 
        ["speed"], 
        "B"
    ],[
        "Effect from exposure to swell when conducting assessments", 
        "Ordinal",
        [["High: completely exposed",1],["Medium: moderately exposed",2],["Low: little exposed",3],["None: not exposed",4]], 
        "C"
    ],[
        "Effect of wind when conducting assessments", 
        "Ordinal",
        [["High: always exposed",1],["Medium: exposed half of time",2],["Low: exposed on few occasions",3],["None: not exposed",4]], 
        "C"
    ],[
       "Abundance of fragile environments (corals, algae, among others) to conduct assessments",
        "Ratio", 
        ["abundance"], 
        "C"
    ],[
       "Total value of product extracted from each site (A) (monetary value)",
        "Ratio", 
        ["monetary unit"], 
        "C"
    ],[
        "Total value of product extracted from each site (B)", 
        "Ordinal",
        [["High",1],["Medium",2],["Low",3],["None",4]],
        "C"
    ],[
       "Recreational value of each site (A) (monetary value)",
        "Ratio", 
        ["monetary unit"], 
        "C"
    ],[
        "Recreational value of each site (B)", 
        "Ordinal",
        [["High",1],["Medium",2],["Low",3],["None",4]],
        "C"
    ],[
        "Acceptance by fishers outside the community", 
        "Ordinal",
        [["High",4],["Medium",3],["Low",2],["None",1]],
        "B"
    ],[
        "Illegal Fishing", 
        "Ordinal",
        [["Constant",4],["Moderate",3],["Little",2],["None",1]],
        "C"
    ],[
        "Surveillance (management) feasibility", 
        "Ordinal",
        [["High",4],["Medium",3],["Low",2],["None",1]],
        "B"
    ],[
        "Robustness to develop the scientific experiment", 
        "Ordinal",
        [["High",4],["Medium",3],["Low",2],["None",1]],
        "B"
    ]
]



#Taken from original version of Delphos for windows.  Deprecated
india1_fisheries_english_default_criteria = [
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
       [["Rural",4],["Semi-rural",3],["Developed",2],["Highly developed and industrialized",1]], 
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