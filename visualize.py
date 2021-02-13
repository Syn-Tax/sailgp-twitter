import plotly.express as px
import pandas as pd
import json

with open("world.geojson", "r") as f:
    geojson = json.load(f)

datafile = "New York.csv"
df = pd.read_csv(datafile, names = ["country_code", "num"])

fig = px.choropleth(df, geojson=geojson, locations="country_code", locationmode="ISO-3", featureidkey="country_code", color="num", color_continuous_scale="Viridis",
range_color=(0, 400))

fig.write_html("New York.html")

