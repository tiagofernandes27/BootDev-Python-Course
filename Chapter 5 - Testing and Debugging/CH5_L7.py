#edited function
def unlock_achievement(before_xp, ach_xp, ach_name):
    return before_xp+ach_xp, f"Achievement Unlocked: {ach_name}"


#do not touch below
run_cases = [
    (100, 20, "Speedster", (120, "Achievement Unlocked: Speedster")),
    (200, 50, "Killer", (250, "Achievement Unlocked: Killer")),
]

submit_cases = run_cases + [
    (100, 50, "Unstoppable", (150, "Achievement Unlocked: Unstoppable")),
    (400, 75, "Gnarly", (475, "Achievement Unlocked: Gnarly")),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    print(f"Expecting: {expected_output}")
    result = unlock_achievement(input1, input2, input3)
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
