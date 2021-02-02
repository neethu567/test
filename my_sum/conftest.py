import pytest
from my_sum.calculator_class import *
@pytest.fixture()
def calcultor():
    return Calculator()

# def url():
#     return "http://127.0.0.1:8001/api/v1/"
@pytest.fixture()
def dict():
    return {"username" : "tester@admaren.com",
	"password" : "asd123##"}