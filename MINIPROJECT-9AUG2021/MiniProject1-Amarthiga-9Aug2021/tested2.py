import pandas as pd
from sentinelsat import SentinelAPI
import geojson

# coordinates
lat = 31.625
long = 34.665

user = 'amarthiga'
password ='Gisamar#1997'

# query scenes
#api = SentinelAPI('amarthiga', 'Gisamar#1997')
api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')
footprint = 'POINT(%s %s)' % (lat, long)

product = api.query(footprint, 
                    date=('NOW-14DAYS', 'NOW'), 
                    platformname='Sentinel-2', 
                    producttype= 'S2MSI1C', 
                    area_relation='Contains',
                    limit=1
                    )

# get tile
for value in product.values():
    tile = value['tileid']
    
print(value)

product_gjson = api.to_geojson(product)
gjson =geojson.loads(product_gjson)
mygeojson=geojson.dumps(gjson.FeatureCollection)

with open('test.json', 'w+', encoding='UTF-8') as s:
    s.write(mygeojson)

print("\n")
product_gdf = api.to_dataframe(product)

# product_gdf_sorted = product_gdf.sort_values(['cloudcoverpercentage'], ascending = [True])
print(product_gdf)


# with open('test.json', 'w+', encoding='UTF-8') as s:
#     s.write(product_gjson)

