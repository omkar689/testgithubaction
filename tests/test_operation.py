from src.math_operation import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-3,3)==0


def test_sub():
    assert sub(2,3)==1
    assert sub(10,3)==7
    assert sub(3,3)==1
    assert sub(2,3)==-1
