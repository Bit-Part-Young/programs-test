#!/bin/bash

atomsk--create bcc 3.165 W orient  [-211] [0-11] [111] -duplicate 5 10 15 W_cell.xsf

atomsk W_cell.xsf -mirror 0 X -wrap W_mirror.xsf

atomsk --merge X 2 W_mirror.xsf W_cell.xsf W_GB_final.cfg
