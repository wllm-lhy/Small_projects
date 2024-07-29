while True:    
    print("==LOG IN==")
    print()
    mnm = input("user ID: ")
    pw = input("password: ")
    if mnm == "Wllm_lhy" or mnm == "wllm_lhy" and pw == "1835":
        print("\033[32m", "acces granted", "\033[0m")
        print()
        print("Hi", mnm,"! please answer this security question to confirm your identity: ")
        answerSecW = input("what is your favorite food?: ")
        print()
        if answerSecW == "Gluten":
            print("\033[32m", "right answer, identity confirmed.", "\033[0m")
        else :
            print("\033[31m", "wrong answer, one attempt remaining", "\033[0m")
            print()
            answerSecW2 = input("in what city were you born?: ")
            if answerSecW2 == "Montreal":
                print("\033[32m", "right answer, identity confirmed.", "\033[0m")
            else :
                print("\033[31m", "wrong answer, you are out of attempts. Your account is now blocked, please contact assistance.", "\033[0m")
    elif mnm == "User" and pw == "123456789":
        print("\033[32m", "acces granted", "\033[0m")
        print()
        print("Hi", mnm,"! please answer this security question to confirm your identity:")
        answerSecW = input("what is your favorite food?: ")
        print()
        if answerSecW == "keyboards":
            print("\033[32m", "right answer, identity confirmed.", "\033[0m")
        else :
            print("\033[31m", "wrong answer, one attempt remaining", "\033[0m")
            print()
        answerSecW2 = input("in what city were you born?: ")
        if answerSecW2 == "Microsoft":
            print("\033[32m", "right answer, identity confirmed.", "\033[0m")
        else :
            print("\033[31m", "wrong answer, you are out of attempts. Your account is now blocked, please contact assistance.", "\033[0m")
    else :
        print("\033[31m", "access denied", "\033[0m")
        print()
    cmd = input("Do you want to quit? enter \"y\" to quit or \"n\" for the menu >")
    if cmd == "y":
        break
print("goodbye!")