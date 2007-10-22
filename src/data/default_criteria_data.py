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




fisheries_spanish_default_criteria = [
    [
        "Interés actual de la comunidad en la certificación del MSC",
        "Ordinal",
        [["Sí",4],["Sí, pero necesita más información",3],[" No está segura ",2],["No",1]], 
        "B"
    ],[
        "Volumen de captura (toneladas/año)", 
        "Ratio", 
        "toneladas/año", 
        "B"
    ],[
       "Número de años para los cuales hay datos disponibles sobre el esfuerzo por unidad", 
       "Ratio", 
       "años", 
       "B"
    ],[
       "Tendencia a largo plazo de la abundancia de la población", 
       "Ordinal",

       [["Al alza",4],["Estable",3],["Variable",2],["A la baja",1]], 
       "B"
    ],[
       "Comprensión de la dinámica de la población", 
       "Ordinal", 
       [["Buena",4],["Mediocre",3],["Deficiente",2],["Ninguna",1]], 
       "B"
    ],[
       "Edad en la madurez o esperanza de vida", 
       "Ordinal", 
       [["Baja/corta",3],["Media/moderada",2],["Alta/larga",1]], 
       "B"
    ],[
       "Captura incidental", 
       "Ordinal", 
       [["Ninguna",4],["Mínima",3],["Moderate",2],["Alta",1]], 
       "B"
    ],[
       "Efecto de la pesquería en la cadena alimentaria", 
       "Ordinal", 
       [["Ninguna",4],["Mínima",3],["Moderate",2],["Alta",1]], 
       "B"
    ],[
        "Interacción del equipo de pesca con el ecosistema", 
        "Ordinal", 
        [["Ninguna",4],["Mínima",3],["Moderate",2],["Alta",1]], 
        "B"
    ],[
        "Interacción con las especie en peligro de extinción", 
        "Ordinal", 
        [["Ninguna",4],["Mínima",3],["Moderada",2],["Alta",1]], 
        "B"
    ],[
       "Percepción local del efecto que tiene la pesquería en el ecosistema", 
       "Ordinal", 
       [["Sin problemas",4],["Desconocida",3],["Polémica",2],["Negativa",1]], 
       "B"
    ],[
       "Sistema de gestión de la pesquería", 
       "Ordinal", 
       [["Co-gerencia",3],["Nacional o tradicional",2],["Ninguna",1]], 
       "B"
    ],[
       "Sofisticación del sistema de gestión", 
       "Ordinal", 
       [["Buena",4],["Mediocre",3],["Deficiente",2],["Ninguna",1]], 
       "B"
       ],[
        "Capacidad del sistema de gestión para hacer frente a las fluctuaciones ambientales y las catstrofes naturales", 
        "Ordinal", 
       [["Buena",4],["Mediocre",3],["Deficiente",2],["Ninguna",1]], 
        "B"
    ],[
       "Resistencia del sistema de gestión a los cambios políticos", 
       "Ordinal", 
       [["Buena",4],["Mediocre",3],["Deficiente",2],["Ninguna",1]], 
       "B"
    ],[
       "Cumplimiento de las regulaciones internacionales para la conservación de las especies", 
       "Binary", 
       [["Las cumplen",1],["No las cumplen",0]], 
       "B"
    ],[
       "Aplicación de las regulaciones de la pesquería", 
       "Ordinal", 
       [["Buena",4],["Mediocre",3],["Deficiente",2],["Ninguna",1]], 
       "B"
    ],[
       "Nivel de organización de los pescadores", 
       "Ordinal", 
       [["Buena",4],["Mediocre",3],["Deficiente",2],["Ninguna",1]], 
       "B"
    ],[
       "Participación de la comunidad en la gestión de la pesquería", 
       "Ordinal", 
       [["Buena",4],["Mediocre",3],["Deficiente",2],["Ninguna",1]], 
       "B"
    ],[
       "Número de las personas implicadas en la pesquería", 
       "Ratio", 
       "personas", 
       "B"
    ],[
       "Porcentaje de la población humana dentro de la comunidad costera que depende de la pesquería para su alimento o sustento (eg. '.10', '.75')", 
       "Ratio", 
       "Porcentaje de la población", 
       "B"
    ],[
       "Desarrollo costero", 
       "Ordinal", 
       [["Altamente desarrollado e industrializado",1],["Desarrollado",2],["Semi-rural",3],["Rural",4]], 
       "C"
    ],[
       "Nivel socioeconómico de la comunidad de la pesca", 
       "Ordinal", 
       [["Rico",4],["Promedio",3],["Pobre",2],["Extremadamente pobre",1]], 
       "B"
    ],[
       "Etapas de la cadena del mercado controlada por los pescadores", 
       "Ordinal", 
       [["Captura, procesamiento y comercialización",3],["Captura y procesamiento",2],["Captura solamente",1]], 
       "B"
    ],[
       "Mercados nacionales", 
       "Ordinal", 
       [["Existentes",3],["Potenciales",2],["Ninguna",1]], 
       "B"
    ],[
       "Mercados internacionales", 
       "Ordinal", 
       [["Existentes",3],["Potenciales",2],["Ninguna",1]], 
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

mpa_english_default_criteria = []
mpa_spanish_default_criteria = []
