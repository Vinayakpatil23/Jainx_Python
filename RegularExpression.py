import re

# s='Welcome to python programming'
# r1=re.split(' ',s)
# print(r1)
#
# li=['This','is','python','session']
# r2=' -*- '.join(li)
# print(r2)
#
# r3=re.match('el',s)
# if r3:
#     print('starts with el')
# else:
#     print("doesn't start with el")

# phonePattern= r'^[0-9]\d{9}'
# ph=input("enter a phone number")
# x=re.fullmatch(phonePattern,ph)
# print(x)
# if x:
#     print("valid phno")
# else:
#     print("not valid")

# def validate_phone_number(phone_number):
#     pattern = r'^[6-9]\d{9}$' 
#     if re.fullmatch(pattern, phone_number):
#         return "Valid phone number"
#     else:
#         return "Invalid phone number"
#
# # Example usage
# phone_number = input("Enter a phone number: ")
# print(validate_phone_number(phone_number))

def validate_gmail(email):
    pattern = r'^[a-zA-Z0-9_]+@gmail\.com$'
    if re.fullmatch(pattern, email):
        return "Valid Gmail address"
    else:
        return "Invalid Gmail address"


email = input("Enter a Gmail address: ")
print(validate_gmail(email))
