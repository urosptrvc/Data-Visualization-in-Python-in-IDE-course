import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.barplot(data=genre_counts, x='Platform', y='Count', hue='Genre')
plt.legend(title='Genre')
plt.show()