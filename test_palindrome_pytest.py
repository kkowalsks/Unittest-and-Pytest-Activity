import palindrome

def test_true():
    assert palindrome.backwards("kayak") == True

def test_false():
    assert palindrome.backwards("CS 362") == False

def test_failed():
    assert palindrome.backwards("racecar") == False


#python -m pytest []