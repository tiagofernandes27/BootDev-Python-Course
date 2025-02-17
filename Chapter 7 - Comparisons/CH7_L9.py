def does_attack_hit(attack_roll, armor_class):
    if (attack_roll != 1 and attack_roll >= armor_class) or (attack_roll == 20):
        return True
    return False
    


#DO NOT TOUCH BELOW
run_cases = [
    (17, 18, False),
    (20, 25, True),
]

submit_cases = run_cases + [
    (1, 0, False),
    (16, 13, True),
    (5, 5, True),
    (1, 1, False),
    (20, 20, True),
    (15, 10, True),
    (2, 3, False),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = does_attack_hit(input1, input2)
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