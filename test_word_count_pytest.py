import word_count

def test_four():
    assert word_count.wordCount("Four word long sentence") == 4

def test_zero():
    assert word_count.wordCount("") == 0

def test_failed():
    assert word_count.wordCount("This sentence will fail") == 7
