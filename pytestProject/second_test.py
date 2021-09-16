from pytest import mark


@mark.parametrize("x,y,z", [(1, 2, 3), (2, 2, 4), (4, 5, 9)])
def test_addition(x, y, z):
    assert x + y == z

def test_addition2(passParam):
    assert passParam[0] + passParam[1] == passParam[2]