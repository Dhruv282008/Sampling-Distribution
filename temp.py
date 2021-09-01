import plotly.figure_factory as ff 
import statistics
import pandas as pd 
import random    
import plotly.graph_objects as go
df = pd.read_csv("temp.csv")
data = df["temp"].to_list()

fig1 = ff.create_distplot([data], ["Temperature"])
fig1.show()

def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)

    return mean

def graph(meanlist):
    mean = statistics.mean(meanlist)
    fig2 = ff.create_distplot([meanlist], ["MEAN OF MEANLIST"])
    fig2.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "Mean"))
    fig2.show()

def setup():
    meanlist = []
    for i in range(0, 1000):
        setOfMeans = randomSetOfMean(100)
        meanlist.append(setOfMeans)

    graph(meanlist)

    mean = statistics.mean(meanlist)

    print("Mean of Sample Distribution: ", mean)

def stdev():
    meanlist = []
    for i in range(0, 1000):
        setOfMeans = randomSetOfMean(100)
        meanlist.append(setOfMeans)

    stdev = statistics.stdev(meanlist)

    print("Standard Deviation of Sample Distribution: ", stdev)

setup()
stdev()

mean = statistics.mean(data)
print("Mean of Data(Population): ", mean)

stdev = statistics.stdev(data)
print("Std Deviation of Data(Population): ", stdev)
