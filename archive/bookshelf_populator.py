#pip3 install pandas
import numpy as np
import matplotlib.pyplot as plt

import wikipedia as wk
import pandas as pd

bkshelf = '/Users/matthewbain/Library/CloudStorage/OneDrive-McMasterUniversity/master notebook/trackers/bookshelf.xlsx'

df = pd.read_excel(bkshelf)
print(df)

for i in range(len(df)):
    film = df["film"]

wk.WikipediaPage("When Marnie Was There")