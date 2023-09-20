import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will invoke first the fixture keyword in python helps to run first this to normally used to "
          "invoke browser")
    yield
    print("I am done with all test case execution")