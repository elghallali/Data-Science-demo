from mylib.arithmetic import add,subtract


def test_add():
    assert 2 == add(1, 1)

def test_subtract():
    assert 2 == subtract(3, 1)    

def test_subtract():
    assert -2 == subtract(1, 3)