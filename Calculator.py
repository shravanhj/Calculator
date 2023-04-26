#Calculator Code by Shravan H J

#ADDition
def for_plus(first_val, second_val):
    return first_val + second_val
#MINUS
def for_substraction(first_val,second_val):
    return first_val - second_val
#MULTIPLICATION
def for_multiplication(first_val,second_val):
    return first_val * second_val
#DIVISION
def for_Division(first_val,second_val):
    return first_val / second_val
#PERCENTAGE
def for_percentage(first_val, second_val):
    return (first_val/second_val)*100
def thank_you():
    print("\tThanks for using Calculator")
    print("\t\tCode by Shravan H J")


def main_fun():
    print("\t\t\t CALCULATOR")
    print()
    print("1: Addition\t\t\t\t2: Substraction")
    print("3: Multiplication\t\t4:Division")
    print("5: Percentage\t\t\t6:Exit")
    print()
    choice = int(input('Select your choice from above options: '))
    print()

    if choice==6:
        thank_you()
    elif choice==1:
        Num1 = int(input('Enter First value: '))
        Num2 = int(input('Enter Second value: '))
        print(Num1,"+",Num2,"=", for_plus(Num1, Num2))
        main_fun()

    elif choice == 2:
        Num1 = int(input('Enter First value: '))
        Num2 = int(input('Enter Second value: '))
        print(Num1, "-", Num2, "=", for_substraction(Num1, Num2))
        main_fun()

    elif choice == 3:
        Num1 = int(input('Enter First value: '))
        Num2 = int(input('Enter Second value: '))
        print(Num1, "*", Num2, "=", for_multiplication(Num1, Num2))
        main_fun()

    elif choice == 4:
        Num1 = int(input('Enter First value: '))
        Num2 = int(input('Enter Second value: '))
        print(Num1, "/", Num2, "=", for_Division(Num1, Num2))
        main_fun()

    elif choice == 5:
        Num1 = int(input('Enter First value: '))
        Num2 = int(input('Enter Total value: '))
        print(Num1, "-", Num2, "=",for_percentage(Num1, Num2),"%")
        main_fun()

    else:
        print("Please Enter Correct input.!!!!")
        main_fun()

main_fun()
