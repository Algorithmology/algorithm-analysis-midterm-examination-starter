"""Pytest configuration for the exam package."""

import sys

import pytest

traced_functions_map = {}


def pytest_configure(config):
    """Add markers to the pytest configuration."""
    # Question 1
    config.addinivalue_line("markers", "question_one_part_a: Question 1 Part (a)")
    config.addinivalue_line("markers", "question_one_part_b: Question 1 Part (b)")
    config.addinivalue_line("markers", "question_one_part_c: Question 1 Part (c)")
    # Question 2
    config.addinivalue_line("markers", "question_two_part_a: Question 2 Part (a)")
    config.addinivalue_line("markers", "question_two_part_b: Question 2 Part (b)")
    config.addinivalue_line("markers", "question_two_part_c: Question 2 Part (c)")
    # Question 3
    config.addinivalue_line("markers", "question_three_part_a: Question 3 Part (a)")
    config.addinivalue_line("markers", "question_three_part_b: Question 3 Part (b)")
    config.addinivalue_line("markers", "question_three_part_c: Question 3 Part (c)")
    # Question 4
    config.addinivalue_line("markers", "question_four_part_a: Question 4 Part (a)")
    config.addinivalue_line("markers", "question_four_part_b: Question 4 Part (b)")
    config.addinivalue_line("markers", "question_four_part_c: Question 4 Part (c)")


def pytest_report_teststatus(report):
    """Suppress all of the output from the test run."""
    category, short, verbose = "", "", ""
    if hasattr(report, "wasxfail"):
        if report.skipped:
            category = "xfailed"
            verbose = "xfail"
        elif report.passed:
            category = "xpassed"
            verbose = ("XPASS", {"yellow": True})
        return (category, short, verbose)
    elif report.when in ("setup", "teardown"):
        if report.failed:
            category = "error"
            verbose = "ERROR"
        elif report.skipped:
            category = "skipped"
            verbose = "SKIPPED"
        return (category, short, verbose)
    category = report.outcome
    verbose = category.upper()
    return (category, short, verbose)


@pytest.fixture(autouse=True)
def trace_function(request):
    """Trace the functions called during a test."""
    traced_functions = set()
    # determine the name of the current test case
    test_case = request.node.name

    def trace_calls(frame, event, _):
        """Trace the function calls."""
        if event != "call":
            return
        code = frame.f_code
        func_name = code.co_name
        filename = code.co_filename
        if "questions" in filename:
            traced_functions.add(func_name)  # ruff: noqa
        return

    sys.settrace(trace_calls)
    yield
    sys.settrace(None)
    if len(traced_functions) == 0:
        traced_functions = traced_functions.add("")
    traced_functions_map[test_case] = traced_functions


def pytest_json_modifyreport(json_report):
    """Add a key to the report."""
    # Add a key to the report
    json_report["test_function_trace"] = traced_functions_map
