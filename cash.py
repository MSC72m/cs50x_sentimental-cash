from cs50 import get_float


def get_cents():
    while True:
        cents = get_float("How many cents do you owe? ")
        if cents > 0:
            return cents * 100
        else:
            return get_cents()


def calculate_quarters(cents):
    quarters = 0
    while cents >= 25:
        cents -= 25
        quarters += 1
    return quarters


def calculate_dimes(cents):
    dimes = 0
    while cents >= 10:
        cents -= 10
        dimes += 1
    return dimes


def calculate_nickels(cents):
    nickels = 0
    while cents >= 5:
        cents -= 5
        nickels += 1
    return nickels


def calculate_pennies(cents):
    pennies = 0
    while cents >= 1:
        cents -= 1
        pennies += 1
    return pennies


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


calculation()
