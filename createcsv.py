import pandas
import random
n = 1470
s = 30
file = "dataset-complete.csv"
skip = sorted(random.sample(range(n), n-s))
df = pandas.read_csv(file, skiprows=skip)
df.drop([1], axis=1)
df.to_csv('dataset.csv')
