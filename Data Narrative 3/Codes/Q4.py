import pandas as pd
import matplotlib.pyplot as plt


# Load the CSV file into a Pandas dataframe
df = pd.read_csv('./Tennis-Major-Tournaments-Match-Statistics/FrenchOpen-women-2013.csv')

# Create a new dataframe containing only the columns for aces and winners
aces_winners = df[['Player1', 'ACE.1', 'WNR.1']].copy()

# Rename the columns for clarity
aces_winners.columns = ['Player', 'Aces', 'Winners']

# Append the data for the other player in each match to the aces_winners dataframe
other_player = df[['Player2', 'ACE.2', 'WNR.2']].copy()
other_player.columns = ['Player', 'Aces', 'Winners']
aces_winners = aces_winners.append(other_player)

# Group the data by player and sum the number of aces and winners for each player
grouped = aces_winners.groupby('Player').sum()
print(grouped)

# Sort the players by the number of aces and winners, in descending order
sorted_players_aces = grouped.sort_values('Aces', ascending=False)
sorted_players_winners = grouped.sort_values('Winners', ascending=False)

font1 = {'family':'Sans','color':'blue','size':15}
font2 = {'family':'serif','color':'darkred','size':15}

plt.subplot(1,2,1)
plt.bar(sorted_players_aces.head(3).index, sorted_players_aces.head(3)['Aces'], color = "orange")
plt.xlabel("Player", fontdict = font2)
plt.ylabel("Total Number of Aces", fontdict = font2)
plt.title("Top 3 players who hit aces in the tournament", fontdict = font1)

plt.subplot(1,2,2)
plt.bar(sorted_players_winners.head(3).index, sorted_players_winners.head(3)['Winners'], color = "#3567BF")
plt.xlabel("Player", fontdict = font2)
plt.ylabel("Total number of Winners", fontdict = font2)
plt.title("Top 3 players who hit winnners in the tournament", fontdict = font1)

plt.show()



