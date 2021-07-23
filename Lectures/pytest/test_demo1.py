import pytest

class Test:

    def test_m1(self):
        a = 3
        b = 4
        assert a+1 == b,"test failed"
        assert a == b,"test failed as a is not equal to b"

    def test_m2(self):
        name = "Selenium"
        assert name.upper()=="SELENIUM"


    def test_m3(self):
        assert True


    def test_m4(self):
        assert False

    @pytest.mark.login
    def test_m5(self):
        assert "naveen" == "Naveen"



