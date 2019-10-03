# python3.7

import fileinput

import numpy as np
import pandas as pd
from scipy.stats.stats import pearsonr

# get positional arguments
import sys
DATA = sys.argv[1]
TARGET = sys.argv[2]

# read in target file
target = pd.read_csv( TARGET, header=0, index_col=0)

# convert target to list of integers
target_li = []
for i in target.values:
    target_li.append(int(i))

# start line counter
count = 0

# loop through all lines in file, one by one
with fileinput.input(DATA) as stream:
    for line in stream:

        # count which line the loop is working on
        count += 1

        # check if on the header line (line 1)
        if count == 1:
            
            # print outfile header
            print("pearsonR")
            
        # if not header line do pearsonR    
        else:

            # strip line and remove the index column
            LINE = line.split()[1:]

            # convert each line as integer list
            li = []
            for i in LINE:
                li.append(int(i))

            # do pearsonR and print
            COR = pearsonr(li, target_li)
            print(COR[0])
