import pytest
import pandas as pd

# Test to ensure the filtered data contains only the required platforms
def test_platform_filter():
    platforms = ['PS4', 'XOne', 'PC', 'WiiU']
    data = pd.read_csv('dataset.csv')
    filtered_data = data[data['platform'].isin(platforms)]
    assert all(filtered_data['platform'].isin(platforms)), "Filtered data contains unwanted platforms"

# Test to check that genre counts are correctly grouped
def test_genre_counts():
    data = pd.read_csv('dataset.csv')
    platforms = ['PS4', 'XOne', 'PC', 'WiiU']
    filtered_data = data[data['platform'].isin(platforms)]
    genre_counts = filtered_data.groupby(['platform', 'genre']).size().reset_index(name='Count')
    assert 'Count' in genre_counts.columns, "Count column not found in grouped data"
    assert genre_counts['Count'].dtype == 'int64', "Count column is not of integer type"
