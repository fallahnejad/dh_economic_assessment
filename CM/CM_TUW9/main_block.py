# -*- coding: utf-8 -*-
"""
Created on July 6 2017

@author: fallahnejad@eeg.tuwien.ac.at
"""
import os
import sys
import time

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if path not in sys.path:
    sys.path.append(path)
from CM.CM_TUW9.bottom_up_hdm import zonStat_selectedArea as zs
from CM.CM_TUW9.shp2csv import shp2csv
from CM.CM_TUW9.specific_demand import specific_demand
from CM.CM_TUW9.update_building_layer import update_building_lyr as update

""" This module calls other calculation modules for the BUHDM"""
verbose = False


def main(process_bool, inputValues):
    (
        eu_shp,
        spec_demand_csv,
        UsefulDemandRasterPath,
        UsefulDemandRaster,
        inShapefile,
        outCSV,
        outShapefile,
        heatDensityRaster,
        gfa_density_raster,
        population,
    ) = inputValues
    # Process 1: creates a specific demand raster layer. The country names in
    # csv should be similar to the ones in the shapefile.
    if process_bool[0]:
        start = time.time()
        specific_demand(eu_shp, spec_demand_csv, UsefulDemandRasterPath)
        if verbose:
            print("Process 1 took: %0.2f seconds" % (time.time() - start))
    # Process 2: creates a standard csv file from the input shapefile
    if process_bool[1]:
        start = time.time()
        shp2csv(inShapefile, UsefulDemandRaster, outCSV)
        if verbose:
            print("Process 2 took: %0.2f seconds" % (time.time() - start))
    # Process 3: updates and creates a new shapefile based on the standard csv
    if process_bool[2]:
        start = time.time()
        inputCSV = outCSV
        update(inputCSV, inShapefile, outShapefile)
        if verbose:
            print("Process 3 took: %0.2f seconds" % (time.time() - start))
    # Process 4: generates a heat density map
    inputCSV = outCSV
    start = time.time()
    outputs = zs(inputCSV, heatDensityRaster, gfa_density_raster, population)
    """
    Outputs are:
        Absolute heat demand: [GWh\a]
        Mean heat demand per capita: [kWh\n]
        Mean heat demand per heated surface (ave. specific demand): [kWh/m2]
    """
    if verbose:
        print("Process 4 took: %0.2f seconds" % (time.time() - start))
    return outputs, outCSV, outShapefile, heatDensityRaster
