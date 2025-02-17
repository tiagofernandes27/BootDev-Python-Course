def check_mount_rental(time_used, time_purchased):
    if time_used >= time_purchased:
        return "overtime charged"
    return "no charges yet"


#DO NOT TOUCH BELOW

run_cases = [
    (3, 4, "no charges yet"),
    (5, 2, "overtime charged"),
]

submit_cases = run_cases + [
    (2, 2, "overtime charged"),
    (0, 1, "no charges yet"),
    (1, 1, "overtime charged"),
    (100, 2, "overtime charged"),
    (2500, 3, "overtime charged"),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = check_mount_rental(input1, input2)
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
