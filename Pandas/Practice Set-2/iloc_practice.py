import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('matches.csv')

# Displaying initial shape and sample of the dataframe
df.info()
df.describe()

# Retrieve specific columns like 'date', 'city', 'team1', 'team2', 'winner'
df[['date', 'city', 'team1', 'team2', 'winner']].shape

# Viewing shape of just the 'winner' column
df['winner'].shape

# Using iloc for data extraction with row and column indices
df.iloc[1:4]  # Fetch rows 2, 3, 4 (Python index starts from 0)

# Load CSV with index set to 'id' column
df1 = pd.read_csv('matches.csv', index_col=['id'])

# First few rows using iloc
df1.iloc[:4]

# Using step size in iloc to fetch every 5th row up to 40th row and slicing specific columns
df.iloc[:40:5, 1:30]

# Retrieve the first match's entire row
df.iloc[0]

# Fetch the last match's entire row
df.iloc[-1]

# Get the match data from the 5th row
df.iloc[4]

# Fetch 'team1' and 'team2' for the 10th match
df[['team1', 'team2']].iloc[9]

# Retrieve 'city', 'venue', and 'date' for the first match
df[['city', 'date', 'venue']].iloc[0]

# Fetch 'player_of_match', 'winner', and 'toss_winner' for the 20th match
df[['player_of_match', 'winner', 'toss_winner']].iloc[19]

# Fetch 'win_by_runs' and 'win_by_wickets' up to the 15th match
df[['win_by_runs', 'win_by_wickets']].iloc[:14]

# Fetch match data for rows 2 to 5
df.iloc[1:5]

# Fetch 'umpire1' and 'umpire2' for rows 3 to 7
df[['umpire1', 'umpire2']].iloc[2:7]

# Retrieve all columns for matches at rows 12, 14, and 16
df.iloc[11:16:2]

# Get 'date', 'city', 'venue', and 'player_of_match' for every 10th match
df[['date', 'city', 'venue', 'player_of_match']].iloc[::10]

# Fetch all details for the 10th, 20th, and 30th matches
df.iloc[9:39:10]

# Retrieve 'winner', 'player_of_match', and 'win_by_runs' for every 5th match
df[['winner', 'player_of_match', 'win_by_runs']].iloc[::5]

# Extract all match information for rows from 50 to 100
df.iloc[50:101]

# Fetch every second match between rows 20 to 50
df.iloc[20:51:2]

# Retrieve 'team1' and 'team2' for the first 10 matches played in Hyderabad
hyderabad = df[df['city'] == 'Hyderabad']
hyderabad[['team1', 'team2']].iloc[:10]

# Get 'winner', 'win_by_runs', and 'win_by_wickets' for the first 20 matches where Royal Challengers Bangalore played
rcb = df[(df['team1'] == 'Royal Challengers Bangalore') | (df['team2'] == 'Royal Challengers Bangalore')]
rcb[['winner', 'win_by_runs', 'win_by_wickets']].iloc[:20]

# Fetch 'umpire1', 'umpire2', and 'umpire3' for matches where D/L method was applied
dl_applied = df[df['dl_applied'] == 1]
dl_applied[['umpire1', 'umpire2', 'umpire3']]

# Retrieve entire data for matches won by Mumbai Indians and fetch specific rows using iloc
mi = df[df['winner'] == 'Mumbai Indians']
mi.iloc[2:30]

# Get match data for rows where 'win_by_wickets' is greater than 5
greater = df[df['win_by_wickets'] > 5]
greater.iloc[2:30]

# Fetch 'date', 'city', and 'winner' for matches where 'toss_decision' was "bat"
toss_decision = df[df['toss_decision'] == 'bat']
toss_decision[['date', 'city', 'winner']].iloc[:31]

# Retrieve 'team1', 'team2', and 'player_of_match' for matches in 2017 with more than 100 runs victory
match2017 = df[(df['date'] >= '2017-01-01') & (df['date'] < '2018-01-01')]
more_than_100 = match2017[match2017['win_by_runs'] > 100]
more_than_100[['team1', 'team2', 'player_of_match']]

# Get 'venue', 'city', 'date', and 'winner' for the first 5 matches that Sunrisers Hyderabad won
srh = df[df['winner'] == 'Sunrisers Hyderabad']
srh[['date', 'venue', 'city', 'winner']].iloc[:5]

# Fetch 'toss_winner', 'toss_decision', and 'winner' for matches where 'toss_winner' is the same as 'winner'
same = df[df['toss_winner'] == df['winner']]
same[['toss_winner', 'toss_decision', 'winner']]

# Retrieve match data for top 10 matches with the highest 'win_by_runs' values
sorted_values = df.sort_values(by='win_by_runs', ascending=False)
sorted_values.iloc[:10]
