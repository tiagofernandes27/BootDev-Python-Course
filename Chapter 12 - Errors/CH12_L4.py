def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")


#DO NOT TOUCH BELOW

run_cases = [
    (1, {"name": "Slayer", "level": 128}),
    (4, Exception("player id not found")),
    (3, {"name": "Saruman", "level": 4000}),
]

submit_cases = run_cases + [
    (2, {"name": "Dorgoth", "level": 300}),
    (5, Exception("player id not found")),
    (0, Exception("player id not found")),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * player_id: {input1}")
    print(f"Expecting: {expected_output}")
    try:
        result = get_player_record(input1)
        print(f"Actual: {result}")
        if isinstance(expected_output, Exception):
            print("Fail -- expected exception")
            return False
        if result == expected_output:
            print("Pass")
            return True
    except Exception as e:
        print(f"Actual: {e}")
        if isinstance(expected_output, Exception) and str(e) == str(expected_output):
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
