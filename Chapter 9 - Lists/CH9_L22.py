def get_first_item(items):
    if items:
        return items[0]
    return "ERROR"


#DO NOT TOUCH BELOW

run_cases = [
    ([1, 2], 1),
    (["Healing Potion"], "Healing Potion"),
    ([], "ERROR"),
]

submit_cases = run_cases + [
    (["Iron Ore", "Iron Bar", "Scimitar"], "Iron Ore"),
    (["Apple", "Banana", "Cherry"], "Apple"),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]),
    ([False, True, False], False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_first_item(input1)
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
