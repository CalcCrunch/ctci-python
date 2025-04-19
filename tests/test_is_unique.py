from arrays_strings.is_unique import is_unique, is_unique_no_ds

def test_is_unique():
    assert is_unique("abcde") == True
    assert is_unique("aabbcc") == False
    assert is_unique("") == True
    assert is_unique("a") == True
    assert is_unique("abcdefghijklmnopqrstuvwxyz") == True
    assert is_unique("aA") == True  # case-sensitive

def test_is_unique_no_ds():
    assert is_unique_no_ds("abcde") == True
    assert is_unique_no_ds("aabbcc") == False
    assert is_unique_no_ds("") == True
    assert is_unique_no_ds("aa") == False
