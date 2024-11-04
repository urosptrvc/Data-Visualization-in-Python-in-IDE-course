
# Setup Instructions

1. Install required packages: `pandas`, `seaborn` (or `matplotlib` if preferred).
2. Load the dataset using `pandas`.

## Task
- Load the dataset `dataset.csv` and check its initial rows to ensure proper loading.

## Theory
- Learn how to use `pandas` to load CSV files.

## Example Code
```python
import pandas as pd

# Load the dataset
data = pd.read_csv('dataset.csv')
print(data.head())
```
