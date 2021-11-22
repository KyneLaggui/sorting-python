import random
import colorama
colorama.init()

def Generate_First_Equations():
    First_Number= random.randint(0,99)
    Second_Number= random.randint(0,99)

    Ask_User_Questions= int(input(colorama.Fore.BLUE + f"1) Sum of {First_Number} and {Second_Number}: "))
    Correct_Answer= First_Number + Second_Number
    if  Correct_Answer == Ask_User_Questions:
        print(colorama.Fore.GREEN + "Correct, Proceed to next question")
        return 1

    elif Correct_Answer != Ask_User_Questions: 
        print(colorama.Fore.RED + "Wrong, Proceed to next question")
        return 0
    
def Generate_Second_Equations():
    First_Number= random.randint(0,99)
    Second_Number= random.randint(0,99)

    Ask_User_Questions= int(input(colorama.Fore.BLUE + f"2) Sum of {First_Number} and {Second_Number}: "))
    Correct_Answer= First_Number + Second_Number
    if  Correct_Answer == Ask_User_Questions:
        print(colorama.Fore.GREEN + "Correct, Proceed to next question")
        return 1

    elif Correct_Answer != Ask_User_Questions: 
        print(colorama.Fore.RED + "Wrong, Proceed to next question")
        return 0

def Generate_Third_Equations():
    First_Number= random.randint(0,99)
    Second_Number= random.randint(0,99)

    Ask_User_Questions= int(input(colorama.Fore.BLUE + f"3) Sum of {First_Number} and {Second_Number}: "))
    Correct_Answer= First_Number + Second_Number
    if  Correct_Answer == Ask_User_Questions:
        print(colorama.Fore.GREEN + "Correct, Proceed to next question")
        return 1

    elif Correct_Answer != Ask_User_Questions: 
        print(colorama.Fore.RED +"Wrong, Proceed to next question")
        return 0

def Generate_Fourth_Equations():
    First_Number= random.randint(0,99)
    Second_Number= random.randint(0,99)

    Ask_User_Questions= int(input(colorama.Fore.BLUE + f"4) Sum of {First_Number} and {Second_Number}: "))
    Correct_Answer= First_Number + Second_Number
    if  Correct_Answer == Ask_User_Questions:
        print(colorama.Fore.GREEN + "Correct, Proceed to next question")
        return 1

    elif Correct_Answer != Ask_User_Questions: 
        print(colorama.Fore.RED + "Wrong, Proceed to next question")
        return 0

def Generate_Fifth_Equations():
    First_Number= random.randint(0,99)
    Second_Number= random.randint(0,99)

    Ask_User_Questions= int(input(colorama.Fore.BLUE + f"5) Sum of {First_Number} and {Second_Number}: "))
    Correct_Answer= First_Number + Second_Number
    if  Correct_Answer == Ask_User_Questions:
        print(colorama.Fore.GREEN + "Correct, Proceed to next question")
        return 1

    elif Correct_Answer != Ask_User_Questions: 
        print(colorama.Fore.RED + "Wrong, Proceed to next question")
        return 0

def Generate_Sixth_Equations():
    First_Number= random.randint(0,99)
    Second_Number= random.randint(0,99)

    Ask_User_Questions= int(input(colorama.Fore.BLUE + f"6) Sum of {First_Number} and {Second_Number}: "))
    Correct_Answer= First_Number + Second_Number
    if  Correct_Answer == Ask_User_Questions:
        print(colorama.Fore.GREEN + "Correct, Proceed to next question")
        return 1

    elif Correct_Answer != Ask_User_Questions: 
        print(colorama.Fore.RED + "Wrong, Proceed to next question")
        return 0

def Generate_Seventh_Equations():
    First_Number= random.randint(0,99)
    Second_Number= random.randint(0,99)

    Ask_User_Questions= int(input(colorama.Fore.BLUE + f"7) Sum of {First_Number} and {Second_Number}: "))
    Correct_Answer= First_Number + Second_Number
    if  Correct_Answer == Ask_User_Questions:
        print(colorama.Fore.GREEN + "Correct, Proceed to next question")
        return 1

    elif Correct_Answer != Ask_User_Questions: 
        print(colorama.Fore.RED + "Wrong, Proceed to next question")
        return 0

def Generate_Eighth_Equations():
    First_Number= random.randint(0,99)
    Second_Number= random.randint(0,99)

    Ask_User_Questions= int(input(colorama.Fore.BLUE + f"8) Sum of {First_Number} and {Second_Number}: "))
    Correct_Answer= First_Number + Second_Number
    if  Correct_Answer == Ask_User_Questions:
        print(colorama.Fore.GREEN + "Correct, Proceed to next question")
        return 1

    elif Correct_Answer != Ask_User_Questions: 
        print(colorama.Fore.RED + "Wrong, Proceed to next question")
        return 0

def Generate_Ninth_Equations():
    First_Number= random.randint(0,99)
    Second_Number= random.randint(0,99)

    Ask_User_Questions= int(input(colorama.Fore.BLUE + f"9) Sum of {First_Number} and {Second_Number}: "))
    Correct_Answer= First_Number + Second_Number
    if  Correct_Answer == Ask_User_Questions:
        print(colorama.Fore.GREEN + "Correct, Proceed to next question")
        return 1

    elif Correct_Answer != Ask_User_Questions: 
        print(colorama.Fore.RED + "Wrong, Proceed to next question")
        return 0

def Generate_Tenth_Equations():
    First_Number= random.randint(0,99)
    Second_Number= random.randint(0,99)

    Ask_User_Questions= int(input(colorama.Fore.BLUE + f"10) Sum of {First_Number} and {Second_Number}: "))
    Correct_Answer= First_Number + Second_Number
    if  Correct_Answer == Ask_User_Questions:
        print(colorama.Fore.GREEN + "Correct")
        return 1

    elif Correct_Answer != Ask_User_Questions: 
        print(colorama.Fore.RED + "Wrong")
        return 0

def User_Final_Score(First, Second, Third, Fourth,Fifth,Sixth,Seventh,Eighth,Ninth,Tenth):
    Total_Score= First + Second+ Third+ Fourth + Fifth + Sixth + Seventh + Eighth + Ninth + Tenth
    print(colorama.Fore.YELLOW + f"Your Final Score is {Total_Score}")

     

First_Score= Generate_First_Equations()
Second_Score= Generate_Second_Equations()
Third_Score= Generate_Third_Equations()
Fourth_Score= Generate_Fourth_Equations()
Fifth_Score= Generate_Fifth_Equations()
Sixth_Score= Generate_Sixth_Equations()
Seventh_Score= Generate_Seventh_Equations()
Eighth_Score= Generate_Eighth_Equations()
Ninth_Score= Generate_Ninth_Equations()
Tenth_Score= Generate_Tenth_Equations()
User_Final_Score(First_Score, Second_Score,Third_Score,Fourth_Score,Fifth_Score,Sixth_Score, Seventh_Score, Eighth_Score, Ninth_Score, Tenth_Score)