import pytest

def M1():
    a="ABC"
    b="ABC"
    assert a==b,"Test case failed if not Matching"

def test_M4():
    a=10
    b=30
    assert a==b,"Test case failed if not Matching"


def test_M5():
    a="ABC"
    b="ABC"
    assert a==b,"Test case failed if not Matching"

def test_Login_FB():
    username="Admin"
    assert username == "Admin","Test case Failed if not matching"