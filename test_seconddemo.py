# to cheecck un the terminal use the command   python -m pytest -v [in detail ]or python -m pytest
#  C:\Users\DeepikaDR\PycharmProjects\pythonProject4>python -m pytest -v
# python -m pytest -v -s this also will work
# To run only test cases with some regular expressions or specific name  python -m pytest -k abc -v -s
# to run only specidifc testcases python -m pytest test_seconddemo.py abc -v -s
# to run only some modukes that is smoke test cases python -m pytest -m smoke -v -s
# before that use the tag @pytset and mark as smoke or whatevr
# a teest case need to be run as part of some prerequiste and do not want to show in any test report then use the tag
# @pytest.mark.xfail


import pytest


# python -m  test_seconddemo.py -v -s   only run single test case


def test_abcgreet(setup):
    msgg = "Hello"
    assert msgg == "Hi", "test failed"


@pytest.mark.smoke
@pytest.mark.xfail
def test_sum():
    a = 9
    b = 8
    assert a + 9 == b, "sum is not same as b"
