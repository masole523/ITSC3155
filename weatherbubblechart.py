import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')
# Removing empty spaces from month column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by month Column
new_df = df.groupby(['month']).agg(
    {'average_max_temp': 'sum', 'average_min_temp': 'sum'}).reset_index()

# Preparing data
data = [
    go.Scatter(x=new_df['average_max_temp'],
               y=new_df['average_min_temp'],
               text=new_df['month'],
               mode='markers',
               marker=dict(size=new_df['average_max_temp'] / 100,color=new_df['average_min_temp'] / 100, showscale=True))
]

# Preparing layout
layout = go.Layout(title='Average high and low average of each month', xaxis_title="average high",
                   yaxis_title="average low", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherbubblechart.html')