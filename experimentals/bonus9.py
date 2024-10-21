# password = input("Enter your password: ")
#
# result = []
#
# if len(password) >= 8:
#     result.append(True)
# else :
#     result.append(False)
#
# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True
# result.append(digit)
#
# uppercase = False
# for i in password:
#     if i.isupper():
#         uppercase = True
# result.append(uppercase)
#
#
# if all(result):
#     print("Password is Strong")
# else:
#     print("Password is Weak")

password = input("Enter your password: ")

result = {}

if len(password) >= 8:
    result['length'] = True
else :
    result['length'] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result['digit'] = True

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result['uppercase'] = True


if all(result.values()):
    print("Password is Strong")
else:
    print("Password is Weak")