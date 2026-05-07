
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


# most_wins = df['WinningTeam'].value_counts()
# print("Most winning team:\n", most_wins.head(10))

# host_city = df['City'].value_counts()
# print("Most Hosted City:\n", host_city.head())

# df["toss_match_win"]= df["TossWinner"] == df["WinningTeam"]

# print(df["toss_match_win"].value_counts())

# print(df["Player_of_Match"].value_counts().head(10))

plt.figure(figsize=(15,10))
top_teams = df['WinningTeam'].value_counts().head(8)
sns.barplot(x=top_teams.index, y=top_teams.values)
plt.title('IPL - Most Wins by Team', fontsize=14, fontweight='bold')
plt.xlabel('Team')
plt.ylabel('Number of Wins')
plt.tight_layout()

plt.savefig('team_wins.png')
plt.show()
print("Chart 1 saved!")

plt.figure(figsize=(10,5))
toss_counts = df['TossDecision'].value_counts()
plt.pie(toss_counts.values, 
        labels=toss_counts.index, 
        autopct='%1.1f%%', 
        colors=['#ff9999','#66b3ff'],
        startangle=90)
plt.title('Toss Decision - Bat vs Field', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('toss_decision.png')
plt.show()
print("Chart 2 saved!")

plt.figure(figsize=(8, 4))
top_potm = df['Player_of_Match'].value_counts().head(5)
sns.barplot(x=top_potm.values, y=top_potm.index, palette='Greens_r')
plt.title('Top 5 Player of the Match', fontsize=14, fontweight='bold')
plt.xlabel('Number of Awards')
plt.ylabel('Player of Match')
plt.tight_layout()
plt.savefig('top_players.png')
plt.show()
print("Chart 3 saved!")