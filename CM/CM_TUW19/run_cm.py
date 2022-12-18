"""
Created on Jul 26, 2017

@author: simulant
"""
import os
import sys
import time

import numpy as np

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if path not in sys.path:
    sys.path.append(path)
import CM.CM_TUW19.array2raster as A2R


def main(
    outRasterPath, geo_transform, dataType, array, noDataValue=0, OutputRasterSRS=3035
):
    A2R.array2raster(
        outRasterPath, geo_transform, dataType, array, noDataValue, OutputRasterSRS
    )
    return
