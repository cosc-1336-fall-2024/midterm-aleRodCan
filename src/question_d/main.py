#add import
from question_d import get_miles_per_hour

def main():
    
    kilometers = int(input("Enter kilometers: "))
    minutes = int(input("Enter minutes: "))

    result = get_miles_per_hour(kilometers, minutes)

    print(f"Result: {result}")

if __name__ == "__name__":
    main()