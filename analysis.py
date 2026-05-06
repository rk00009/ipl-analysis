
import pandas as pd

df = pd.read_csv(r'c:\91931\archive\IPL_Matches_2022.csv')

# print(df.shape) #how many row and columns?
# print(df.head()) #first 5 rows
# print(df.info()) #column names + data types
# print(df.describe()) #stats summary
# print(df.columns) # all column names

#Clean the data
#First check for missing values
print(df.isnull().sum())

#handle missing data
# df['WinningTeam'] = df['WinningTeam'].fillna('No Result')
# df = df.dropna(subset=['City'])
# print(df.isnull().sum())


most_wins = df['WinningTeam'].value_counts()
print("Most winning team:\n", most_wins.head(10))

host_city = df['City'].value_counts()
print("Most Hosted City:\n", host_city.head())

df["toss_match_win"]= df["TossWinner"] == df["WinningTeam"]

print(df["toss_match_win"].value_counts())

print(df["Player_of_Match"].value_counts().head(10))