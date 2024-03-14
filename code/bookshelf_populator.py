import numpy as np
import wikipedia as wk
import pandas as pd
import matplotlib.pyplot as plt

bkshelf = '/film next.xlsx'

df = pd.read_excel(bkshelf)

for m in range(len(df)):
    film = df["film"][m]
    print(film)

x = wk.WikipediaPage(title = "When Marnie Was There")

content = x.content
y = content.find('L')

content[y:200000]
content.index('hi')
content[content.index('hi'):content.index('hi')+11]

# help(wk.WikipediaPage)

plt.bar(content, 3)
plt.show()

# from sklearn import sk
