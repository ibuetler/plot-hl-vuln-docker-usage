#!/usr/bin/env python3


import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('trend.log','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))
  
plt.bar(x, y, color = 'g', width = 0.72, label = "date")
plt.xlabel('date')
plt.ylabel('usage')
plt.title('vulnerable docker usage')
plt.legend()
plt.show()
