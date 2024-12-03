import pandas as pd
import plotly.graph_objects as go
import time

data = pd.read_csv(file_path)


data['Month'] = pd.Categorical(
    data['Month'], 
    categories=["January", "February", "March", "April", "May", "June", 
                "July", "August", "September", "October", "November", "December"], 
    ordered=True
)


illnesses_by_month = (
    data.groupby(['Year', 'Month'])['Illnesses']
    .sum()
    .reset_index()
    .sort_values(['Year', 'Month'])
)


fig = go.Figure()


fig.update_layout(
    title="Real-Time Simulation of Illnesses (Month by Month)",
    xaxis_title="Time",
    yaxis_title="Total Illnesses",
    template="plotly_white",
    height=500
)


for i in range(len(illnesses_by_month)):
    year = illnesses_by_month.loc[i, 'Year']
    month = illnesses_by_month.loc[i, 'Month']
    total_illnesses = illnesses_by_month.loc[i, 'Illnesses']

    fig.add_trace(go.Scatter(
        x=[f"{month} {year}"],
        y=[total_illnesses],
        mode='lines+markers',
        name='Illnesses',
        line=dict(color='blue'),
        showlegend=False 
    ))

   
    fig.show()


    time.sleep(0.5) 
