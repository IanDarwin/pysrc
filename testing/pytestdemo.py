# pytest works on assertions; see https://docs.pytest.org/en/8.0.x/
# PyCharm doesn't detect this, so run from command line

def inc( x):
    return x + 1

def test_answer_good():
    assert inc(3) == 4

# This test is expected to fail, just to show what failure looks like
def test_answer_bad():
    assert inc(3) == 5
