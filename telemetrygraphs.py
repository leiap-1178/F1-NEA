import fastf1
import plotly.graph_objects as go
#imports plotly and fastf1 needed for these  graphs

#Loads the session which is set to a default right now
session = fastf1.get_session(2024, "Bahrain", "Q")
session.load()

#selects drivers and stores them as a list(also a default right now)
drivers = ["VER", "HAM", "LEC"]

#creates the plotly graph template
fig = go.Figure()

#for each driver in the driver list retrieves the data
for drv in drivers:
    lap = session.laps.pick_drivers(drv).pick_fastest()
    tel = lap.get_car_data().add_distance()

# Tracks temperature trace data to access it
weather = session.weather_data

#cutsomises graph with a title, axis labels and values
fig.add_trace(go.Scatter(
    x=weather["Time"].dt.total_seconds(),   # convert timedelta to seconds so plotly processes it
    y=weather["TrackTemp"],
    mode="lines",
    name="Track Temp (°C)",
    yaxis="y2",
    line=dict(color="orange", width=3)
))

# layout for the labelled axis
fig.update_layout(
    title="Telemetry Overlay + Track Temperature",
    xaxis_title="Distance (m) / Time (s)",
    yaxis=dict(
        title="Speed (km/h)"
    ),
    yaxis2=dict(
        title="Track Temp (°C)",
        overlaying="y",
        side="right"
    ),
    template="plotly_dark"#sets the graph colour scheme
)

fig.show()#Executes the graph



