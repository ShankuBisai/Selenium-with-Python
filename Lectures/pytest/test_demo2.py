import pytest


class Test:

    def test_m6(self):
        a = 3
        b = 4
        assert a+1 == b,"test failed"
        assert a == b,"test failed as a is not equal to b"

    def test_m7(self):
        name = "Selenium"
        assert name.upper()=="SELENIUM"


    def test_m8(self):
        assert True


    def test_m9(self):
        assert False

    @pytest.mark.login
    def test_m10(self):
        assert "naveen" == "naveen"



