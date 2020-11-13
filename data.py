import pandas as pd
from datetime import datetime

df = pd.read_csv('jadwal.csv', delimiter=',')

a = [list(row) for row in df.values]
lst = []

for i in a:
    while True:
        if datetime.now().strftime("%a") == i[0] and datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
            lst.append(i)
