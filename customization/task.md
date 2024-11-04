
# Customization Instructions

1. Customize the bar chart with colors, labels, and legend position.
2. Ensure the chart matches the required style.

## Task
- Add customizations to the chart, like colors and labels.

## Theory
- Learn how to use seaborn/matplotlib to style charts.

## Example Code
```python
plt.figure(figsize=(10, 6))
sns.barplot(data=genre_counts, x='Platform', y='Count', hue='Genre', palette='muted')
plt.xlabel('Platform')
plt.ylabel('Count')
plt.title('Game Genres by Platform')
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
```
