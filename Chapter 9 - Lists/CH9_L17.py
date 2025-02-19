def get_champion_slices(champions):
    # EXAMPLE
    # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # numbers[:3]  - Gives [0, 1, 2]
    # numbers[3:]  - Gives [3, 4, 5, 6, 7, 8, 9]
    # numbers[::2] - Gives [0, 2, 4, 6, 8]
    # numbers[-3:] - Gives [7, 8, 9]

    return champions[2:], champions[:-2], champions[::2]


#DO NOT TOUCH BELOW

run_cases = [
    (
        ["Thrundar", "Morgate", "Gandolfo", "Thraine", "Norwad", "Gilforn"],
        (
            ["Gandolfo", "Thraine", "Norwad", "Gilforn"],
            ["Thrundar", "Morgate", "Gandolfo", "Thraine"],
            ["Thrundar", "Gandolfo", "Norwad"],
        ),
    ),
    (
        ["Frank", "Dennis", "Sweet Dee", "Mac", "Charlie"],
        (
            ["Sweet Dee", "Mac", "Charlie"],
            ["Frank", "Dennis", "Sweet Dee"],
            ["Frank", "Sweet Dee", "Charlie"],
        ),
    ),
]

submit_cases = run_cases + [
    (
        (["John", "Sydney", "Spencer", "Bill", "Matthew", "Brandon", "Tony"]),
        (
            ["Spencer", "Bill", "Matthew", "Brandon", "Tony"],
            ["John", "Sydney", "Spencer", "Bill", "Matthew"],
            ["John", "Spencer", "Matthew", "Tony"],
        ),
    ),
    (([]), ([], [], [])),
]


def test(input1, expected_output):
    print("-" * 40)
    print(f"Input:\n{input1}")
    print(f"Expecting:\n{expected_output}")
    try:
        slice_1, slice_2, slice_3 = get_champion_slices(input1)
        result = (slice_1, slice_2, slice_3)
    except Exception as e:
        print(f"Error: {e}")
        return False
    print(f"Actual:\n{result}")
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
