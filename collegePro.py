import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path)as f:
        df=csv.DictReader(f)
        fig=px.scatter(df, x="Marks In Percentage", y="Days Present")
        fig.show()

def getDataSource(data_path):
   marks_percentage=[]
   days_present=[]
   with open(data_path)as f:
       csv_reader=csv.DictReader(f)
       for row in csv_reader:
           marks_percentage.append(float(row["Marks In Percentage"]))
           days_present.append(float(row["Days Present"]))

   return{"x":marks_percentage, "y":days_present}



def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Marks in percentage and Days present is:", correlation[0, 1])

def setup():
    data_path="collegePro.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path)

setup()




