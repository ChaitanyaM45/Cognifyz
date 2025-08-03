password = input("Enter Password: ")
symbols = ['@', '#', '$', '%', '&', '!', '*', '_']

if len(password) >= 8 and any(sym in password for sym in symbols):
    print("Strong password")
else:
    print("Weak password")
