# https://automating-gis-processes.github.io/2016/Lesson2-geopandas-basics.html

import geopandas as gpd

fp = "./data/UKR_adm1.shp"

data = gpd.read_file(fp)

print(data)

print(data.crs)