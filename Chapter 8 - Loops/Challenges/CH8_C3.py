def calculate_experience_points(level):
    total_exp = 0
    for i in range(1, level):
        total_exp = total_exp + i*5
    return total_exp


#DO NOT TOUCH BELOW

run_cases = [
    (2, 5),
    (3, 15),
    (4, 30),
]

submit_cases = run_cases + [
    (1, 0),
    (5, 50),
    (7, 105),
    (10, 225),
    (15, 525),
    (20, 950),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = calculate_experience_points(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
