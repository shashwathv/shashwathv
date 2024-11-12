def main():
    while True:
        password = input("Enter your password: ")
        mistakes = []
        count = 0
        if len(password) > 0:
            if length(password):
                count += 1
            else:
                mistakes.append("Minimum length of the password.")
            if cases(password):
                count += 1
            else:
                mistakes.append("The password is not case-sensitive.")
            if num(password):
                count += 1
            else:
                mistakes.append("Include numbers in the password")
            if special(password):
                count += 1
            else:
                mistakes.append("Include special charecters in the password.")
            if count <= 1:
                print("Strength: Weak")
                print("Missing: ")
                for i in range(len(mistakes)):
                    print(mistakes[i])
            if 2 <= count <= 3:
                print("Strength: Moderate")
                print("Missing: ")
                for i in range(len(mistakes)):
                    print(mistakes[i])
            if count == 4:
                print("Strength: Strong")
                break
        else:
            continue


def length(str):
    if len(str) >= 8:
        return True
    else:
        return False
    

def cases(strs):
    upper = 0
    lower = 0
    for str in strs:
        if str.isupper():
            upper += 1
        if str.islower():
            lower += 1
    if upper != 0 and lower != 0:
        return True
    else:
        return False
    

def num(strs):
    count = 0
    for str in strs:
        if str.isdigit():
            count += 1
    if count > 0:
        return True
    else:
        return False
    

def special(strs):
    s_c = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "<", ">", "?", "/", "[", "]", "{", "}"]
    count = 0
    for str in strs:
        if str in s_c:
            count += 1
    if count > 0:
        return True
    else:
        return False
    

if __name__ == "__main__":
    main()