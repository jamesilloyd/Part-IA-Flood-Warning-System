from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations = build_station_list()

x = rivers_with_station(stations)


print("In alphabetical order, the first 10 rivers are:" )
print()

for i in range(10):
    print(list(x)[i])
    
hello = stations_by_river(stations)

print()

print(hello["River Aire"])
print()

print(hello["River Cam"])

print()

print(hello["Thames"])


