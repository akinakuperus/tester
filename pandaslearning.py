import pandas as pd
import numpy as np

df = pd.read_csv('BCCDC_COVID19_Dashboard_Case_Details.csv')

df['Reported_Date'] = pd.to_datetime(df['Reported_Date']).dt.day_name()

group_counts = df.groupby(['Age_Group', 'Reported_Date','Sex']).size().reset_index(name = 'count')

idxmax_value = group_counts.groupby(['Age_Group','Sex'])['count'].idxmax()
print((group_counts.loc[idxmax_value]))
# max_values = df.loc[idxmax_value, ['Age_Group', 'Reported_Date', 'count']]
# print(max_values)