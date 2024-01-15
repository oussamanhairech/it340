
def validate_password(password,length,digit_count,char_count,special_chars="!@#$%^&*()_+-={}[]|\:;'<>,.?/"):
    print("test initilizing ...")
    #test 1
    if len(password)>=length:
        print( True,"Test 1 : password  have at least",length," characters")
    else:
        print( False,"Test 1 : password must have  more than",length,"characters")
    # test 2
    digit=0
    for e in password:
        if e.isdigit():
            digit+=1
    if digit == digit_count:
        print(True, "Test 2 : password must have at least ",digit_count, "number")
    else:
        print(False,"Test 2 : password have at least " ,digit_count, "number")
    # test 3
    char=0
    for e in password:
        if e.isalpha():
            char+=1
    if char == char_count:
        print(True, "Test 3 : password must have at least",char_count, "character")
    else:
        print(False,"Test 3 : password have at least",char_count,"character")
    # Test 4 
    special_count=0;
    for e in password:
        if e in special_chars:
            special_count +=1
    if special_count !=0 :
        print(True, "Test 4 : password  have at least one of those special characters : ",special_chars)
    else:
        print(False,"Test 4 : password must have at least one of those special characters : ", special_chars)
password = input("Enter your password: ")
validate_password(password,3,1,1,"!")