"""
A test module that tests your example module.

Some people prefer to write tests in a test file for each function or
method/ class. Others prefer to write tests for each module. That decision
is up to you. This test example provides a single test for the example.py
module.
"""

from pyospackage_hli76_test.example import add_numbers


def test_add_numbers():
    """
    Test that add_numbers works as expected.

    A single line docstring for tests is generally sufficient.
    """
    out = add_numbers(1, 2)
    out2 = add_numbers(101, 202)
    expected_out = 3
    expected_out2 = 303
    assert out == expected_out, f"Expected {expected_out} but got {out}"
    assert out2 == expected_out2, f"Expected {expected_out2} but got {out2}"
