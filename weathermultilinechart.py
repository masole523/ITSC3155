import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

# Preparing data
trace1 = go.Scatter(x=df['date'], y=df['actual_mean_temp'], mode='lines', name='Mean')
trace2 = go.Scatter(x=df['date'], y=df['actual_min_temp'], mode='lines', name='Minimum')
trace3 = go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='Maximum')
data = [trace1,trace2,trace3]


# Preparing layout
layout = go.Layout(title='Corona Virus Death and Recovered Cases From 2020-01-22 to 2020-03-17', xaxis_title="Date",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weathermultilinechart.html')