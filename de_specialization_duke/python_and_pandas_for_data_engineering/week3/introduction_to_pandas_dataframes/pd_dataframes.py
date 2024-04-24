import pandas as pd

# Create from Dictionary

data = {
    'Name': ['Carl', 'Carol', 'Cas'],
    'Age': [43, 23, 30],
    'Score': [123, 168, 14]
}

df_dict = pd.DataFrame(data)
print('From dict: \n', df_dict)

# Create from list of lists
data = [
    ['Carl', 43, 123],
    ['Carol', 23, 168],
    ['Cas', 30, 14]
]

df_list = pd.DataFrame(data, columns=['Name', 'Age', 'Score'])
print('\nFrom lists: \n', df_list)

# Create from file
file_path = 'de_specialization_duke/USCG.Search.Rescue.Stats.csv'
df_file = pd.read_csv(file_path)

print('\nFrom file: \n', df_file)
