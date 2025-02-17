def player_status(health):
    if(health <= 0):
        return "dead"
    elif health <=5:
        return "injured"
    else :
        return "healthy"


#DO NOT TOUCH BELOW
run_cases = [
    (0, "dead"),
    (4, "injured"),
]

submit_cases = run_cases + [
    (6, "healthy"),
    (5, "injured"),
    (1, "injured"),
    (10, "healthy"),
    (-1, "dead"),
]


def test(health, expected_status):
    print("---------------------------------")
    print(f"Health: {health}")
    print(f"Expecting: {expected_status}")
    result = player_status(health)
    print(f"Result: {result}")
    if result == expected_status:
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
