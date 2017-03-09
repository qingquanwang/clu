#!/usr/bin/python

import re
import pprint
import sys,os

pp = pprint.PrettyPrinter(indent = 4)

rootdir = './dict'

entity = {}

plants = {}
diseases = {}

def init():
    # plant name
    filename = os.path.join(rootdir, 'plant.txt')
    with open(filename) as fd:
        for line in fd.readlines():
            plant_name = line.strip()
            if plant_name not in plants:
                plants[plant_name] = '/plant/name'
    # disease name
    filename = os.path.join(rootdir, 'disease.txt')



if __name__ == '__main__':
    init()
