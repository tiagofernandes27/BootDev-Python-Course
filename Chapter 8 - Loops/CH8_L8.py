def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total


#DO NOT TOUCH BELOW

run_cases = [(0, 5, 10), (0, 10, 45), (10, 20, 145)]

submit_cases = run_cases + [
    (1, 100, 4950),
    (5, 50, 1215),
    (20, 30, 245),
    (50, 60, 545),
    (100, 110, 1045),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * start: {input1}")
    print(f" * end: {input2}")
    print(f"Expecting: {expected_output}")
    result = sum_of_numbers(input1, input2)
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
