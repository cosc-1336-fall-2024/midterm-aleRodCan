#add import
from question_b import use_global, global_variable

def test_global_modification():
    assert global_variable == 10, "Initial value should be 10"

    use_global()

    assert global_variable == 15, "After modification, value should be 15"

    print(f"Global variable after modification: {global_variable}")

if __name__ == "__main__":
    test_global_modification()
