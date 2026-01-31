"""
NTU Assignment - Pandas Basics

This script demonstrates solutions for:
1. Row filtering with threshold
2. Sorting DataFrames
3. Concatenating DataFrames
4. Cumulative sum
5. String transformation

Run:
    python assignment_pandas.py
"""

import pandas as pd


def question_1():
    print("\n--- Question 1: Rows where any value exceeds threshold ---")
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    })
    threshold = 30

    filtered_df = df[df.gt(threshold).any(axis=1)]
    print(filtered_df)


def question_2():
    print("\n--- Question 2: Sort DataFrame by columns A and B ---")
    df = pd.DataFrame({
        'A': [2, 1, 2],
        'B': [2, 3, 1],
        'C': [1, 2, 3]
    })

    sorted_df = df.sort_values(by=['A', 'B'])
    print(sorted_df)


def question_3():
    print("\n--- Question 3: Concatenate DataFrames vertically ---")
    df1 = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df2 = pd.DataFrame({
        'A': [7, 8, 9],
        'B': [10, 11, 12]
    })

    combined_df = pd.concat([df1, df2], ignore_index=True)
    print(combined_df)


def question_4():
    print("\n--- Question 4: Cumulative sum of a column ---")
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

    df['A_cumsum'] = df['A'].cumsum()
    print(df)


def question_5():
    print("\n--- Question 5: Convert Series to uppercase ---")
    series = pd.Series(['apple', 'banana', 'cherry'])

    upper_series = series.str.upper()
    print(upper_series)


def main():
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()


if __name__ == "__main__":
    main()
