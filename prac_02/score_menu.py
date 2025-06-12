MENU = "(G)et a valid score\n (P)rint result\n (S)how stars\n (Q)uit"
print(MENU)


def main():
    """main function"""
    valid_score = ""
    choice = input("Choose:").upper()
    while choice != "Q":
        if choice == "G":
            valid_score = validate_score()
        elif choice == "P":
            if valid_score == "":
                print("No score to determine")
            else:
                result = print_result(valid_score)
                print(result)
        elif choice == "S":
            if valid_score == "":
                print("No score to determine")
            else:
                print("*"*int(valid_score))
        else:
            print(MENU)
            print("Error choice")
        choice = input("Choose：").upper()
    print("Bye")


def validate_score():
    """validate user input"""
    score = float(input("Enter your score:"))
    while score < 0 or score > 100:
        score = float(input("Enter your score:"))
    return score

def print_result(score):
    """determine user inputted score and print result"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()