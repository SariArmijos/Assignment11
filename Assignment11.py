#Import pandas
import pandas as pd
# Read the CSV file using Pandas.
video_games = pd.read_csv("video_games_raw.csv")
# Ask the user for a specific row number to inspect.
row_number = int(input("Which row would you like to inspect?: "))
# Use .iloc[] to display information about the selected game.
print(video_games.iloc[row_number - 1])
# Ask the user to enter a new status for that game, such as Backlog, Playing, Completed, or Dropped.
new_status = str(input("What's the new status for the game? (Backlog, Playing, Completed, or Dropped): "))
# Use .at[] to update the selected game
video_games.at[row_number, "Status"] = new_status

print(video_games)