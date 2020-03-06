import pytest


class TestClass:

    data = [{"name": "zbc", "age": 18}, {"name": "zsm", "age": 18}]

    @pytest.mark.zbc
    @pytest.mark.zsm
    @pytest.mark.parametrize("value", data)
    def test_1(self, value):
        assert isinstance(value.get("name"), str)
        assert value.get("age") == 18

    @pytest.mark.zsm
    @pytest.mark.zbc
    @pytest.mark.skip(reason="test skip1111")
    def test_2(self):
        x = "hello"
        assert type(x) == str