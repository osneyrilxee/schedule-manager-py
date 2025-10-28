#!/usr/bin/env python3

def main():
    try:
        user = int(input("How old are you? "))

        if user < 18:
            print("Hello world 👋")
        else:
            print("Sorry, you must be under 18 to use this program.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
