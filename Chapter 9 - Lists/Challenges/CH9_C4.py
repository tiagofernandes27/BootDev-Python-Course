def validate_path(expected_path, character_path):
    percentage = float(0)
    total = 0
    count = 0
    
    character_name = character_path.pop(0)

    for i in range(0, len(expected_path)):
        total += 1
        if expected_path[i] in character_path:
            count += 1

    percentage = (count/total) * 100

    return character_name, percentage


#DO NOT TOUCH BELOW

run_cases = [
    (
        ["A", "B", "C", "D", "E"],
        ["Dellbi", "A", "B", "C", "D", "E"],
        ("Dellbi", 100.0),
    ),
    (
        ["A", "B", "C", "D", "E"],
        ["Kaladin", "A", "X", "C", "D", "E"],
        ("Kaladin", 80.0),
    ),
]

submit_cases = run_cases + [
    (
        ["A", "B", "C", "D", "E"],
        ["ShadowWalker", "X", "X", "X", "X", "X"],
        ("ShadowWalker", 0.0),
    ),
    (
        ["A", "B", "C", "D", "E"],
        ["Jamie", "A", "B", "X", "X", "E"],
        ("Jamie", 60.0),
    ),
    (
        ["A", "B", "C", "D", "E"],
        ["Odium", "A", "B", "C", "D", "E"],
        ("Odium", 100.0),
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:\nexpected_path: {input1}\ncharacter_path: {input2}")
    print(f"Expecting: {expected_output}")
    result = validate_path(input1, input2)
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
