# Parabank Automation Framework

## Overview
End-to-end test automation framework built with Playwright and Python
targeting the Parabank banking application.

## Tech Stack
- Language: Python
- Automation Tool: Playwright
- Test Framework: pytest
- Design Pattern: Page Object Model
- CI/CD: GitHub Actions
- Reporting: pytest-html

## Framework Structure
```
parabank-framework/
├── pages/
│   ├── login_page.py           → Login and logout actions
│   ├── register_page.py        → User registration actions
│   ├── accounts_page.py        → Account overview actions
│   ├── transfer_page.py        → Fund transfer actions
│   ├── billpay_page.py         → Bill payment actions
│   ├── findtransaction_page.py → Find transaction actions
│   ├── profile_page.py         → Update profile actions
│   └── loan_page.py            → Loan request actions
├── tests/
│   ├── test_login.py           → 6 login test cases
│   ├── test_register.py        → 3 register test cases
│   ├── test_accounts.py        → 2 account test cases
│   ├── test_transfer.py        → 3 transfer test cases
│   ├── test_billpay.py         → 1 bill payment test case
│   ├── test_findtransaction.py → 2 find transaction test cases
│   ├── test_profile.py         → 1 profile test case
│   └── test_loan.py            → 1 loan test case
├── utilities/
│   └── base_page.py            → Base class with reusable methods
├── testdata/
│   └── data.json               → Centralised test data
├── reports/                    → Generated HTML test reports
├── conftest.py                 → Browser setup and fixtures
└── pytest.ini                  → pytest configuration
```

## Test Coverage

| Module | Test Cases |
|---|---|
| Login | Valid login, invalid login, logout, empty username, empty password, both fields empty |
| Register | New user, existing username, mismatched passwords |
| Accounts | View accounts, account details |
| Transfer | Transfer funds, zero amount, page load |
| Bill Payment | Pay bill |
| Find Transaction | Search by amount, search by date |
| Profile | Update profile |
| Loan | Apply for loan |
| **Total** | **19 test cases** |

## How to Run
```
pip install playwright pytest pytest-playwright pytest-html
playwright install
pytest --headed --html=reports/report.html
```

## Run Specific Test File
```
pytest tests/test_login.py --headed
```

## Run Single Test Case
```
pytest tests/test_login.py::test_valid_login --headed
```
