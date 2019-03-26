"""This module contains a collection of functions related to
geographical data."""

from floodsystem.utils import sorted_by_key
from floodsystem.haversine import haversine

'''Function that recieves a list of monitoring station objects,
and a longitude and latitude coordinates in the form of a touple, 
then returns a list of the station name, location and distance
sorted in increasing distance from the coordinates'''

def stations_by_distance(stations, p):
    a = []
    for i in stations:
        x = float(haversine(p,i.coord, miles=False))
        y = (i,x)
        a.append(y)
    a=sorted_by_key(a,1)
    return a



'''Function that recieves a list of monitoring station objects and creates a list of
the rivers with a monitoring station'''

def stations_within_radius(stations, centre, r,):
    stations_with_distance = stations_by_distance(stations, centre)
    stations_relative_to_r= []
    for i in stations_with_distance:
        if i[1]<r:
            m = i[0]
            stations_relative_to_r.append(m)
        else:
            pass
    return stations_relative_to_r
        
 


def rivers_with_station(stations):
    a = []
    for i in stations:
        x = str(i.river)
        a.append(x)
    return sorted(set(a))


'''Function that maps river names to a list of stations on that given river'''
def stations_by_river(stations):
    d={}
    for i in range(len(stations)):
        x = stations[i].river
        l = []
        if not x in d:
            for i in range(len(stations)):
                if stations[i].river == x:
                    y = stations[i].name
                    l.append(y)
            l = sorted(l)
            d[x]=l
    return d

"Function that prints the number of stations along N rivers"
  
def rivers_by_station_number(stations, N):
    m = stations_by_river(stations)
    n=[]
    for key, value in m.items():
        x= (key, len(list(filter(bool, value))))
        n.append(x)

    n.sort( key=lambda x: x[1], reverse=True)
    
    while n[N-1][1] == n[N][1]:
        N += 1
    return n[:N-1]


             