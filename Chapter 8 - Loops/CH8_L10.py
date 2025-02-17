def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance>3:
        current_health += 1
        enemy_distance -= 2
    return current_health



#DO NOT TOUCH BELOW

run_cases = [(0, 10, 20, 9), (0, 10, 4, 1), (8, 10, 20, 10)]

submit_cases = run_cases + [
    (0, 0, 0, 0),
    (9, 10, 3, 9),
    (100, 100, 200, 100),
    (2, 110, 50, 26),
    (100, 1010, 2000, 1010),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print("Inputs:")
    print(f" * current_health: {input1}")
    print(f" *     max_health: {input2}")
    print(f" * enemy_distance: {input3}")
    print(f"Expected Health: {expected_output}")
    result = regenerate(input1, input2, input3)
    print(f"  Actual Health: {result}")
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
