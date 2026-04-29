# Selenium Pytest Data-Driven Framework

## Tech Stack
- Python
- Selenium WebDriver
- Pytest
- Pandas (Excel handling)

## Features
- Data-driven testing using Excel
- Page Object Model (POM)
- Reusable utility functions
- Pytest fixtures

## How to Run
pip install -r requirements.txt
pytest -v


## Reports & Screenshots

To generate an HTML report:
pytest -v --html=reports/report.html --self-contained-html

Screenshots are captured automatically on test failure and stored in:
reports/screenshots/
