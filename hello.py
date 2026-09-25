print("Hello, QA world!")
username = "standard_user"
print (username)
login_attempts = 3
is_locked = True
print (login_attempts)
print (is_locked)
username = ["standard_user", "locked_out_user", "problem_user"]
print(username) 
login_attempts = 3
if login_attempts >= 3:
    print ("account locked")
else:
    print ("login allowed")
usernames = ["standard_user", "locked_out_user", "problem_user"]
for name in usernames:
 print ("testing login for:", name)
def check_login (attempts):
   if attempts >= 3:
      print ("account locked")
   else:
      print ("login allowed")
check_login (3)
check_login (1)
numbers = [0, 1, 2, 9, 10, 11]
for number in numbers:
   if number >= 1 and number <=10:
      print (number, "-valid")
   else: 
      print (number, "invalid")   