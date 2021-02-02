import pytest
import requests
import json

# @pytest.fixture
# def input_value():
#    input = "http://127.0.0.1:8001/api/v1/login/"
#    return input

def test_login(dict):
    _login=requests.post("http://127.0.0.1:8001/api/v1/login/",data=dict)
    print(_login)
    assert _login.json()["status_code"]==200

def test_verify():
    _verify=requests.post("http://127.0.0.1:8001/api/v1/verify/",data={"username" : "tester@admaren.com",
	"secure_code" : "EAE38BC902DBD6C4F1F17295FD7BD22BCCF64B8F"})
    assert _verify.status_code==200
