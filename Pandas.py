import pandas as pd
import numpy as np
my_series = pd.Series([10,27,32,41,5])
#indexleriyle birlikte yazdırır.
print(my_series)

my_series.size
my_series.ndim
my_series.head(2)
# ilk iki veriye ulaşmamızı sağlar head(2)

my_series.tail(2)
# Son verilere erişmemizi sağlar

my_series[1:4]
#indexler arasındaki verileri ekrana yazdırır.


numbers = [[1,2,39,67,90],[1,2,39,67,90]]
df = pd.DataFrame(numbers)
# Çarğım tablosu şeklinde  ekrana yazdırır.
print(df)


arr = np.array([[1,2,39,67,90],[8,12,45,12,8],[2,8,34,90,102]])
df = pd.DataFrame(arr)

print(df.describe().T)
"""
Çıktısı: 
   count       mean        std   min   25%   50%   75%    max
0    3.0   3.666667   3.785939   1.0   1.5   2.0   5.0    8.0
1    3.0   7.333333   5.033223   2.0   5.0   8.0  10.0   12.0
2    3.0  39.333333   5.507571  34.0  36.5  39.0  42.0   45.0
3    3.0  56.333333  40.079088  12.0  39.5  67.0  78.5   90.0
4    3.0  66.666667  51.159880   8.0  49.0  90.0  96.0  102.0
"""

dataframe_csv = pd.read_csv("file.csv")
dataframe_txt = pd.read_csv("file.txt")
dataframe_xlsx = pd.read_xlsx("file.xlsx")

