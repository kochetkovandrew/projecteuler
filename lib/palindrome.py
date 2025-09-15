def check_pal(cand):
    """Check if a number is a palindrome."""
    return cand == int(str(cand)[::-1])
