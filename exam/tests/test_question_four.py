"""Confirm the correctness of functions in question_four."""

# Note: Do not modify any part of this file!

import pytest

# ruff: noqa: PLR2004
from questions.question_four import (
    Gene,
    detect_duplicates_gene,
    detect_duplicates_int,
    detect_duplicates_str,
)


def assert_and_print(expected, actual, message):
    """Print a diagnostic message and assert that the expected and actual values are equal."""
    print(f"{message}: Expected {expected}, got {actual}")
    assert expected == actual


def demarcate():
    """Demarcate test output."""
    print("test_question_four.py")


@pytest.mark.question_four_part_a
def test_duplicates_int():
    """Confirm correctness of question part."""
    demarcate()
    # check 1: small list with duplicates
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    detected = detect_duplicates_int(data)
    expected = True
    assert_and_print(expected, detected, "Small list with int duplicates")
    # check 2: larger list with duplicates
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10]
    detected = detect_duplicates_int(data)
    expected = True
    assert_and_print(expected, detected, "Larger list with int duplicates")
    # check 3: list without duplicates
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    detected = detect_duplicates_int(data)
    expected = False
    assert_and_print(expected, detected, "List without int duplicates")
    # check 4: empty list
    data = []
    detected = detect_duplicates_int(data)
    expected = False
    assert_and_print(expected, detected, "Empty list with not int values")


@pytest.mark.question_four_part_b
def test_duplicates_str():
    """Confirm correctness of question part."""
    # check 1: small list with duplicates
    data = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "1"]
    detected = detect_duplicates_str(data)
    expected = True
    assert_and_print(expected, detected, "Small list with str duplicates")
    # check 2: larger list with duplicates
    data = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "10"]
    detected = detect_duplicates_str(data)
    expected = True
    assert_and_print(expected, detected, "Larger list with str duplicates")
    # check 3: list without duplicates
    data = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    detected = detect_duplicates_str(data)
    expected = False
    assert_and_print(expected, detected, "List without str duplicates")
    # check 4: empty list
    data = []
    detected = detect_duplicates_str(data)
    expected = False
    assert_and_print(expected, detected, "Empty list with not str values")


@pytest.mark.question_four_part_c
def test_duplicates_gene():
    """Confirm correctness of question part."""
    # check 1: small list with two genes that are duplicates
    data = [
        Gene("AADACL3", 5, "Arylacetamide deacetylase-like 3"),
        Gene("AADACL4", 5, "Arylacetamide deacetylase-like 4"),
    ]
    detected = detect_duplicates_gene(data)
    expected = True
    assert_and_print(expected, detected, "Small list with gene duplicates")
    # check 2: small list with two genes that are not duplicates
    data = [
        Gene("FPGT02", 4, "Fucose-1-phosphate guanylyltransferase"),
        Gene("AADACL4", 5, "Arylacetamide deacetylase-like 4"),
    ]
    detected = detect_duplicates_gene(data)
    expected = False
    assert_and_print(expected, detected, "Small list without gene duplicates")
    # check 3: larger list with duplicates
    data = [
        Gene("AADACL3", 5, "Arylacetamide deacetylase-like 3"),
        Gene("FPGT02", 4, "Fucose-1-phosphate guanylyltransferase"),
        Gene("AADACL4", 5, "Arylacetamide deacetylase-like 4"),
        Gene("AADACL3", 5, "Arylacetamide deacetylase-like 3"),
        Gene("AADACL4", 5, "Arylacetamide deacetylase-like 4"),
    ]
    detected = detect_duplicates_gene(data)
    expected = True
    assert_and_print(expected, detected, "Larger list with gene duplicates")
    # check 4: empty list
    data = []
    detected = detect_duplicates_gene(data)
    expected = False
    assert_and_print(expected, detected, "Empty list")
