# Python Stock Checker

A beginner Python exercise completed as part of my cloud and AI learning.

## What it does

Asks for the number of laptops in stock.
Displays "Low stock" when the number is below 3.
Otherwise, displays "Stock available".

## How to run

With Python installed, open PowerShell in the python-basics folder:

```powershell
py stock_checker.py
```

## Tests I ran

| Input | Expected output | Actual output |
|---|---|---|
| 13 | Stock available | Stock available |
| 2 | Low stock | Low stock |

## What I learned

- Collecting text with input().
- Converting text to an integer with int().
- Making decisions with if and else.
- Using colons and indentation.
- Running a saved Python script from PowerShell.
- Using cd with a quoted folder path.

## Current limitations

The script does not yet handle non-numeric input or reject negative numbers.