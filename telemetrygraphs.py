import fastf1
import plotly.graph_objects as go

session = fastf1.get_session(2024, "Bahrain", "Q")
session.load()

drivers = ["VER", "HAM", "LEC"]

fig = go.Figure()

for drv in drivers:
    lap = session.laps.pick_drivers(drv).pick_fastest()
    tel = lap.get_car_data().add_distance()

# Track temperature trace data to access it
weather = session.weather_data

fig.add_trace(go.Scatter(
    x=weather["Time"].dt.total_seconds(),   # convert timedelta to seconds
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
    template="plotly_dark"
)

fig.show()

