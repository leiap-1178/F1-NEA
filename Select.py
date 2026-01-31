import fastf1

# Allows data to be written to cache
fastf1.Cache.enable_cache("cache")

 #lists the seasons which data is reliable for
seasons = list(range(2018, 2025))

print("Available F1 seasons:")
for s in seasons:
    print(s)
#asks for user to input a season cllecting data
season = int(input("\nSelect a season: "))
schedule = fastf1.get_event_schedule(season)

print(f"\nRaces in {season}:")
for _, event in schedule.iterrows():
    print(f"{event['RoundNumber']}: {event['EventName']}")

round_number = int(input("\nSelect race round number: "))

# -----------------------------------------
# 3. Load race session
# -----------------------------------------
session = fastf1.get_session(season, round_number, 'R')
session.load()

# -----------------------------------------
# 4. List drivers in that race
# -----------------------------------------
print("\nDrivers in this race:")
drivers = session.drivers
driver_abbrs = []

for d in drivers:
    info = session.get_driver(d)
    print(f"{info['Abbreviation']} - {info['FullName']}")
    driver_abbrs.append(info['Abbreviation'])

driver = input("\nSelect driver (e.g., VER, HAM, LEC): ").upper()

laps = session.laps.pick_driver(driver)

if laps.empty:
    print("\nNo lap data for this driver.")
else:
    print(f"\nLap times for {driver}:")
    for _, lap in laps.iterrows():
        print(f"Lap {int(lap['LapNumber'])}: {lap['LapTime']}")
