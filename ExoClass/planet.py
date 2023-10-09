#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from astropy.modeling.physical_models import BlackBody as Bnu
import astropy.units as u


class Star(object):
    '''
    Star class, defines a star object with the parameters relevant for the 
    computations, including the distance of the exoplanetary system.
    
    To create a Star instance, the user need to pass a dictionary with the 
    following parameters:
    
    stardict = {
                  'Name' : 'Sun',     # Star name
                  'Label': '$\odot$', # Star label
                  'Mass' : 1.0,       # mass in Solar masses
                  'Radius': 1.0,      # Star radius in Solar radii
                  'Lstar' : 1.0,      # Stellar luminosity in Lsun
                  'Teffstar': 5772.,  # Stellar Effective Temperature
                  'dist' : 10.,       # Distance from observer in pc
                 }
    '''
    
    def __init__(self, stardict, verbose=False):
        #
        self.rsun = 6.95700e8 # m
        self.lsun = 3.828e26  # W
        self.msun = 1.9885e33 # g
        self.label = stardict['Label']
        self.name = stardict['Name']
        self.mass = stardict['Mass']
        self.dist = stardict['dist']
        self.rstar = stardict['Radius']
        self.lstar = stardict['Lstar']
        self.teff = stardict['Teff']
        

class Planet(object):
    '''
    Planet class, defines a planet object with the parameters relevant for the 
    computations.
    
    To create a Planet instance, the user need to pass a dictionary with the 
    following parameters:
    
    planetdict = {
                  'Name' : 'Earth', # planet name
                  'Label': 'E',     # planet label
                  'Mass' : 1.0,     # mass in Earth masses
                  'Radius': 1.0,    # Planet radius in Earth radii
                  'albedo': 0.3,    # Spherical albedo
                  'a' : 1.0,        # orbital radius in AU
                  'Star' : Sun,    # Star (this needs to be an instance of Star)
                  'color' : 'green', # color for plots
                 }
    '''
    
    def __init__(self, planetdict, verbose=False):
        #
        self.mearth = 5.972168e27 # g
        self.rearth = 6.371e6     # m
        self.au = 1.49598023e11   # m
        self.label = planetdict['Label']
        self.name = planetdict['Name']
        self.mass = planetdict['Mass']
        self.a = planetdict['a']
        self.albedo = planetdict['albedo']
        self.radius = planetdict['Radius']
        self.star = planetdict['Star']
        self.color = planetdict['color']
        self.verbose = verbose
        
    def f_refl(self, distance=None):
        #
        if not distance:
            rad = self.a
        else:
            rad = distance
        f = 4.55e-10*self.albedo*(self.radius/rad)**2
        dm = -2.5*np.log10(f)
        if self.verbose: print('f={0} dm={1}'.format(f, dm))
        return f
    
    def Teq(self):
        #
        #lsun = 3.828e26
        #au = 1.495978707e11
        #sbc = 5.670374419e-8
        #teq = (lsun/(16.*np.pi*sbc*au*au)*(1-self.albedo)*self.lstar/self.a/self.a)**0.25
        myteq = 278.33*((1-self.albedo)*self.star.lstar/self.a/self.a)**0.25
        return myteq
    
    def f_ther(self, wl=10., Tpla=None):
        #
        #nu = 2.99792458e14/wl
        if not Tpla:
            t_planet = self.Teq()
        else:
            t_planet = (self.Teq()**4+Tpla**4)**0.25
        
        ft_pla = Bnu(temperature=t_planet*u.K)
        ft_star = Bnu(temperature=self.star.teff*u.K)
        fact = (self.radius*self.rearth/self.star.rstar/self.star.rsun)**2
        return fact*ft_pla(wl*u.um)/ft_star(wl*u.um)
        
        