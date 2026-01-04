from fastf1.core import Session
from kivy.config import Config
from kivy.graphics.context_instructions import Image
from kivy.uix.boxlayout import BoxLayout
# Imports the needed tools

#imports the libraries plotting features
from fastf1 import plotting
from matplotlib import pyplot as plt
import fastf1
from fastf1 import plotting


# Enable Matplotlib to plot the timedelta values and load
# FastF1's dark color scheme for the graph
fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme='fastf1')

#Loads a race session which is set to a default right now
race: Session = fastf1.get_session(2025, "Azerbaijan", 'R')
race.load()

#assigns a line style to each driver based on their number
my_styles = [
    {'color': 'auto', 'linestyle': 'solid', 'linewidth': 5, 'alpha': 0.3},
    {'color': 'auto', 'linestyle': 'solid', 'linewidth': 1, 'alpha': 0.7}
]
#sets the size of the graph figure
fig, ax = plt.subplots(figsize=(8, 5))

#for each driver in the list retrieves the data
for driver in ('HAM', 'PER', 'VER', 'RUS'):
    laps = race.laps.pick_drivers(driver).pick_quicklaps().reset_index()

    # customise the style of the graph (labels)
    style = plotting.get_driver_style(identifier=driver,
                                      style=my_styles,
                                      session=race)

    ax.plot(laps['LapTime'], **style, label=driver)

# add axis labels 
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time")
plotting.add_sorted_driver_legend(ax, race)

plt.show()#Executes the graph visual 
