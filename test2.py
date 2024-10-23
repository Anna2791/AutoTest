import pytest
from main import count_vowels

def test_only_vowels():
    assert count_vowels("аеиуо") == 5
    assert count_vowels("АУЕОИ") == 5

def test_no_vowels():
    assert count_vowels("рнглд") == 0
    assert count_vowels("") == 0

def test_mixed_string():
    assert count_vowels("программистка") == 4
    assert count_vowels("гарри поттер") == 4

if __name__ == "__main__":
    pytest.main()