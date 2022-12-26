def add_nums(a, b):
    return a + b

def sub_nums(a, b):
    return a - b

def test_add_nums():
    assert add_nums(1, 2) == 3
    assert add_nums(1, 3) == 4
    assert add_nums(1, 4) == 6

def test_sub_nums():
    assert sub_nums(1, 2) == -1
    assert sub_nums(1, 3) == -2
    assert sub_nums(1, 4) != 6