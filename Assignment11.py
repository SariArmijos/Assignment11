# Import pandas
import pandas as pd
# Read the CSV file using Pandas.
video_games = pd.read_csv("video_games_raw.csv")

#TASK 1

# Ask the user for a specific row number to inspect.
row_number = int(input("Which row would you like to inspect?: "))
# I have added a while loop just in case user selects row o instead of starting at 1 or choose a row that does not exist in the database
while row_number <= 0 or row_number > len(video_games):
    row_number = int(input("Invalid number. Which row would you like to inspect?: "))
# I will assume that users will insert rows starting from 1
# Use .iloc[] to display information about the selected game.
# I have used - 2 to account for the title and index 0
print(video_games.iloc[row_number -1])
# Ask the user to enter a new status for that game, such as Backlog, Playing, Completed, or Dropped.
new_status = str(input("What's the new status for the game? (Backlog, Playing, Completed, or Dropped): "))
# Use .at[] to update the selected game
video_games.at[row_number -1, "Status"] = new_status

#print(video_games)

#TASK 2
# Add a Recommended column to the panda.
    #I will initially set all the columns as No and later based on filter put Yes
video_games["Recommended"] = "No"
# Set Recommended to Yes for games that meet both of these criteria:
    # Rating is at least 8.
    # Price is $40 or less.
#I used .loc[] because I will change the values, each condition will go in parenthesis
video_games.loc[(video_games["Rating"] >= 8) & (video_games["Price"] <= 40), "Recommended"] = "Yes"
# Set Recommended to No for all other games.
    #Previously set
# Use .query() to display the recommended games.
print("\nRecommended games\n")
print(video_games.query("Recommended == 'Yes'"))
#Save the updated data to a new file named video_games_cleaned.csv.
    #Add index = False so the document does not save with the index as an extra column
video_games.to_csv("video_games_cleaned.csv", index = False)
print("The updated document has been saved as 'video_games_cleaned.csv'")