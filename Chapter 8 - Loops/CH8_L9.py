def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total


#DO NOT TOUCH BELOW

run_cases = [
    (4, 4),
    (6, 9),
]

submit_cases = run_cases + [
    (0, 0),
    (1, 0),
    (2, 1),
    (4, 4),
    (10, 25),
    (15, 49),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * end: {input1}")
    print(f"Expecting: {expected_output}")
    result = sum_of_odd_numbers(input1)
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
