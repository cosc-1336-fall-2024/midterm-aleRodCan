#add import
from question_a import get_day_of_week

def main():
    while True:
        try:
            user_input = int(input("Enter a number (1-7) fro the day of the week,  or 0 to quit:"))

            if user_input == 0:
                print("Exiting Program.")
                break
            print(get_day_of_week(user_input))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()


         