from calculator import Calculator
import editdistance
import pytest

calculator = Calculator()


#@pytest.mark.my_suite
def test1():
    assert calculator.add(4, 7) == 11


def test2():
    assert calculator.subtract(10, 5) == 5


def test3():
    assert calculator.multiply(3, 7) == 21


def test4():
    assert calculator.divide(10, 2) == 5


def test5():
    assert editdistance.eval('111', '112') == 1


def exception_raiser():
    return 1 / 0


def test_exception():
    with pytest.raises(ZeroDivisionError):
        exception_raiser()


def test_with_mock(mocker):
    mocker.patch(
        'calculator.Calculator.add',
        return_value=5
    )
    assert calculator.add(4, 7) != 11


@pytest.fixture
def my_fixture():
    return 42


def test_with_fixture(my_fixture):
    assert my_fixture == 42