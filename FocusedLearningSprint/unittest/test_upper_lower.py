import pytest
from upper_lower import upper_lower

def test_upper_lower():
    res1 = upper_lower("HelloWorld")
    assert  res1 is True, " Test Case 1 failed"

    res2 = upper_lower("ThisIsAStringWithUpperCaseLetters")
    assert res2 is True, "Test Case 2 Failed"

    res3 = upper_lower("")
    assert res3 is False, "Test Case 2 Failed"

    res4 = upper_lower("ibrahim")
    assert res4 is False, "Test Case 2 Failed"