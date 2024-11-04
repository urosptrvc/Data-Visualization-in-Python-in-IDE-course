
# Plotting Instructions

1. Use seaborn or matplotlib to create a bar chart.
2. Set `Platform` as the x-axis, `Count` as the y-axis, and color by `Genre`.

## Task
- Use the grouped data to plot a bar chart.

## Theory
- Learn basic bar chart plotting in seaborn or matplotlib.

## Example Code
```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.barplot(data=genre_counts, x='Platform', y='Count', hue='Genre')
plt.legend(title='Genre')
plt.show()
```
