import pandas as pd

df = pd.read_csv('jadwal.csv', delimiter=',')

lst = [list(row) for row in df.values]