import pandas as pd

dataset = pd.read_csv('data.csv')

dataset = dataset.drop(['Period', 'Dynasty', 'Reign', 'Portfolio', 'Subregion', 'Locale', 'Locus', 'Excavation', 'River'], axis=1)

#Visualize the various countries from where the artworks are coming.
df = dataset.iloc[:,[5,27]]
df = df.dropna()
country = df['Country'].unique()
print('Country that are giving art work : ')
print(country)

#Visualize the top 2 classification for the artworks
df = dataset['Classification']
df = df.dropna()
z = df.value_counts().head(2)
print('top 2 classification of art work : ')
print(z.keys())

#Visualize the artist interested in the artworks
df = dataset['Artist Display Name']
df = df.dropna()
z = df.value_counts()

#Visualize the top 2 culture for the artworks
df = dataset['Culture']
df = df.dropna()
z = df.value_counts.head(2)
print('top 2 culture of art work : ')
print(z.keys())