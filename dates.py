import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("ufo_data/ufo_dates.csv")

# overall
by_month = data.groupby("month")["country", "city"].count()
print(by_month.columns)
print(by_month)
