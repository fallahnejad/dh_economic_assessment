# -*- coding: utf-8 -*-
"""
Created on July 26 2017

@author: fallahnejad@eeg.tuwien.ac.at
"""
import os
import sys
import time
from math import ceil

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if path not in sys.path:
    sys.path.append(path)
"""
This modules is for calculating the indices of those pixels of a raster which
are covered with a vector. It considers an envelop around the vector layer and
returns min-xy and max-xy indices of the envelop within raster.
The indices are only for the overlapping part of a vector layer and a raster
"""


def calc_index(
    minx,
    maxy,
    dimX,
    dimY,
    fminx_,
    fmaxx_,
    fminy_,
    fmaxy_,
    pixWidth=100.0,
    pixHeight=100.0,
):
    """
    minx:          minx Raster
    maxy:          maxy Raster
    dimX:          Raster X dimension
    dimY:          Raster Y dimension
    fminx_:        minx shapefile
    fmaxx_:        maxx shapefile
    fminy_:        miny shapefile
    fmaxy_:        maxy shapefile
    pixWidth:      Width of raster pixels
    pixHeight:     Height of raster pixels
    """
    pixWidth = abs(pixWidth)
    pixHeight = abs(pixHeight)
    fminx = fminy = 10 ** 10
    fmaxx = fmaxy = 0
    # Get boundaries
    fminx = min(fminx_, fminx)
    fminy = min(fminy_, fminy)
    fmaxx = max(fmaxx_, fmaxx)
    fmaxy = max(fmaxy_, fmaxy)
    # define exact index that encompasses the feature.
    lowIndexY = int((fminx - minx) / pixWidth)
    lowIndexX = int((maxy - fmaxy) / pixHeight)
    upIndexY = ceil((fmaxx - minx) / pixWidth)
    upIndexX = ceil((maxy - fminy) / pixHeight)
    # check if input shapefile exceed the boundaries of input raster file.
    if lowIndexY < 0:
        lowIndexY = 0
    if lowIndexX < 0:
        lowIndexX = 0
    if upIndexY > dimX:
        upIndexY = dimX
    if upIndexX > dimY:
        upIndexX = dimY
    return (lowIndexX, upIndexX, lowIndexY, upIndexY)
