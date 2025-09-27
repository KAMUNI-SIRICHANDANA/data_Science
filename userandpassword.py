user_pass = {"siri06@gmail.com":["siri",21,"siri06"],"megha01@gmail.com":["megha",23,"megha01"],"jay10@gmail.com":["jay",25,"jay01"]}
user=input("Enter user name ")
if user_pass.get(user) == None:
    print("Sign up for new account")
else:
    print(f"{user}, Exists")