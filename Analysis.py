import pandas as pd
import numpy as np
import pandas_profiling
from pandas_profiling import ProfileReport

df=pd.read_csv(r'realtor-data.zip.csv')
#rpt=ProfileReport(df)
#rpt.to_file("Report.html")
print("Before dropping/cleaning",df.shape)

df.drop(columns=['brokered_by','zip_code','prev_sold_date'],inplace=True) #Dropping columns as we don't need these.
df.dropna(inplace=True) #Missing Values dropped.
df.drop_duplicates(inplace=True) #Dropped duplicates i.e, repeated rows.
print("After dropping/cleaning",df.shape)
#print(df.duplicated().sum())
#print(df.isna().sum())
print(df.head())