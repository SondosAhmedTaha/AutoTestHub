# tests/test_utils.py

from src.utils import is_valid_email

def test_valid_email():
    assert is_valid_email("sara@example.com")

def test_invalid_email_no_at():
    assert not is_valid_email("saraexample.com")

def test_invalid_email_no_domain():
    assert not is_valid_email("sara@com")

def test_empty_email():
    assert not is_valid_email("")
