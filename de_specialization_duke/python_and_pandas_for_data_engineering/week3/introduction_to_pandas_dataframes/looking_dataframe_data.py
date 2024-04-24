import pandas as pd

file_path = 'de_specialization_duke/USCG.Search.Rescue.Stats.csv'
df = pd.read_csv(file_path)

# Display first x rows (5 by default)
print(df.head(3))

# Display bottom x rows (5 by default)
print(df.tail(2))

# Descriptive Statistics
print(df.describe())

print(df.min())
print()
print(df.std())

# Selecting Columns
print('\nColumn names\n')
print(df.columns)

print('\n Selecting a single column \n')
print(df['Cases'])  # Can also use df.Cases directly

print('\n Selecting multiple columns \n')
# Returns a dataframe with the selected data from the original dataframe
print(df[['Cases', 'Sorties']])


# Selecting columns and rows the optimal way

# iloc selects depending on index
# first arg is the row, second the columns
print('\nSelecing with iloc\n')
print(df.iloc[3:29, 3])


# loc selects using labels names
# first arg is the row, second the columns
print('\nSelecing with loc\n')
print(df.loc[1965:1974, ['Cases', 'Sorties']])
