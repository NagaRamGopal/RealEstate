import pandas as pd
import numpy as np
import pandas_profiling
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt

df=pd.read_csv(r'realtor-data.zip.csv')
rpt=ProfileReport(df)
rpt.to_file("Report.html")
print("Before dropping/cleaning",df.shape)

df.drop(columns=['brokered_by','zip_code','prev_sold_date'],inplace=True) #Dropping columns as we don't need these.
df.dropna(inplace=True) #Missing Values dropped.
df.drop_duplicates(inplace=True) #Dropped duplicates i.e, repeated rows.
print("After dropping/cleaning",df.shape)
print(df.duplicated().sum())
print(df.isna().sum())
print(df.head())
print("Total number of houses for sale and sold are",df["status"].value_counts())
print(df.groupby("state")["status"].value_counts().head())
print("Avg price of houses by states wise",df.groupby("state")["price"].mean().astype(int).sort_values(ascending=True)) #Ohio is having less prices and while Virgin Islands are highest.
print(df.groupby(["state","city"])["price"].mean().astype(int).reset_index())

rpt1=ProfileReport(df)
rpt1.to_file("After Standardizing.html")
print(df.select_dtypes(include="number").corr()["price"].sort_values(ascending=False)) #we can see price is highly corelated with bath, bed.