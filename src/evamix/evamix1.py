import csv

#dialect class defining structure of files we'll be parsing
class TSV(csv.excel):
    delimiter = "\t"
    
csv.register_dialect("TSV",TSV)
reader = csv.reader(open("india1.tsv", "rb"), "TSV")

india1_values = []
for row in reader:
		india1_values.append(row)
    
for i in range(len(india1_values)):
	for j in range(len(india1_values[i])):
		#Convert cell value from string to integer
		india1_values[i][j] = int(india1_values[i][j])
	#print entire row
	print india1_values[i]
