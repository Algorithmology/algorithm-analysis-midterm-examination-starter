"""Confirm the correctness of functions in question_two."""

import pytest

# ruff: noqa: PLR2004
from questions.question_two import (
    reverse_count,
    reverse_number,
    reverse_str,
)


def assert_and_print(expected, actual, message):
    """Print a diagnostic message and assert that the expected and actual values are equal."""
    print(f"{message}: Expected {expected}, got {actual}")
    assert expected == actual


def demarcate():
    """Demarcate test output."""
    print("test_question_two.py")


@pytest.mark.question_two_part_a
def test_reverse_string():
    """Confirm correctness of question part."""
    demarcate()
    # check 1: short string with even number of characters
    string = "hello!"
    reversed_string = reverse_str(string)
    assert_and_print("!olleh", reversed_string, "Even number of characters")
    # check 2: short string with odd number of characters
    string = "world"
    reversed_string = reverse_str(string)
    assert_and_print("dlrow", reversed_string, "Odd number of characters")
    # check 3: short string with non-standard characters
    string = "$%^&*"
    reversed_string = reverse_str(string)
    assert_and_print("*&^%$", reversed_string, "Non-standard characters")
    # check 4: empty string
    string = ""
    reversed_string = reverse_str(string)
    assert_and_print("", reversed_string, "Empty string of no characters")


@pytest.mark.question_two_part_b
def test_reverse_number():
    """Confirm correctness of question part."""
    demarcate()
    # check 1: short number with even number of numerals
    number = 4321
    reversed_number = reverse_number(number)
    assert_and_print(1234, reversed_number, "Even number of numerals")
    # check 2: short number with odd number of numerals
    number = 54321
    reversed_number = reverse_number(number)
    assert_and_print(12345, reversed_number, "Odd number of numerals")
    # check 3: short number with non-standard numerals
    number = 12340000
    reversed_number = reverse_number(number)
    assert_and_print(4321, reversed_number, "Non-standard numerals")
    # check 4: empty number
    number = 0
    reversed_number = reverse_number(number)
    assert_and_print(0, reversed_number, "Empty number of no numerals")


@pytest.mark.question_two_part_c
def test_reverse_count():
    """Confirm correctness of question part."""
    demarcate()
    # check 1: short string with even number of characters
    string = "hello!"
    reversed_string = reverse_count(string)
    expected = {"hello!": {"count": "6", "reversed": "!olleh"}}
    assert_and_print(expected, reversed_string, "Even number of characters")
    # check 2: short string with odd number of characters
    string = "world"
    reversed_string = reverse_count(string)
    expected = {"world": {"count": "5", "reversed": "dlrow"}}
    assert_and_print(expected, reversed_string, "Odd number of characters")
    # check 3: string with non-standard characters
    string = "h3ll0!"
    reversed_string = reverse_count(string)
    expected = {"h3ll0!": {"count": "6", "reversed": "!0ll3h"}}
    assert_and_print(expected, reversed_string, "Non-standard characters")
    # check 4: empty string
    string = ""
    reversed_string = reverse_count(string)
    expected = {"": {"count": "0", "reversed": ""}}
    assert_and_print(expected, reversed_string, "Empty string")
