import time
#\u265E
#\u25A1 black square
#\u25A0 white squeare
import csv
from DecisionTreeLearning import DecisionTreeLearner
file = open('tennis.csv')
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
file.close()

dtl = DecisionTreeLearner(rows,header)
dtl.meausureAtribbutes()
attrs = dtl.attributsObjectList
arbol = dtl.learn( rows ,attrs,"no")


inicio2 = time.time()

fin2 = time.time()
print("El tiempo final utilizado fue: ", fin2-inicio2)
