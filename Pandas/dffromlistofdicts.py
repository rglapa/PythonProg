import pandas as pd

data = [{'Geeks':'dataframe', 'For':'using', 'geeks':'list'},
        {'Geeks':10, 'For':20, 'geeks':30}]

df = pd.DataFrame.from_records(data, index=['1','2'])
print(df)