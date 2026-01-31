import pandas as pd

# Sample DataFrame for demonstration
df = pd.DataFrame({
    'A': [1, 5, 3],
    'B': [2, 1, 6],
    'C': [0, 4, 2]
})

threshold = 4

# Question 1:
# Select rows where any value in the row exceeds a threshold
filtered_df = df[df.gt(threshold).any(axis=1)]
print("Filtered DataFrame:")
print(filtered_df)

# Question 2:
# Sort DataFrame by columns A and B
sorted_df = df.sort_values(by=['A', 'B'])
print("\nSorted DataFrame:")
print(sorted_df)

# Question 3:
# Concatenate two DataFrames vertically
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

combined_df = pd.concat([df1, df2], ignore_index=True)
print("\nConcatenated DataFrame:")
print(combined_df)

# Question 4:
# Compute cumulative sum of column A
df['A_cumsum'] = df['A'].cumsum()
print("\nDataFrame with Cumulative Sum:")
print(df)

# Question 5:
# Convert a Series of strings to uppercase
series = pd.Series(['apple', 'banana', 'cherry'])
upper_series = series.str.upper()
print("\nUppercase Series:")
print(upper_series)
