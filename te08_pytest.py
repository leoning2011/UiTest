import pytest


def fun(x):
    return x + 1

def test_answer_1():
    """测试断言一"""
    assert fun(3) == 4
def test_answer_2():
    """测试断言二"""
    assert fun(5) == 7

@pytest.mark.parametrize("test_input,expected",[
    ("3+5",8),
    ("2+4",6),
    pytest.param("6 * 9",42,marks=pytest.mark.xfail),
    pytest.param("6 * 6",42,marks=pytest.mark.skip)
])

def test_mark(test_input,expected):
    """用例集合"""
    assert eval(test_input) == expected

if __name__ == '__main__':
    pytest.main(['-v','--html=report.html','te08_pytest.py'])