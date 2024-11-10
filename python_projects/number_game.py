import random

def main():
    while True:
        while True:
            try:
                print("There are three modes\nEasy\nMedium\nHard")
                lvl = input("Choose your level: ").lower()
                if lvl == "easy":
                    lvl = random.randint(1, 10)
                    break
                elif lvl == "medium":
                    lvl = random.randint(1, 100)
                    break
                elif lvl == "hard":
                    lvl = random.randint(1, 1000)
                    break
            except ValueError:
                pass
        level = random.randrange(lvl)
        count = 0
        print("You get 5 attempts only.")
        while True:
            try:
                guess = int(input("What's the number: "))
                if count == 5:
                    print("Maximum amount of attempt(s) reached.")
                    break
            except ValueError:
                pass
            if guess < level:
                print("Too low")
                count += 1
                print(f"{5 - count} attempt(s) remaining.")
            elif guess > level:
                print("Too high")
                count += 1
                print(f"{5 - count} attempt(s) remaining.")
            elif guess == level:
                print("Correct")
                print(f"You finished in {count} attempt(s)")
                break
        option = input("Do you want to re-try? ").lower()
        if option in ('y', 'yes'):
            continue
        else:
            break


if __name__ == "__main__":
    main()