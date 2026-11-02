from src.cli import get_menu

def main():
    menu = get_menu()

    while True:
        print(menu)

        user_inp = input(">>")


# problem
if __name__== "__main__":
    main()