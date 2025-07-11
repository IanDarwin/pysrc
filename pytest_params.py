from pytest import mark

# Parameterized tests run the same test logic with multiple different inputs.
# The parameter names on the function must concord with the @mark annotation.
# Despite mark's incorrect spelling of "parameterize", this does work:
@mark.parameterize("first,second,third", [
    (1,2,3),
    (4,5,6),
    (7,8,9),
])
def test_foo(first,second,third):
    print("values:", first, second, third)
    assert first > 0;

