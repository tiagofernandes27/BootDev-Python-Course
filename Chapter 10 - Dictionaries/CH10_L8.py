def get_most_common_enemy(enemies_dict):
    max_count = float("-inf")
    max_name = None
    for enemy in enemies_dict:
        enemy_count = enemies_dict[enemy]
        if enemy_count > max_count:
            max_count = enemy_count
            max_name = enemy
    
    return max_name


#DO NOT TOUCH BELOW

run_cases = [
    ({"jackal": 4, "kobold": 3, "soldier": 10, "gremlin": 5}, "soldier"),
    ({"jackal": 1, "kobold": 3, "soldier": 2, "gremlin": 5}, "gremlin"),
]

submit_cases = run_cases + [
    ({"jackal": 2, "gremlin": 7}, "gremlin"),
    ({"jackal": 3}, "jackal"),
    ({}, None),
    ({"kobold": 5, "soldier": 5, "gremlin": 5, "dragon": 5}, "kobold"),
    ({"jackal": 5, "kobold": 3, "soldier": 10, "gremlin": 5, "dragon": 20}, "dragon"),
    ({"jackal": 5, "kobold": 3, "soldier": 2, "gremlin": 10, "dragon": 1}, "gremlin"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_most_common_enemy(input1)
    if result == "None":
        print('Actual: "None"')
    else:
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
