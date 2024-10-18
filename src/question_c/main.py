#add import
from question_c import use_local_variable

def test_local_variable():
    num = 100
    print(f"Before function call, num is {num}")

    use_local_variable(num)

    print(f"After function call, num is still {num} (unchanged)")

if __name__ == "__name__":
    test_local_variable()