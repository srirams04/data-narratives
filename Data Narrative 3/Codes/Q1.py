import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV file
data = pd.read_csv("./Tennis-Major-Tournaments-Match-Statistics/AusOpen-men-2013.csv")
big_3 = {"Roger Federer": [0,0], "Novak Djokovic": [0,0], "Rafael Nadal": [0,0]}

for name in big_3:
    sum_wins = 0
    sum_losses = 0
    for i in (1,2):
        x = data[(data[f'Player{i}'] == name) & (data['Result'] == (i % 2))]
        y = data[(data[f'Player{i}'] == name) & (data['Result'] != (i % 2))]
    
        sum_wins += x[f'FSP.{i}'].sum()/x.shape[0] if x.shape[0] != 0 else 0
        sum_losses += y[f'FSP.{i}'].sum()/y.shape[0] if y.shape[0] != 0 else 0
    big_3[name] = [sum_wins, sum_losses]

# Create pie charts for each player
plt.figure(figsize=(25,25))

for i, name in enumerate(big_3):
    plt.subplot(1, 3, (i+1))
    plt.pie(big_3[name], labels=["Wins", "Losses"], autopct='%1.1f%%')
    plt.title(f"{name}\nFirst Serve Percentage in Games Won vs Lost")
plt.tight_layout()
plt.show()
