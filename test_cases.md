# Simple Data Filtering — Test Cases

## Testing Objective

To verify that student records are correctly filtered using marks, age, department, and combined conditions.

## Test Cases

| Test ID | Input / Scenario | Expected Result |
|---|---|---|
| TC01 | Display all students | Eight records displayed |
| TC02 | Minimum marks = 80 | Five students returned |
| TC03 | Minimum marks = 95 | One student returned |
| TC04 | Maximum age = 21 | Four students returned |
| TC05 | Department = Data Science | Priya and Kiran returned |
| TC06 | Department = data science | Same two students returned |
| TC07 | Minimum marks = 80 and age < 21 | Arun and Kiran returned |
| TC08 | Minimum marks = 100 | No matching students |
| TC09 | Minimum marks = 110 | Input rejected |
| TC10 | Enter non-numeric marks | Error message displayed |
| TC11 | Enter an unknown department | No matching students |
| TC12 | Enter an invalid menu choice | Error message displayed |

## Test Execution Record

Run each test and record the actual outcome.

| Test ID | Actual Result | Status |
|---|---|---|
| TC01–TC12 | Record after execution | Pending |

## Testing Notes

The minimum marks condition uses greater-than-or-equal-to (>=). The age condition uses less-than (<). Department matching ignores capitalization.

Combined filtering uses AND logic, so both conditions must be satisfied.

Only mark a test as passed after confirming the actual output.

## Testing Conclusion

These tests verify the core filtering functions and help identify errors in condition handling and user input validation.
