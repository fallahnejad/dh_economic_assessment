import os
import sys
import time

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if path not in sys.path:
    sys.path.append(path)
from CM.CM_TUW21.csv2shp import csv2shapefile as c2s


def main(inShpPath, inCSV, outShpPath, id_field="id", shp_id_field=0, OutputSRS=3035):
    c2s(inShpPath, inCSV, outShpPath, id_field, shp_id_field, OutputSRS)
