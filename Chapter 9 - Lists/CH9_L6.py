def get_last_index(inventory):
    return len(inventory)-1


#DO NOT TOUCH BELOW

run_cases = [
    (["Potion"], 0),
    (["Potion", "Iron Breastplate"], 1),
    (["Potion", "Iron Breastplate", "Bread", "Longsword"], 3),
]

submit_cases = run_cases + [
    ([], -1),
    (["Single item"], 0),
    (["Shield", "Sword", "Bow", "Arrows", "Health Potion"], 4),
    (["Shield", "Sword", "Bow"], 2),
    (["Shield", "Sword"], 1),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_last_index(input1)
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
