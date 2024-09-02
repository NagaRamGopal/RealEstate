import pandas as pd
import numpy as np
import pandas_profiling
from pandas_profiling import ProfileReport

df=pd.read_csv(r'realtor-data.zip.csv')
print(df.head())
rpt=ProfileReport(df)
rpt.to_file("Report.html")
