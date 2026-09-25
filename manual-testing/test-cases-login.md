# SauceDemo Login — Manual Test Cases

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|--------------|-------|------------------|
| TC-01 | Successful login with valid credentials | User is on the SauceDemo login page | 1. Enter username `standard_user`<br>2. Enter password `secret_sauce`<br>3. Click Login | User is redirected to the inventory page |
|----|-------|--------------|-------|------------------|
| TC-02 | login attempt with locked-out user account | User is on the SauceDemo login page | 1. Enter username `locked_out_user`<br>2. Enter password `secret_sauce`<br>3. Click Login | error message "Sorry, this user has been locked out" |
|----|-------|--------------|-------|------------------|
| TC-03 | login attempt with wrong password | User is on the SauceDemo login page | 1. Enter username `standard_user`<br>2. Enter password `secret_saucerr`<br>3. Click Login | error message "Epic sadface: Username and password do not match any user in this service" |
|----|-------|--------------|-------|------------------|
| TC-04 | login attempt without filling in username | User is on the SauceDemo login page | 1. Enter password `secret_sauce`<br>3. Click Login | error message "Epic sadface: Username is required" |
|----|-------|--------------|-------|------------------|
| TC-05 | login attempt without filling in username or password| User is on the SauceDemo login page | 1. Click Login | error message "Epic sadface: Username is required" |
|----|-------|--------------|-------|------------------|
| TC-06 | login attempt with incorrect username case | User is on the SauceDemo login page | 1. Enter username `Standard_User`<br>2. Enter password `secret_sauce`<br>3. Click Login | error message "Epic sadface: Username and password do not match any user in this service" |
|----|-------|--------------|-------|------------------|
| TC-07 | login attempt with leading whitespace in username | User is on the SauceDemo login page | 1. Enter username ` standard_user` (with a leading space)<br>2. Enter password `secret_sauce`<br>3. Click Login | error message "Epic sadface: Username and password do not match any user in this service" |
|----|-------|--------------|-------|------------------|
| TC-08 | login attempt with an extremely long username | User is on the SauceDemo login page | 1. Enter a 100+ character random string as username<br>2. Enter password `secret_sauce`<br>3. Click Login | error message "Epic sadface: Username and password do not match any user in this service" — no crash or unexpected behavior |