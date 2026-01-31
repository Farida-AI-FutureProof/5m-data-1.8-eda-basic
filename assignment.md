# Assignment

## Brief

Write the Python codes for the following questions.

## Instructions

Paste the answer as Python in the answer code section below each question.

### Question 1

Question: How do you select rows from a DataFrame where any value in the row exceeds a threshold?

```python
filtered_df = df[df.gt(threshold).any(axis=1)]

```

Answer:

```python

```

### Question 2

Question: How do you sort a DataFrame by columns `A` and `B`?

```python
sorted_df = df.sort_values(by=['A', 'B'])

```

Answer:

```python

```

### Question 3

Question: How do you concatenate two DataFrames vertically?

```python
combined_df = pd.concat([df1, df2], ignore_index=True)

```

Answer:

```python

```

### Question 4

Question: How do you compute the cumulative sum of a column in a DataFrame?

```python
df['A_cumsum'] = df['A'].cumsum()

```

Answer:

```python

```

### Question 5

Question: How do you convert a Series of strings to uppercase?

```python
import pandas as pd

series = pd.Series(['apple', 'banana', 'cherry'])
```

Answer:

```python
upper_series = series.str.upper()

```

## Submission

- Submit the URL of the GitHub Repository that contains your work to NTU black board.
- Should you reference the work of your classmate(s) or online resources, give them credit by adding either the name of your classmate or URL.
