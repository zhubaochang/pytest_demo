import pytest


@pytest.mark.usefixtures("testfixture")
def test_fixture():
    assert 1