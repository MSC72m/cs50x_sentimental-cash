# Cash Python Program

## Project Description
This project is a solution to a CS50x problem set that involves implementing a coin counting program in Python. The program calculates the minimum number of coins (quarters, dimes, nickels, and pennies) needed to make a given amount of cents. It prompts the user for the amount in cents and then determines the fewest number of each coin needed to make that amount.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Explanation](#algorithm-explanation)
- [Code Explanation](#code-explanation)

## Installation
No special installation is required for this project. Ensure you have Python and the CS50 library available.

## Usage
To run the project, use the following command:
```sh
python coin_counter.py
```
You will be prompted to enter the amount of cents, and the program will output the minimum number of coins needed.

### Algorithm Explanation
The coin counting algorithm is designed to minimize the number of coins needed to make change for a given amount of cents. The algorithm works as follows:

Get Cents:
Prompt the user to input a positive number of cents. Repeat the prompt if the input is invalid (negative value or zero).
Calculate Coins:
Calculate Quarters: Determine the number of quarters (25-cent coins) needed.
Calculate Dimes: Determine the number of dimes (10-cent coins) needed after quarters.
Calculate Nickels: Determine the number of nickels (5-cent coins) needed after dimes.
Calculate Pennies: Determine the number of pennies (1-cent coins) needed after nickels.
Output the Result:
Sum the total number of coins and print the result.

## Code Explanation
Importing Libraries
``` python
from cs50 import get_float
```
from cs50 import get_float: Imports the get_float function from the CS50 library to handle user input.
Getting Cents
``` python
def get_cents():
    while True:
        cents = get_float("How many cents do you owe? ")
        if cents > 0:
            return cents * 100
        else:
            return get_cents()
```
Function get_cents:
Prompts the user for the amount in cents.
Ensures the input is a positive number.
Converts dollars to cents by multiplying by 100.
Calculate Quarters Function
``` python
def calculate_quarters(cents):
    quarters = 0
    while cents >= 25:
        cents -= 25
        quarters += 1
    return quarters
```
Function calculate_quarters:
Calculates the number of quarters (25-cent coins).
Subtracts the value of each quarter from the total cents.
Calculate Dimes Function
python
Copy code
def calculate_dimes(cents):
    dimes = 0
    while cents >= 10:
        cents -= 10
        dimes += 1
    return dimes
Function calculate_dimes:
Calculates the number of dimes (10-cent coins).
Subtracts the value of each dime from the total cents.
Calculate Nickels Function
``` python
def calculate_nickels(cents):
    nickels = 0
    while cents >= 5:
        cents -= 5
        nickels += 1
    return nickels
```
Function calculate_nickels:
Calculates the number of nickels (5-cent coins).
Subtracts the value of each nickel from the total cents.
Calculate Pennies Function
``` python
def calculate_pennies(cents):
    pennies = 0
    while cents >= 1:
        cents -= 1
        pennies += 1
    return pennies
```
Function calculate_pennies:
Calculates the number of pennies (1-cent coins).
Subtracts the value of each penny from the total cents.
Calculation Function
``` python
def calculation():
    cents = get_cents()
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5
    pennies = calculate_pennies(cents)
    coins = quarters + dimes + nickels + pennies
    print(coins)
```
Function calculation:
Orchestrates the process of calculating the total number of coins.
Calls get_cents to get the total amount in cents.
Uses the coin calculation functions to determine the number of each type of coin.
Sums the total number of coins and prints the result.
Main Execution
``` python
calculation()
```
Calls the calculation function to execute the program.
