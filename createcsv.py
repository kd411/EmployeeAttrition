import pandas
import random
n = 1470
s = 20
file = "dataset-complete.csv"
skip = sorted(random.sample(range(n),n-s))
df = pandas.read_csv(file, skiprows=skip)
df.to_csv('dataset.csv')
