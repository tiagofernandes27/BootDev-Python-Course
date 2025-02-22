def merge(dict1, dict2):
    dict3 = {}
    for score in dict1:
        if score not in dict3:
            dict3[score] = dict1[score]
    
    for score in dict2:
        if score not in dict3:
            dict3[score] = dict2[score]
        else:
            dict3[score] = dict2[score]
        

    #print(dict3)
    return dict3


def total_score(score_dict):
    total = 0
    for score in score_dict:
        total += score_dict[score]

    return total


#DO NOT TOUCH BELOW

run_cases = [
    (
        {"first_quarter": 24, "second_quarter": 31},
        {"third_quarter": 29, "fourth_quarter": 40},
        124,
    ),
    (
        {"first_quarter": 12, "second_quarter": 2},
        {"third_quarter": 32, "fourth_quarter": 87},
        133,
    ),
    ({}, {}, 0),
]

submit_cases = run_cases + [
    (
        {"first_quarter": 25, "second_quarter": 2},
        {"third_quarter": 31, "fourth_quarter": 0},
        58,
    ),
    (
        {"first_quarter": 25, "second_quarter": 2},
        {"second_quarter": 3, "third_quarter": 31, "fourth_quarter": 0},
        59,
    ),
    (
        {"first_quarter": 10, "second_quarter": 20},
        {"third_quarter": 30, "fourth_quarter": 40},
        100,
    ),
    (
        {"first_quarter": 15, "second_quarter": 25},
        {"third_quarter": 0, "fourth_quarter": 0},
        40,
    ),
    (
        {"first_quarter": 0, "second_quarter": 0},
        {"third_quarter": 0, "fourth_quarter": 0},
        0,
    ),
    (
        {"first_quarter": 100, "second_quarter": 100},
        {"third_quarter": 100, "fourth_quarter": 100},
        400,
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * first_half: {input1}")
    print(f" * second_half: {input2}")
    print(f"Expecting: {expected_output}")
    merged = merge(input1, input2)
    result = total_score(merged)
    print(f"Actual: {result}")
    if result == expected_output:
        if len(merged) == 4 or expected_output == 0:
            print("Pass")
            return True
        print("Dictionaries merged incorrectly")
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
