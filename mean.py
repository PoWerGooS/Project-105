import csv
with open("class1.csv", newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
newdata = []
for i in range(len(filedata)):
    number = filedata[i][1]
    newdata.append(number)
n = len(newdata)
total = 0
for x in newdata:
    total = total + int(x)
mean = total/n
print(mean)
import pandas as pd
import plotly.express as px
df = pd.read_csv("class1.csv")
fig = px.scatter(df, x = "Student Number", y = "Marks") 
fig.update_layout(shapes=[ dict( type= 'line', y0= mean, y1= mean, x0= 0, x1= 100 ) ])
fig.show()