#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 08:06:51 2019

@author: teslim
"""

def volume(L,B,H):
    '''
    To compute the volume of a box
    Use the info from the gro file after creating the box from editconf
    L: length
    B: width
    H: Height
    '''
    vol = L*B*H # volume in nm3
    # vol in nm3 to litres
    conv = 1E-24
    vol = vol*conv
    
    return vol

def ppm2gL(ppm):
    '''
    To convert ppm to g/L
    ppm: conc in ppm
    gL : conc in gram per litre
    '''
    gL = ppm*1E-3
    return gL

def molecules(gL,vol):
    '''
    To calculate the number of molecules
    avogadros = avogadros number given as 6.023 * 10^-23
    mole: number of mole given as mass / molecular weight
    no_molecules = mole / avogadros number
    '''
    avogadros = 6.023 * 1E+23
    mole = vol*gL/mol_wt
    no_molecules  = mole * avogadros
        
    return no_molecules


def no_molecules_calc(L,B,H,mol_wt,ppm):
    '''
    To calculate the number of molecules i.e available_molecules
    ''' 
    vol = volume(L,B,H)
    gL = ppm2gL(ppm)
    no_molecules = molecules(gL,vol)
    
    return no_molecules




print("******************************************************")
print("Interactive tool for caclculating the number of molecules for specific ions: ")
L = 8
B = 13
H = 12
mol_wt = 23
ppm = 18300
ion_name = 'Na'

molecules = round(no_molecules_calc(L,B,H,mol_wt,ppm),4)

print("The number of molecular for the ion '{}' of {} ppm is {}.".\
      format(ion_name,ppm,molecules))

print("******************************************************")