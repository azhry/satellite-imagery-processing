# import math
# import rasterio
# import requests
# import os
# import matplotlib.pyplot as plt

# image_file = "./data/red.tif"
# sat_data = rasterio.open(image_file)
# b = sat_data.read()
# fig = plt.imshow(b[0])
# fig.set_cmap("inferno")
# plt.colorbar()
# plt.show()

import os, numpy as np, matplotlib.pyplot as plt, matplotlib as mpl
import rasterio as rio, geopandas as gpd, earthpy as et, earthpy.spatial as es, earthpy.plot as ep
from glob import glob

os.chdir("C:/xampp/htdocs/sat-imgproc")

# mpl.rcParams['figure.figsize'] = (10, 10)
# mpl.rcParams['axes.titlesize'] = 20

all_landsat_post_bands = glob("data/coldspringfire/landsat_collect/LC080340322016072301T1-SC20180214145802/crop/*band*.tif")
# all_landsat_post_bands = glob("data/*B*.TIF")
all_landsat_post_bands.sort()

# plotting single band
# with rio.open(all_landsat_post_bands[3]) as src:
# 	landsat_band4 = src.read()

# ep.plot_bands(landsat_band4[0], title="Landsat Cropped Band 4\nColdsprings Fire Scar", cmap="Greys_r")


# stacking multiple bands
landsat_post_fire_path = "data/coldspringfire/outputs/landsat_post_fire.tif"
land_stack, land_meta = es.stack(all_landsat_post_bands, landsat_post_fire_path)
with rio.open(landsat_post_fire_path) as src:
    landsat_post_fire = src.read()

band_titles = ["Band 1", "Blue", "Green", "Red", "NIR",
           "Band 6", "Band7"]
ep.plot_bands(landsat_post_fire, title=band_titles, cmap="Greys_r")

# ep.plot_rgb(landsat_post_fire,
#             rgb=[3, 2, 1],
#             title="RGB Composite Image\n Post Fire Landsat Data")

# ep.plot_rgb(landsat_post_fire,
#             rgb=[3, 2, 1],
#             title="Landsat RGB Image\n Linear Stretch Applied",
#             stretch=True,
#             str_clip=1)

# ep.hist(landsat_post_fire, title=band_titles)
# plt.show()