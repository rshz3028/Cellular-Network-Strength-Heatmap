import pandas as pd
import folium
from folium.plugins import HeatMap

data = pd.read_csv('jionet.csv')

# Check if data is loaded correctly
print(data.head())

# Create a base map
map_center = [data['lat'].mean(), data['lon'].mean()]
m = folium.Map(location=map_center, zoom_start=13)
heat_data = [[row['lat'], row['lon'], row['signal']] for index, row in data.iterrows()]

HeatMap(heat_data).add_to(m)
m.save('heatmap.html')
