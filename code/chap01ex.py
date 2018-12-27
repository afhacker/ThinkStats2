"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def main():
    df = read("2002FemResp.dct", "2002FemResp.dat.gz")
    print(df.pregnum.value_counts().sort_index())

def read(dct_file_path, data_file_path):
    dct = thinkstats2.ReadStataDct(dct_file_path)
    df = dct.ReadFixedWidth(data_file_path, compression="gzip")
    return df
                            
if __name__ == '__main__':
    main()
