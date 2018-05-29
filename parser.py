#!/usr/bin/python
# zsim stats README
# Author: Daniel Sanchez <sanchezd@stanford.edu>
# Date: May 3 2011
#
# Stats are now saved in HDF5, and you should never need to write a stats
# parser. This README explains how to access them in python using h5py. It
# doubles as a python script, so you can just execute it with "python
# README.stats" and see how everything works (after you have generated a stats
# file).
#

import h5py # presents HDF5 files as numpy arrays
import numpy as np
import sys

# Open stats file
f = h5py.File('zsim-ev.h5', 'r')

# Get the single dataset in the file
dset = f["stats"]["root"]

# Each dataset is first indexed by record. A record is a snapshot of all the
# stats taken at a specific time.  All stats files have at least two records,
# at beginning (dest[0])and end of simulation (dset[-1]).  Inside each record,
# the format follows the structure of the simulated objects. A few examples:

l3_hits = np.sum(dset[-1]['l3']['hGETS'] + dset[-1]['l3']['hGETX'])
l3_misses = np.sum(dset[-1]['l3']['mGETS'] + dset[-1]['l3']['mGETXIM'] + dset[-1]['l3']['mGETXSM'])

totalInstrs = np.sum(dset[-1]['core']['instrs'])
totalCycles = np.sum(dset[-1]['core']['cycles'] + dset[-1]['core']['cCycles'])

cmdargs = str(sys.argv[0])
f = open(cmdargs, 'a')
ipc = totalInstrs / float(totalCycles)
mpki = (l3_misses * 1000) / float(totalInstrs)
f.write(str(l3_hits) + "," + str(l3_misses) + "," + str(totalInstrs) + "," + str(totalCycles) + "," + str(ipc) + "," + str(mpki) + "\n")
f.close()