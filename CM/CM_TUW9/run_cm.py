"""
Created on Jul 26, 2017

@author: simulant
"""
import os
import sys
import time

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if path not in sys.path:
    sys.path.append(path)
import CM.CM_TUW9.main_block as mb


def main(process_bool, inputValues):
    outputs = mb.main(process_bool, inputValues)
    return outputs
