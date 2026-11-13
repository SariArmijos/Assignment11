#Import pandas
import pandas as pd
# Read the CSV file using Pandas.
video_games = pd.read_csv("video_games_raw.csv")

#TASK 1

# Ask the user for a specific row number to inspect.
row_number = int(input("Which row would you like to inspect?: "))
#I have added a while loop just in case user selects row o instead of starting at 1 or choose a row that does not exist in the database
while row_number <= 0 or row_number > len(video_games):
    row_number = int(input("Invalid number. Which row would you like to inspect?: "))
#I will assume that users wiill insert rows starting from 1
# Use .iloc[] to display information about the selected game.
#I have used - 2 to account for the title and index 0
print(video_games.iloc[row_number - 2])
# Ask the user to enter a new status for that game, such as Backlog, Playing, Completed, or Dropped.
new_status = str(input("What's the new status for the game? (Backlog, Playing, Completed, or Dropped): "))
# Use .at[] to update the selected game
video_games.at[row_number - 2, "Status"] = new_status

print(video_games)

#TASK 2