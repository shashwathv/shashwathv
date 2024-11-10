def main():
    sentence = input("Enter the string: ")
    print("Choose from any of the following option to perform on the string:")
    print("1.Reversing the string\n2.Finding whether it is a pallindrome\n3.Finding the frequency of the charecters.")
    option = int(input())
    if option == 1:
        print(reverse(sentence))
    elif option == 2:
        print(pallindrome(sentence))
    elif option == 3:
        frequency(sentence)
    else:
        raise ValueError("Enter the correct option.")


def reverse(string):
    return string[::-1]


def pallindrome(string):
    if string == string[::-1]:
        return "Pallindrome"
    else:
        return "Not Pallindrome"
    

def frequency(strs):
    freq = {}
    for char in strs:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    for char, count in freq.items():
        print(f"{char} appears {count} times.")
        
if __name__ == "__main__":
    main()