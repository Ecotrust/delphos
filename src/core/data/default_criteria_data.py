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
       "Percentage of the human population within the coastal community that depends on the fishery for their food or livelihood (eg. '10', '75')", 
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
       [[u"Las cumplen",1],[u"No las cumplen",0]], 
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
       [[u"Altamente desarrollado e industrializado",1],[u"Desarrollado",2],[u"Semi-rural",3],[u"Rural",4]], 
       u"C"
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
