import pytest


@pytest.fixture(name="testfixture")
def db():
    print("\nConnection Success!")

    yield

    print("Connection Closed!")


@pytest.fixture("class", autouse=True)
def class_scope():
    print("\nsetUpClass")
    yield
    print("tearDownClass")
