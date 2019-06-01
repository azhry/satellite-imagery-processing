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

from glob import glob

# Set working directory 
os.chdir("C:/xampp/htdocs/sat-imgproc")

mpl.rcParams['figure.figsize'] = (14, 14)
mpl.rcParams['axes.titlesize'] = 20

all_landsat_post_bands = glob("data/coldspringfire/landsat_collect/LC080340322016072301T1-SC20180214145802/crop/*band*.tif")
all_landsat_post_bands.sort()

# stacking multiple bands
landsat_post_fire_path = "data/coldspringfire/outputs/landsat_post_fire.tif"
land_stack, land_meta = es.stack(all_landsat_post_bands, landsat_post_fire_path)
with rio.open(landsat_post_fire_path) as src:
    landsat_post_fire = src.read()

# (NIR - Red) / (NIR + Red)
landsat_ndvi = (landsat_post_fire[3] - landsat_post_fire[0]) / (landsat_post_fire[3] + landsat_post_fire[0])

# (band2 - band5) / (band2 + band5)
landsat_ndwi = (landsat_post_fire[1] - landsat_post_fire[4]) / (landsat_post_fire[1] + landsat_post_fire[4])
print(landsat_ndwi)

ndwicp = copy.copy(landsat_ndwi)
# ndwicp[(landsat_ndwi < 0.0) & (landsat_post_fire[1] > 0.15) & (landsat_post_fire[6] < 0.05) & (landsat_ndvi > 0.0)] = np.nan
ndwicp[np.any([landsat_ndwi < 0.0, landsat_post_fire[1] > 0.15, landsat_post_fire[6] < 0.05, landsat_ndvi > 0.0], axis=0)] = np.nan

# Plot NDVI data
fig, ax = plt.subplots(figsize=(12,6))
ndwi = ax.imshow(ndwicp, cmap='PiYG',
                vmin=-1, vmax=1)
fig.colorbar(ndwi, fraction=.05)
ax.set(title="Landsat Derived NDWI")
ax.set_axis_off()
plt.show()