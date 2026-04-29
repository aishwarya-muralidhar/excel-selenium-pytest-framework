import pytest
from utils.excel_reader import read_excel_file
from pages.login_page import LoginPage

data = read_excel_file("test_data/login_data.xlsx")
test_data = data.to_dict(orient= "records")

@pytest.mark.parametrize("data", test_data)

def test_login(driver, data):
    login = LoginPage(driver)
    login.enter_username(data["username"])
    login.enter_password(data["password"])
    login.click_login()

    if data["expected_result"] == "success":
        assert login.is_login_successful(), "Expected success but failed"
    else:
        assert not login.is_login_successful(), "Expected failure but succeeded"