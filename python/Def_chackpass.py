def chack_pasword(password):
    if len(password)<8:
        return "password is to short"
    else:
        return "password is secure "

test_1= chack_pasword("sup boy")
test_2=chack_pasword("eldern ring 12345")
print(f"This is test_1: {test_1}| This is test_2: {test_2}")