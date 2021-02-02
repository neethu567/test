import pytest
from my_sum.calculator_class import Calculator
from my_sum.calculator import *

NUMBER1=2
NUMBER2=4


def test_init(calcultor):
    assert calcultor._number==0

def test_sum(calcultor):
    assert (calcultor.calculate(add,NUMBER1,NUMBER2),6)

def test_mul():
    s1=Calculator()
    assert (s1.calculate(mul,NUMBER1,NUMBER2),8)

def test_div_zero(calcultor):

    with pytest.raises(ZeroDivisionError) as e:
        calcultor.calculate(div,NUMBER1,0)
    assert "division by zero" in str(e.value)

@pytest.mark.parametrize("a,b,c",[(1,2,3),(2,3,5),(2,3,1)])
def test_adds(calcultor,a,b,c):
    assert (calcultor.calculate(mul,a,b),c)


