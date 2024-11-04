
# Data Preparation Instructions

1. Filter the data to include only the platforms PS4, XOne, PC, and WiiU.
2. Group the data by `Platform` and `Genre` to get the count of each genre per platform.

## Task
- Filter the dataset for the specified platforms and group by `Platform` and `Genre`.

## Theory
- Learn how to filter data and group in `pandas`.

## Example Code
```python
# Filter for specific platforms
platforms = ['PS4', 'XOne', 'PC', 'WiiU']
filtered_data = data[data['Platform'].isin(platforms)]

# Group and count genres by platform
genre_counts = filtered_data.groupby(['Platform', 'Genre']).size().reset_index(name='Count')
print(genre_counts.head())
```
