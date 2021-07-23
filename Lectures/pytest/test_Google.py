import pytest

# @pytest.mark.usefixtures("setup")
# class TestWithoutParamters:
#
#     def test_Title1(self):
#         assert "Google" in self.driver.title
#
#     def test_Title2(self):
#         assert "Googlee" in self.driver.title


@pytest.mark.usefixtures("setupWithParams")
class TestWithParameters:

    def test_Title1(self):
        assert "Google" in self.driver.title

    def test_Title2(self):
        assert "Google" in self.driver.title

    def test_Title3(self):
        assert "Google" in self.driver.title

    def test_Title4(self):
        assert "Google" in self.driver.title

    def test_Title5(self):
        assert "Google" in self.driver.title

    def test_Title6(self):
        assert "Google" in self.driver.title

    def test_Title7(self):
        assert "Google" in self.driver.title

    def test_Title8(self):
        assert "Google" in self.driver.title

    def test_Title9(self):
        assert "Google" in self.driver.title

    def test_Title10(self):
        assert "Google" in self.driver.title






