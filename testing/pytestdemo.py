# pytest works on assertions; see https://docs.pytest.org/en/8.0.x/
# PyCharm doesn't detect this, so run from command line

class PyTestDemo:
    def inc(self, x):
        return x + 1

    def test_answer_bad(self):
        assert self.inc(3) == 5

    def test_answer_good(self):
        assert self.inc(3) == 4
