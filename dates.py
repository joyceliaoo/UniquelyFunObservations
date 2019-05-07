import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("ufo_data/ufo_dates.csv")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

data_us = data[data["country"] == "us"]
by_month_us = data_us.groupby("month").count()["city"]
ct_by_month_us = list(by_month_us)
df = pd.DataFrame({'Month':months, 'sightings':ct_by_month_us})
# print(df)
df.plot.bar(x="Month", y="sightings", rot=0, title="Sightings in U.S. by Month")
# plt.show()

data_gb = data[data["country"] == "gb"]
by_month_gb = data_gb.groupby("month").count()["city"]
ct_by_month_gb = list(by_month_gb)
df = pd.DataFrame({'Month':months, 'sightings':ct_by_month_gb})
# print(df)
df.plot.bar(x="Month", y="sightings", rot=0, title="Sightings in U.K. by Month")
# plt.show()

data_ca = data[data["country"] == "ca"]
by_month_ca = data_ca.groupby("month").count()["city"]
ct_by_month_ca = list(by_month_ca)
df = pd.DataFrame({'Month':months, 'sightings':ct_by_month_ca})
# print(df)
df.plot.bar(x="Month", y="sightings", rot=0, title="Sightings in Canada by Month")
# plt.show()

data_us_july = data_us[data_us["month"] == 7]
# print(data_us_july)
days = [x for x in range(1,32)]
ct_data_us_july = data_us_july.groupby("mm/dd").count()["city"]
# print(data_us_july)
ct_data_us_july = list(ct_data_us_july)
df = pd.DataFrame({"Day":days, 'sightings':ct_data_us_july})
df.plot.bar(x="Day", y= "sightings", rot=0, title="Sightings in U.S. (July)")
# plt.show()

data_us_july = data_us_july[data_us_july["UFO_shape"] != "unknown"]
data_us_july_shape = data_us_july.groupby("UFO_shape").count()["city"].sort_values(ascending=False).head(10)
print(data_us_july_shape)
ct_data_us_july_shape  = list(data_us_july_shape)
shapes = [shape for shape in data_us_july_shape.keys()]
# print(shapes)
# print(ct_data_us_july_shape)
df = pd.DataFrame({"Shape":shapes, 'sightings':ct_data_us_july_shape})
df.plot.bar(x="Shape", y= "sightings", rot=0, title="Shapes of Sightings in U.S. (July)")
plt.show()
