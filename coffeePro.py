import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path)as f:
        df=csv.DictReader(f)
        fig=px.scatter(df, x="Coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource(data_path):
   coffee_ml=[]
   sleep_hours=[]
   with open(data_path)as f:
       csv_reader=csv.DictReader(f)
       for row in csv_reader:
           coffee_ml.append(float(row["Coffee in ml"]))
           sleep_hours.append(float(row["sleep in hours"]))

   return{"x":coffee_ml, "y":sleep_hours}



def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between coffee in ml and sleep in hours is:", correlation[0, 1])

def setup():
    data_path="coffeePro.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path)

setup()




