def is_unique(s: str) -> bool:
    """
    Returns True if the string has all unique characters, False otherwise.
    Assumes ASCII input.
    """
    if len(s) > 128:  # There are only 128 unique ASCII characters
        return False

    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)

    return True


# Optional: version without additional data structures
def is_unique_no_ds(s: str) -> bool:
    """
    Version that does not use additional data structures.
    Time: O(n^2)
    """
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True
