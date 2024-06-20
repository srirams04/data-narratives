import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas dataframe
df = pd.read_csv('./Tennis-Major-Tournaments-Match-Statistics/USOpen-men-2013.csv')

break_point_winners = df[['Player1', 'BPW.1']].copy()

# Rename the columns for clarity
break_point_winners.columns = ['Player', 'Break Points Won']

other_player = df[['Player2', 'BPW.2']].copy()
other_player.columns = ['Player', 'Break Points Won']
break_point_winners = break_point_winners.append(other_player)

grouped = break_point_winners.groupby('Player').sum()

sorted_players = grouped.sort_values('Break Points Won', ascending=False)
print(sorted_players.head(10))