import fastf1
from fastf1.core import Session
import plotly.graph_objects as go
import pandas as pd

# Load session which is set to a random default right now
race: Session = fastf1.get_session(2025, "Azerbaijan", "R")
race.load()

# Drivers you want to compare (plan to make this customisable by user input after testing functionability
drivers = ['HAM', 'PER', 'VER', 'RUS']

# Creates the Plotly graph
fig = go.Figure()

#styles (defines the two lines styles that a driver may have depending on its index number)
my_styles = [
    {'line': {'width': 5}, 'opacity': 0.3},
    {'line': {'width': 1}, 'opacity': 0.7}
]

for driver in drivers:#selects each driver in list to clean and pick acceptable data values
    laps = race.laps.pick_drivers(driver).pick_quicklaps().reset_index()

    # Convert LapTime (timedelta) to seconds for Plotly as it cannot process it otherwise
    laps['LapTimeSeconds'] = laps['LapTime'].dt.total_seconds()
    style = my_styles[0] if drivers.index(driver) % 2 == 0 else my_styles[1]

    #creates the labelled graph customising the line and opacity and setting the axis values
    fig.add_trace(go.Scatter(
        x=laps.index + 1,  # Lap number
        y=laps['LapTimeSeconds'],
        mode='lines',
        name=driver,
        line=style['line'],
        opacity=style['opacity']
    ))

# Layout of the labelled axis
fig.update_layout(
    title="Lap Time Comparison (Plotly)",
    xaxis_title="Lap Number",
    yaxis_title="Lap Time (seconds)",
    template="plotly_dark",
    legend_title="Driver",
    height=600
)

fig.show() #executes the graph
