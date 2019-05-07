import pandas as pd
import numpy as np

data = pd.read_csv("ufo_data/ufo_sqlite_1.csv")
# print(data.describe())
# print(len(data.index))

total_sightings = len(data.index)

ufo_by_country = data.groupby('country').count()["city"]
print("country distribution", ufo_by_country)

ufo_us = data[data['country'] == 'us']
ufo_gb = data[data['country'] == 'gb']
ufo_ca = data[data['country'] == 'ca']
print(len(ufo_us.index), "sightings occurred in the U.S.", len(ufo_us.index) / total_sightings, "%")
print(len(ufo_gb.index), "sightings occurred in the U.K.", len(ufo_gb.index) / total_sightings, "%")
print(len(ufo_ca.index), "sightings occurred in Canada", len(ufo_ca.index) / total_sightings, "%")

ufo_us_states = ufo_us.groupby("state/province").count()["city"].sort_values(ascending=False).head(10)
print("top 10 states with most ufo sightings:\n", ufo_us_states)

ufo_us_shapes = ufo_us[ufo_us['UFO_shape'] != "unknown"]
ufo_us_shapes = ufo_us_shapes.groupby("UFO_shape").count()["city"].sort_values(ascending=False).head(20)
print("shapes distribution in U.S.\n", ufo_us_shapes)

ufo_gb_shapes = ufo_gb[ufo_gb['UFO_shape'] != "unknown"]
ufo_gb_shapes = ufo_gb_shapes.groupby("UFO_shape").count()["city"].sort_values(ascending=False)
print("shapes distribution in U.K.\n", ufo_gb_shapes)

ufo_ca_shapes = ufo_ca[ufo_ca['UFO_shape'] != "unknown"]
ufo_ca_shapes = ufo_ca_shapes.groupby("UFO_shape").count()["city"].sort_values(ascending=False)
print("shapes distribution in Canada\n", ufo_ca_shapes)
