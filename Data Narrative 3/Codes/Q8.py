import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas dataframe
df = pd.read_csv('./Tennis-Major-Tournaments-Match-Statistics/Wimbledon-women-2013.csv')

net_points_attempted = df[['Player1', 'NPA.1']].copy()

# Rename the columns for clarity
net_points_attempted.columns = ['Player', 'Net Points Attempted']

other_player = df[['Player2', 'NPA.2']].copy()
other_player.columns = ['Player', 'Net Points Attempted']
net_points_attempted = net_points_attempted.append(other_player)

grouped = net_points_attempted.groupby('Player').sum()

sorted_players = grouped.sort_values('Net Points Attempted', ascending=False)
print(sorted_players.head(5))