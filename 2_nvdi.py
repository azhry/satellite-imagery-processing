import numpy as np
import os
import matplotlib as mpl
import matplotlib.pyplot as plt

import rasterio as rio
import geopandas as gpd
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import copy

# Set working directory 
os.chdir("C:/xampp/htdocs/sat-imgproc")

mpl.rcParams['figure.figsize'] = (14, 14)
mpl.rcParams['axes.titlesize'] = 20

with rio.open("data/coldspringfire/naip/m_3910505_nw_13_1_20150919/crop/m_3910505_nw_13_1_20150919_crop.tif") as src:
    naip_data = src.read()
    
# View shape of the data
print(naip_data.shape)

# (NIR - Red) / (NIR + Red)
naip_ndvi = (naip_data[3] - naip_data[0]) / (naip_data[3] + naip_data[0])
print(naip_ndvi)

ndvicp = copy.copy(naip_ndvi)
ndvicp[naip_ndvi < 0.3] = 0

# Plot NDVI data
fig, ax = plt.subplots(figsize=(12,6))
ndvi = ax.imshow(ndvicp, cmap='RdYlGn',
                vmin=-1, vmax=1)
fig.colorbar(ndvi, fraction=.05)
ax.set(title="NAIP Derived NDVI\n 19 September 2015 - Cold Springs Fire, Colorado")
ax.set_axis_off()
plt.show()

# ep.hist(naip_ndvi,
#        figsize=(12,6),
#        title=["NDVI: Distribution of pixels\n NAIP 2015 Cold Springs fire site"])
# plt.show()