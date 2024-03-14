"""Question Three: Algorithm Analysis Executable Examination."""

# TODO: The imports in the following source code block no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import Dict

# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> You may refer to the checks that are specified in the exam/gatorgrade.yml file
# in this GitHub repository for the configuration and name of each tool used
# to analyze the code inside of this file.

# }}}

# Part (a) {{{

# Instructions:
# Implement the following function that inputs the contents of a file
# so that it adheres to all aspects of the following specification.

# Function specification:
# The function sum_stop_int should:
# - Take an integer, called stop, as its parameter
# - Return an integer that is the sum of all of the numbers up to and including the stop value
# - If the stop value is less than 0, the function should return 0 to indicate an invalid input

# TODO: The provided source code is not correct! To complete this question you should
# write the correct implementation of the function sum_stop_int so that it adheres to the
# given specification.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def sum_stop_int(stop: int) -> int:
    """all of the numbers up to and including the provided stop value."""
    if stop < 0:
        return 0
    return sum(range(stop))


# }}}

# Part (b) {{{

# Instructions:
# Implement the following function that inputs the contents of a file
# so that it adheres to all aspects of the following specification.

# Function specification:
# The function sum_stop_float should:
# - Take a float, called stop, as its first parameter
# - Take a float, called step, as its second parameter
# - Return a float that is the sum of all of the numbers up to and including the stop value
# - The step value should be used to determine the increment between each number in the summation
# - If the stop value is less than 0, the function should return 0 to indicate an invalid input

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def sum_stop_float(stop, step):
    """Sum all of the numbers up to the provided stop value by a given step value."""
    total = 0.0
    return total


# }}}


# Part (c) {{{

# Instructions:
# Implement the following function that inputs the contents of a file
# so that it adheres to all aspects of the following specification.

# Function specification:
# The function sum_function_call_counts should:
# - Take a dictionary, called function_call_data, as its parameter
# - Return an integer that is the sum of all of the counts of function calls in the provided dictionary
# - The dictionary will have string keys and integer values that represent the count of function calls
# - The function should return 0 if the dictionary is empty

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def sum_function_call_counts(function_call_data) -> int:
    total_sum_of_calls = 0
    return total_sum_of_calls


# }}}
