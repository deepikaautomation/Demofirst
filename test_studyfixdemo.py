import pytest


@pytest.mark.usefixtures("setup")
class Testexanple:

    def test_addition(self):
        a = 10
        b = 11
        print(sum)
        assert a + b == 21, "I am wrong"

    def test_def1(self):
        print(" i am def 1")

    def test_def2(self):
        print(" i am def 2")

    def test_def3(self):
        print(" i am def 3")
