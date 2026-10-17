# Simple Data Filtering Using Python

## Project Overview

Simple Data Filtering is a Python program that filters student records according to marks, age, and department.

The project uses a list of dictionaries to represent structured student data and conditional statements to select records that satisfy specified criteria.

## Objective

To understand how conditions can be used to filter structured data and extract relevant records from a collection.

## Features

- Display all student records.
- Filter students by minimum marks.
- Filter students by maximum age.
- Filter students by department.
- Combine marks and age conditions.
- Handle invalid input and empty results.

## Technologies Used

- Python 3
- Lists and dictionaries
- Conditional statements
- List comprehensions
- Visual Studio Code
- GitHub

## Dataset

The program contains eight manually created fictional student records with the following fields:

- Student ID
- Name
- Age
- Department
- Marks

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Open a terminal.
5. Execute:

`python data_filtering.py`

On Windows, you can also try:

`py data_filtering.py`

## Filtering Conditions

- **Marks:** Selects students whose marks are greater than or equal to the chosen minimum.
- **Age:** Selects students whose age is less than the specified maximum.
- **Department:** Selects students belonging to the specified department.
- **Combined filtering:** Selects students satisfying both the minimum marks and maximum age conditions.

## Concepts Learned

- Lists and dictionaries
- Conditional statements
- Comparison operators
- Logical operators
- List comprehensions
- Functions
- Input validation
- Structured data filtering

## Limitations and Future Improvements

The current project uses a manually created dataset. Changes to the data require editing the Python code.

Future improvements could include reading records from CSV or Excel files, using Pandas DataFrames, and developing an interactive dashboard.

## Conclusion

This project demonstrates how Python can filter structured student data using conditional expressions. It provides practical experience with basic data-processing techniques that can be extended to larger datasets.
