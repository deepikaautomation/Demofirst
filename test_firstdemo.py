import pytest

@pytest.mark.skip

def test_firstpgm():
    print("hello")


def test_abcpgm(setup):
    print("hellosecond")


@pytest.mark.smoke
def test_thirdpgm():
    print("hellothird")
