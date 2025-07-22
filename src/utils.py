# src/utils.py

import re

def is_valid_email(email: str) -> bool:
    """Check if the email is valid."""
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email) is not None
