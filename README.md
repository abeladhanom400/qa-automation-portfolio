# SauceDemo Automated Regression Suite

Automated tests covering core SauceDemo user flows, built with Python, pytest, and Selenium.

## What each test protects against

- **test_successful_login** — Confirms a user with valid credentials can actually get into the site. If this breaks, legitimate customers are locked out of the app entirely.
- **test_locked_out_login** — Confirms the account-lockout block actually works, so a banned account is refused access and shown an error instead of slipping through.
- **test_checkout_flow** — Confirms a customer can add an item to their cart and complete checkout. If this breaks, customers cannot buy anything.
- **test_reset_app_state** — Confirms the "Reset App State" menu option actually empties the cart, so customers can start over when they want to.
- **test_sort_price_low_to_high** — Confirms the price sort dropdown doesn't just *look* like it works — it checks the actual displayed order is correct, catching a bug that would be easy to miss just by glancing at the page.

## Running the suite

python -m pytest test_saucedemo_login.py

## Notes

Chrome's built-in password-breach warning popup is disabled for these tests via Chrome options — without it, the popup can intercept clicks and keystrokes mid-test and cause misleading failures.