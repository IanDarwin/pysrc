# pytest works on assertions; see https://docs.pytest.org/en/8.0.x/

def inc(x):
    return x + 1

def test_answer_bad():
    assert inc(3) == 5

def test_answer_good():
    assert inc(3) == 4
