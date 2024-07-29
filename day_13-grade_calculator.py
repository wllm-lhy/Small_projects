print("==DAT TIRTHEEN==")
print()
print("Major project 1: grade calculator")
print()
Name = input("what was the name of your exam? :")
ms = float(input("what was the maxumum possible score? :"))
ys = int(input("and what was your grade? :"))
finalP = round((ys/100*ms),2)
gradeF = "input grade"
if finalP == 100 :
    gradeF = "\033[32m"+"A+"+"\033[0m"
elif finalP == [95-99]:
    gradeF = "\033[32m"+"A"+"\033[0m"
elif finalP == [90-94] :
    gradeF = "\033[32m"+"A-"+"\033[0m"
elif finalP == [85-89] :
    gradeF = "\033[33m"+"B+"+"\033[0m" 
elif finalP == [80-84] :
    gradeF = "\033[33m"+"B"+"\033[0m"    
elif finalP == [75-79] :
    gradeF = "\033[33m"+"B-"+"\033[0m"   
elif finalP == [70-74] :
    gradeF = "\033[35m"+"C+"+"\033[0m"    
elif finalP == [65-79] :
    gradeF = "\033[35m"+"C"+"\033[0m"   
elif finalP == [60-64] :
    gradeF = "\033[35m"+"c-"+"\033[0m"    
elif finalP < 60 :
    gradeF = "\033[31m"+"Fail"+"\033[0m"  
print()
print("\033[32m","here are your results >","\033[0m")
print()
print("exam name:", Name)
print("note(%):", finalP)
print("grade:", gradeF)

