import os
import pytest
import pytest_html
from selenium import webdriver
from datetime import datetime

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only act after test execution
    if report.when == "call":
        driver = item.funcargs.get("driver", None)

        if driver:
            screenshots_dir = os.path.abspath("reports/screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            # Take screenshot
            driver.save_screenshot(file_path)

            # Attach screenshot ONLY if test failed
            if report.failed:
                extra = getattr(report, "extra", [])

                extra.append(pytest_html.extras.image(file_path))

                report.extra = extra

