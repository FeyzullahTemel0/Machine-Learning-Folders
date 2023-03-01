import pandas as pd
import numpy as np

last_year = pd.read_csv("employee_revenue_lastyear.csv")

# print(last_year.head())


# print(last_year.head(8))

# print(last_year.tail(6))
'''
      Name  Number of Calls  Average Deal Size  Revenue
5     Rose              350                8.0   1800.0
6     Lucy               50               12.0    500.0
7    Ellen              560                NaN   3300.0
8    Karen               20               25.0    500.0
9   Jamaal               30               30.0    800.0
10    Omer              400                8.0   2000.0
'''

# print(last_year.shape)
# print(last_year.info())


# last_year["Year"] = 2021 
# print(last_year)

names = np.array(["Ben","Omer","Karen","Celine","Sue","Bore","Rose","Ellen","Bob","Taylor","Jude"])
call_numbers = np.array([300,10,500,70,100,100,600,800,200,450,80])
average_deal_sizes = np.array([8,6,24,32,5,25,25,40,15,10,12])
revenues = np.array([2400,60,12000,2275,500,770,4000,6000,800,1200,500])

dictionary = {"name":names,
              "calls":call_numbers,
              "avg_deal_size":average_deal_sizes,
              "revenue":revenues}

current_year = pd.DataFrame(dictionary)
# print(current_year.head())


current_year.columns=last_year.columns

all_data = pd.concat([last_year,current_year],axis =0)
# print(all_data)

all_data.reset_index(drop=True,inplace=True)
# print(all_data)

print(all_data.isna().any())

all_data.fillna(value=np.mean(all_data),inplace=True)
# print(all_data)

all_data.drop_duplicates(inplace=True)
# print(all_data)

all_data.reset_index(drop=True)
# print(all_data)

# print(all_data.describe())

# print(all_data[all_data["Year"]==2021].describe())
# print(all_data[all_data["Year"]==2022].describe()) 

# print(all_data.sort_values(by="Revenue"))#revenues verilerini küçükten büyüğe doğru sıralar.

# all_data[all_data["Year"]==2022].sort_values(by="Revenue")

# print(all_data["Name"].value_counts())