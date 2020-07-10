import csv # CSV module handles working with CSV files
import sys # sys module to work with system-specific variables
import math # math module

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f'City(\"{self.name}\", {self.lat}, {self.lon})'

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
    with open('cities.csv', 'r') as citiesFile:
        citiesDict = csv.DictReader(citiesFile)
        for row in citiesDict:
            newCity = City(name=row['city'].strip(), lat=float(str(row['lat']).strip("0")), lon=float(str(row['lng']).strip("0")))
            cities.append(newCity)      
    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-120 # top-left
# Enter lat2,lon2: 32,-100 # bottom-right
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
# location1 = input('Enter lat1, lon1: ') # bottom-left corner
# location2 = input('Enter lat2, lon2: ') # top-right corner

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []

  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.
  if (lat1, lat2, lon1, lon2) is float:
      for city in cities:
          if math.abs(lat1 - lat2) <= 90 and math.abs(lon1 - lon2) <= 180
              if lat1 > lat2 and lon1 > lon2:
                  # lat1 north
                  # lat2 south
                  # lon1 east
                  # lon2 west
              elif lat1 > lat2 and lon1 < lon2
                  # lat1 north
                  # lat2 south
                  # lon1 west
                  # lon2 east
              elif lat1 < lat2 and lon1 > lon2:
                  # lat1 south
                  # lat2 north
                  # lon1 east
                  # lon2 west
              elif lat1 < lat2
                  

  return within
