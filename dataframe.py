import pandas as pd
df = pd.read_csv('inflation.csv')
df['average inflation'] = df.mean(axis=1)
inflation = df.loc[:, "average inflation"].to_frame().dropna()
countries = df.loc[:, "Country Name"].to_frame().dropna()

# Wages
df1 = pd.read_csv('wages.csv')
df1 = df1.rename_axis("industries").reset_index()
df1['wage growth'] = df1.iloc[:, 1:].pct_change(
    axis='columns').mean(axis=1) * 100
growth = df1.loc[:, "wage growth"].to_frame().dropna()
industries = df1.loc[:, "industries"].to_frame().dropna()
