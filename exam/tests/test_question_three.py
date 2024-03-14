"""Confirm the correctness of functions in question_three."""

import pytest

# ruff: noqa: PLR2004
from questions.question_three import (
    sum_function_call_counts,
    sum_stop_float,
    sum_stop_int,
)


def assert_and_print(expected, actual, message):
    """Print a diagnostic message and assert that the expected and actual values are equal."""
    print(f"{message}: Expected {expected}, got {actual}")
    assert expected == actual


def demarcate():
    """Demarcate test output."""
    print("test_question_three.py")


@pytest.mark.question_three_part_a
def test_sum_stop_int():
    """Confirm correctness of question part."""
    demarcate()
    # check 1: small summation
    stop = 10
    sum = sum_stop_int(stop)
    expected = 55
    assert_and_print(expected, sum, "Sum up to the stop value of 10")
    # check 2: larger summation
    stop = 100
    sum = sum_stop_int(stop)
    expected = 5050
    assert_and_print(expected, sum, "Sum up to the stop value of 100")
    # check 3: summation with stop value of 0
    stop = 0
    sum = sum_stop_int(stop)
    expected = 0
    assert_and_print(expected, sum, "Sum up to the stop value of 0")
    # check 4: summation with negative stop value
    stop = -10
    sum = sum_stop_int(stop)
    expected = 0
    assert_and_print(expected, sum, "Sum up to the stop value of -10")\


@pytest.mark.question_three_part_b
def test_sum_stop_float():
    """Confirm correctness of question part."""
    demarcate()
    # check 1: small summation
    stop = 10.0
    step = 1.0
    sum = sum_stop_float(stop, step)
    expected = 55.0
    assert_and_print(expected, sum, "Sum up to the stop value of 10.0 with step size of 1.0")
    # check 2: larger summation
    stop = 100.0
    step = 1.0
    sum = sum_stop_float(stop, step)
    expected = 5050.0
    assert_and_print(expected, sum, "Sum up to the stop value of 100.0 with step size of 1.0")
    # check 3: summation with stop value of 0
    stop = 0.0
    step = 1.0
    sum = sum_stop_float(stop, step)
    expected = 0.0
    assert_and_print(expected, sum, "Sum up to the stop value of 0.0 with step size of 1.0")
    # check 4: summation with negative stop value
    stop = -10.0
    step = 1.0
    sum = sum_stop_float(stop, step)
    expected = 0.0
    assert_and_print(expected, sum, "Sum up to the stop value of -10.0 with step size of 1.0")


@pytest.mark.question_three_part_c
def test_sum_function_calls():
    """Confirm correctness of question part."""
    demarcate()
    # check 1: small dictionary
    function_calls = {"func1": 5, "func2": 5}
    sum = sum_function_call_counts(function_calls)
    expected = 10
    assert_and_print(expected, sum, "Sum of function calls in a small dictionary")
    # check 2: larger dictionary
    function_calls = {"func1": 50, "func2": 50, "func3": 100}
    sum = sum_function_call_counts(function_calls)
    expected = 200
    assert_and_print(expected, sum, "Sum of function calls in a larger dictionary")
    # check 3: dictionary with a function not called
    function_calls = {"func1": 0, "func2": 50, "func3": 100}
    sum = sum_function_call_counts(function_calls)
    expected = 150
    assert_and_print(expected, sum, "Sum of function calls with a function not called")
    # check 4: empty dictionary
    function_calls = {}
    sum = sum_function_call_counts(function_calls)
    expected = 0
    assert_and_print(expected, sum, "Sum of function calls in an empty dictionary")
