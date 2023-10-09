#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .planet import Star, Planet

sun_dict = {
                  'Name' : 'Sun',     # Star name
                  'Label': '$\odot$', # Star label
                  'Mass' : 1.0,       # mass in Solar masses
                  'Radius': 1.0,      # Star radius in Solar radii
                  'Lstar' : 1.0,      # Stellar luminosity in Lsun
                  'Teff' : 5700.,     # Stellar Effective Temperature
                  'dist' : 10.,       # Distance from observer in pc
                 }

Sun = Star(sun_dict)

# Earth
earth_dict = {
              'Name' : 'Earth', # planet name
              'Label': 'E',     # planet label
              'Mass' : 1.0,     # mass in Earth masses
              'Radius': 1.0,    # Planet radius in Earth radii
              'albedo': 0.3,    # Spherical albedo
              'a' : 1.0,        # orbital radius in AU
              'Star' : Sun,     # Star to use
              'color' : 'green', # color in plots
              }

# Venus
venus_dict = {
              'Name' : 'Venus', # planet name
              'Label': 'V',     # planet label
              'Mass' : 5.87/5.97,     # mass in Earth masses
              'Radius': 6.05/6.37,    # Planet radius in Earth radii
              'albedo': 0.71,    # Spherical albedo
              'a' : 0.72,        # orbital radius in AU
              'Star' : Sun,     # Star to use
              'color' : 'purple', # color in plots
              }

# Mars
mars_dict = {
              'Name' : 'Mars', # planet name
              'Label': 'M',     # planet label
              'Mass' : 0.64/5.97,     # mass in Earth masses
              'Radius': 3.39/6.37,    # Planet radius in Earth radii
              'albedo': 0.16,    # Spherical albedo
              'a' : 1.52,        # orbital radius in AU
              'Star' : Sun,     # Star to use
              'color' : 'red', # color in plots
              }

# Jupiter
jupiter_dict = {
              'Name' : 'Jupiter', # planet name
              'Label': 'J',     # planet label
              'Mass' : 1899.0/5.97,     # mass in Earth masses
              'Radius': 69.9/6.37,    # Planet radius in Earth radii
              'albedo': 0.34,    # Spherical albedo
              'a' : 5.2,        # orbital radius in AU
              'Star' : Sun,     # Star to use
              'color' : 'orange', # color in plots
              }

# Saturn
saturn_dict = {
              'Name' : 'Saturn', # planet name
              'Label': 'S',     # planet label
              'Mass' : 569.0/5.97,     # mass in Earth masses
              'Radius': 58.2/6.37,    # Planet radius in Earth radii
              'albedo': 0.34,    # Spherical albedo
              'a' : 9.54,        # orbital radius in AU
              'Star' : Sun,     # Star to use
              'color' : 'brown', # color in plots
              }

# Uranus
uranus_dict = {
              'Name' : 'Uranus', # planet name
              'Label': 'U',     # planet label
              'Mass' : 87.0/5.97,     # mass in Earth masses
              'Radius': 25.3/6.37,    # Planet radius in Earth radii
              'albedo': 0.30,    # Spherical albedo
              'a' : 19.2,        # orbital radius in AU
              'Star' : Sun,     # Star to use
              'color' : 'cyan', # color in plots
              }

# Neptune
neptune_dict = {
              'Name' : 'Neptune', # planet name
              'Label': 'N',     # planet label
              'Mass' : 102./5.97,     # mass in Earth masses
              'Radius': 24.6/6.37,    # Planet radius in Earth radii
              'albedo': 0.29,    # Spherical albedo
              'a' : 30.1,        # orbital radius in AU
              'Star' : Sun,     # Star to use
              'color' : 'blue', # color in plots
              }

# 5Jupiter
jupiter5_dict = {
              'Name' : '5Mj', # planet name
              'Label': '5Mj',     # planet label
              'Mass' : 5.*1899.0/5.97,     # mass in Earth masses
              'Radius': 77.9/6.37,    # Planet radius in Earth radii
              'albedo': 0.34,    # Spherical albedo
              'a' : 5.2,        # orbital radius in AU
              'Star' : Sun,     # Star to use
              'color' : 'orange', # color in plots
              }

# 10Jupiter
jupiter10_dict = {
              'Name' : '10Mj', # planet name
              'Label': '10Mj',     # planet label
              'Mass' : 10.*1899.0/5.97,     # mass in Earth masses
              'Radius': 74.8/6.37,    # Planet radius in Earth radii
              'albedo': 0.34,    # Spherical albedo
              'a' : 5.2,        # orbital radius in AU
              'Star' : Sun,     # Star to use
              'color' : 'orange', # color in plots
              }


# Create planets
Venus = Planet(venus_dict)
Earth = Planet(earth_dict)
Mars = Planet(mars_dict)
Jupiter = Planet(jupiter_dict)
Saturn = Planet(saturn_dict)
Uranus = Planet(uranus_dict)
Neptune = Planet(neptune_dict)
Jupiter5 = Planet(jupiter5_dict)
Jupiter10 = Planet(jupiter10_dict)