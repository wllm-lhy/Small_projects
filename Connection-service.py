print("==LOG IN==")
print()
mnm = input("user ID: ")
pw = input("password: ")
if mnm == "Wllm_lhy" or mnm == "wllm_lhy" and pw == "7951":
    print("\033[32m", "acces granted", "\033[0m")
    print()
    print("Hi Wllm! please answer this security question to confirm your identity:")
    answerSecW = input("what is your favorite food?: ")
    print()
    if answerSecW == "Gluten":
        print("\033[32m", "right answer, identity confirmed.", "\033[0m")
    else :
        print("\033[31m", "wrong answer, one attempt remaining", "\033[0m")
        print()
        answerSecW2 = input("in what city were you born?: ")
        if answerSecW2 == "St-Hyacinthe":
            print("\033[32m", "right answer, identity confirmed.", "\033[0m")
        else :
            print("\033[31m", "wrong answer, you are out of attempts. Your account is now blocked, please contact assistance.", "\033[0m")
elif mnm == "Nilon" and pw == "123456789":
    print("\033[32m", "acces granted", "\033[0m")
else :
    print("\033[31m", "access denied", "\033[0m")