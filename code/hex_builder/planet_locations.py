# coding: utf-8
"""
====================================
Planet Positions in the Solar System
====================================

The purpose of this demo is to demonstrate the ability of sunpy
to get the position of planetary bodies im the solar system.
"""

##############################################################################
# First the imports
from astropy.coordinates import SkyCoord
from sunpy.coordinates import get_body_heliographic_stonyhurst
from astropy.time import Time
import matplotlib.pyplot as plt
import numpy as np
from pprint import *
import ephem
import datetime

##############################################################################
# Lets grab the positions of each of the planets in stonyhurt coordinates.
obstime = Time('2014-05-15T07:54:00.005')
# planet_list = ['earth','mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus']
planet_list = ['earth','earth']
planet_coord = [get_body_heliographic_stonyhurst(this_planet, time=obstime) for this_planet in planet_list]
# pprint(planet_coord)



home = ephem.Observer()
home.lat, home.lon = -38.42, -63.58
home.date = datetime.datetime.utcnow()

moon = ephem.Moon()
moon.compute(home)
print("Moon: ",moon.az) # moon.alt,

sun = ephem.Sun()
sun.compute(home)
print("Sun: ",sun.az)


##############################################################################
# Now lets make a plot.
fig = plt.figure()
ax1 = plt.subplot(1, 1, 1, projection='polar')
tdeg = 0;
for this_planet, this_coord in zip(planet_list, planet_coord):
    tdeg = tdeg + this_coord.lon
    plt.polar(np.deg2rad(this_coord.lon), this_coord.radius, 'o', label=this_planet)
plt.legend()
plt.show()
