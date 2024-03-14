"""Question Two: Algorithm Analysis Executable Examination."""

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
# The function reverse_str should:
# - Take a string, called data, as its parameter
# - Return a string that represents the reverse of the input string
# - The input string may contain any characters that are valid according to unicode

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def reverse_str(data):
    """Reverse the content of the provided string."""
    return ""


# }}}

# Part (b) {{{

# Instructions:
# Implement the following function that inputs the contents of a file
# so that it adheres to all aspects of the following specification.

# Function specification:
# The function reverse_number should:
# - Take an integer, called data, as its parameter
# - Return an integer that represents the reverse of the input number
# - The input number may be any integer value according to the Python programming language

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def reverse_number(data: int) -> int:
    return 0


# }}}


# Part (c) {{{

# Instructions:
# Implement the following function that inputs the contents of a file
# so that it adheres to all aspects of the following specification.

# Function specification:
# The function reverse_count should:
# - Take a string, called data, as its parameter
# - Return a dictionary that represents the count and reverse of the input string
# - The input string may contain any characters that are valid according to unicode
# - The dictionary should have the following structure:
#   - The key should be the input string
#   - The value of this key should include the following key-value pairs:
#     - "count" is the key and the value is the number of characters in the input string
#     - "reversed" is the key and the value is the reverse of the input string

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def reverse_count(data: str):
    """Reverse the content of the provided string and return it in a mapping."""
    return {}


# }}}
