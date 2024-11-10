def main():
    m_num = int(input("Enter the number you want the table of: "))
    print("Do you want it till 10 or 20?")
    option = int(input())
    create_table(m_num, option)

    
def create_table(num, max):
    for i in range(max):
        print(f"{num} x {i+1} = {num*(i+1)}")


if __name__ == "__main__":
    main()