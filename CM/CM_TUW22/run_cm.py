import os
import sys
import time

from osgeo import gdal

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if path not in sys.path:
    sys.path.append(path)
from CM.CM_TUW1.read_raster import raster_array as RA
from CM.CM_TUW22.clip import clip_raster as cr


def main(
    rast,
    features_path,
    output_dir,
    gt,
    nodata=-9999,
    save2csv=None,
    save2raster=None,
    save2shp=None,
    unit_multiplier=None,
    return_array=False,
    OutputSRS=3035,
):
    output = cr(
        rast,
        features_path,
        output_dir,
        gt,
        nodata,
        save2csv,
        save2raster,
        save2shp,
        unit_multiplier,
        return_array,
        OutputSRS,
    )
    if return_array:
        return output
