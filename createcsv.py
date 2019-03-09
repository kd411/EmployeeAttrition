import pandas
import random
n = 1470
s = 30
file = "dataset-complete.csv"
skip = sorted(random.sample(range(n), n-s))
df = pandas.read_csv(file, skiprows=skip)
df = df.drop(df.columns[[0, 1]], axis=1)
print(df)
df.to_csv('dataset.csv')
