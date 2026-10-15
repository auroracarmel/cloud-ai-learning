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

The script handles non-numeric input with a helpful message.
It does not yet reject negative numbers or automatically ask again.


## Dictionary practice

File: dictionary_practice.py

I created a dictionary containing an assistant name and a max_words setting.
I changed max_words from 50 to 100, then retrieved and printed its value.

Expected output: 100
Actual output: 100

I learned:
- A dictionary stores values under keys.
- Square brackets retrieve a value using its key.
- Text keys need quotation marks.
- An assignment can update a dictionary value.

This exercise stores settings locally. It does not call an AI service.



## Request checker

File: request_checker.py

Checks whether a sample request has a description.
Uses .strip() to treat whitespace-only descriptions as missing.

Tests completed:
- Empty description: Missing description.
- Three spaces: Missing description.
- Actual text: Description supplied.

This is fixed-rule automation, not an AI model.