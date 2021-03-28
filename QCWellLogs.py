# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 13:09:41 2021

@author: Kevin Torres
"""

# =============================================================================
# 01. Uploading LAS files using welly
# 02. Display Well logs graphically
# 03. Display Statistics of wells logs
# 04. Quality COntrol of well logs
# =============================================================================


### IMPORTING LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import welly
from welly import Well
from welly import Project
#%config InlineBackend.figure_format='svg' # to create high resolution graphics

### IMPORT WELL DATA
well = Well.from_las(r"E:\00 ProjectsData\100. STATIC MODEL\TALARA\02. WELLS\03. LAS - DEV\LOTE X - PETROBRAS\02. las\EA11097.LAS")
well.data

well.header.name #extract the common well name from the LAS file

# well.plot() #extract general header information from the LAS file

### DISPLAY LOGS

# ## DISPLAY GRAPH
# tracks=["MD","RESD","&LN"]
# well.plot(tracks=tracks,lw=3) #line width
# well.data["GR"].plot(lw=0.7)

# ## DISPLAY INFORMATION
# well.data["GR"].start,well.data["GR"].stop # We can display the start and end depth
# well.data["GR"].read_at(1200) #output the value of GR at any depth
# well.data["GR"].describe() #print summary stats of GR curve
# print(well.data["GR"].get_stats()) #another method to print summary stats of any curve

# ## QUALITY CONTROL
# well.data["GR"].plot(lw=0.7) #display GR curve first to break the spiking parameters required

# well.data["GR_DESPIKED"]=well.data["GR"].despike(window_length=50,z=2) #Despiking is controlled by two parameters, window_length and z. We will plot both original and despiked version of log curves in the same track for comparison
# well.plot(tracks=[["MD","GR","GR_DESPIKED"]],extents=(500,1525))

# # ## CREATE A COLOR FILLED VERSION OF ANY LOG
# well.data["GR"].plot_2d(cmap="gist_rainbow")
# GR_SELECTED=well.data["GR_DESPIKED"].to_basis(start=500,stop=1500) #Let's generate a subset of despiked GR curve between say 500-1500
# GR_SELECTED.plot()

# # ## We can color fill the above log from left to rigth edge within the defined x limits
# (GR_SELECTED).plot_2d(cmap="afmhot_r",curve=True,lw=0.5,edgecolor="k")
# plt.xlim(20,150) # a color filled version between 20 API to 170 API is display

### CREATE A ZONE
zone_one = 

### VCL INTERPRETATION
