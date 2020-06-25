"""This time we want to write calculations using functions and get the results. Let's have a look at some examples:

JavaScript:

seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3

Ruby:

seven(times(five)) # must return 35
four(plus(nine)) # must return 13
eight(minus(three)) # must return 5
six(divided_by(two)) # must return 3

Requirements:

    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy
    (divided_by in Ruby)
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Divison should be integer division, e.g eight(dividedBy(three()))/eight(divided_by(three)) should return 2, not
     2.666666...

Available at: https://www.codewars.com/kata/calculating-with-functions/train/python

"""
# solution


def helper(number_function, operation_operand):
    function_name = number_function.__name__
    function_to_number = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    number = function_to_number[function_name]
    if operation_operand[0] == '+':
        return number + operation_operand[1]
    elif operation_operand[0] == '-':
        return number - operation_operand[1]
    elif operation_operand[0] == '*':
        return number * operation_operand[1]
    elif operation_operand[0] == '/':
        return int(number / operation_operand[1])


def zero(operation_operand=None):
    if operation_operand:
        return helper(zero, operation_operand)
    return 0


def one(operation_operand=None):
    if operation_operand:
        return helper(one, operation_operand)
    return 1


def two(operation_operand=None):
    if operation_operand:
        return helper(two, operation_operand)
    return 2


def three(operation_operand=None):
    if operation_operand:
        return helper(three, operation_operand)
    return 3


def four(operation_operand=None):
    if operation_operand:
        return helper(four, operation_operand)
    return 4


def five(operation_operand=None):
    if operation_operand:
        return helper(five, operation_operand)
    return 5


def six(operation_operand=None):
    if operation_operand:
        return helper(six, operation_operand)
    return 6


def seven(operation_operand=None):
    if operation_operand:
        return helper(seven, operation_operand)
    return 7


def eight(operation_operand=None):
    if operation_operand:
        return helper(eight, operation_operand)
    return 8


def nine(operation_operand=None):
    if operation_operand:
        return helper(nine, operation_operand)
    return 9


def times(operand):
    return '*', operand


def plus(operand):
    return '+', operand


def minus(operand):
    return '-', operand


def divided_by(operand):
    return '/', operand


# Examples
print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))
