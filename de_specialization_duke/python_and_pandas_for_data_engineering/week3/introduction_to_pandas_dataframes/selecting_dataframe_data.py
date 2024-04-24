import pandas as pd

file_path = 'de_specialization_duke/USCG.Search.Rescue.Stats.csv'
df = pd.read_csv(file_path)

print(df.head(2))

mask = [False for _ in range(len(df))]
mask[3:7] = [True] * 4

# Returns only the rows that had a true value that matched to their row position
print(df[mask])
print(df.loc[mask])

# Creating a mask using comparison operators
print('\n\n')
mask = df.loc[:, 'Lives Lost After CG Notification'] < df.loc[:,
                                                              'Lives Lost Before CG Notification']
print(df[mask])

# Pandas boolean operators
# AND: &
# OR: |
# NOT: ~

print('\n\n')
mask = (df.loc[:, 'Cases'] < 60000) & (df.loc[:, 'Sorties'] > 4500)
print(df[mask])

# Creating new column
print('\n\n')
df.loc[:, 'Saved per Sortie'] = df.loc[:, 'Lives Saved'] / df.loc[:, 'Sorties']
print(df.columns)
print('\n\n')
print(df['Saved per Sortie'])
