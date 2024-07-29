print("==DAT TIRTHEEN==")
print()
print("Major project 1: grade calculator")
print()
print("\033[31m","NOTICE: the grades are based on Quebec's grading system, each grade is -5%. Ex: A+ = 100, A = 95 etc.","\033[0m")
Name = input("what was the name of your exam? :")
ms = float(input("what was the maximum possible score? :"))
ys = int(input("and what was your grade? :"))
finalP =  round((ys*100/ms),2)
gradeF = "input grade"
if finalP == 100 :
    gradeF = "\033[32m"+"A+"+"\033[0m"
elif finalP >= 95 and finalP < 100:
    gradeF = "\033[32m"+"A"+"\033[0m"
elif finalP >= 90 and finalP < 95:
    gradeF = "\033[32m"+"A-"+"\033[0m"
elif finalP >= 85 and finalP < 90:
    gradeF = "\033[33m"+"B+"+"\033[0m" 
elif finalP >= 80 and finalP < 85:
    gradeF = "\033[33m"+"B"+"\033[0m"    
elif finalP >= 75 and finalP < 80:
    gradeF = "\033[33m"+"B-"+"\033[0m"   
elif finalP >= 70 and finalP < 75:
    gradeF = "\033[35m"+"C+"+"\033[0m"    
elif finalP >= 65 and finalP < 70:
    gradeF = "\033[35m"+"C"+"\033[0m"   
elif finalP >= 60 and finalP < 65:
    gradeF = "\033[35m"+"c-"+"\033[0m"    
elif finalP < 60 :
    gradeF = "\033[31m"+"Fail"+"\033[0m"  
print()
print("\033[32m","here are your results >","\033[0m")
print()
print("exam name:", Name)
print("note(%):", finalP)
print("grade:", gradeF)
if finalP == 100 :
    print("Thats amazing, congrats!")
elif finalP >= 95 and finalP < 100:
    print("great! keep it like that!")
elif finalP >= 90 and finalP < 95:
    print("Nice!")
elif finalP >= 85 and finalP < 90:
    print("Really good!")
elif finalP >= 80 and finalP < 85:
    print("pretty good, you can seek higher for your next excam, i know you can!")   
elif finalP >= 75 and finalP < 80:
    print("you can do even better next time ;)")
elif finalP >= 70 and finalP < 75:
    print("yes you can!!!!")
elif finalP >= 65 and finalP < 70:
    print("oh careful! you're near the line there.")
elif finalP >= 60 and finalP < 65:
    print("oh that was near! i know you can do better,  just push a little more!")  
elif finalP < 60 :
    print("oh no... maybe that was a bad exam, i'm sure the next one are going to be better if you give a little more of yourself.")  