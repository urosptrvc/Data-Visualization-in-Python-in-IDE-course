import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('dataset.csv')

# Filter for specific platforms
platforms = ['PS4', 'XOne', 'PC', 'WiiU']
filtered_data = data[data['platform'].isin(platforms)]

# Group and count genres by platform
genre_counts = filtered_data.groupby(['platform', 'genre']).size().reset_index(name='Count')

# Set the order of the platforms
platform_order = ['PS4', 'XOne', 'PC', 'WiiU']

# Plotting
plt.figure(figsize=(14, 6))
sns.barplot(data=genre_counts, x='platform', y='Count', hue='genre', palette='muted', order=platform_order)
plt.xlabel('Platform')
plt.ylabel('Count')
plt.title('Game Genres by Platform')
plt.legend(title='Genre', bbox_to_anchor=(1, 1), loc='upper left')
plt.show()
