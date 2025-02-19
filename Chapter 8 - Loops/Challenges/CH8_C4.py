def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    


#DO NOT TOUCH BELOW

run_cases = [
    (7, True),
    (-7, False),
    (9, False),
    (23, True),
]

submit_cases = run_cases + [
    (-1, False),
    (0, False),
    (1, False),
    (2, True),
    (4, False),
    (31, True),
    (100, False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input number: {input1}")
    print(f"Expecting: {expected_output}")
    result = is_prime(input1)
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
