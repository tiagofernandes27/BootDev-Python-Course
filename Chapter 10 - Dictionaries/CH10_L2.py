def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }


#DO NOT TOUCH BELOW

run_cases = [
    (
        "bloodwarrior123",
        "server1",
        5,
        1,
        {
            "name": "bloodwarrior123",
            "server": "server1",
            "level": 5,
            "rank": 1,
            "id": "bloodwarrior123#server1",
        },
    ),
    (
        "fronzenboi",
        "server2",
        2,
        1,
        {
            "name": "fronzenboi",
            "server": "server2",
            "level": 2,
            "rank": 1,
            "id": "fronzenboi#server2",
        },
    ),
]

submit_cases = run_cases + [
    (
        "slasher69",
        "server3",
        2,
        5,
        {
            "name": "slasher69",
            "server": "server3",
            "level": 2,
            "rank": 5,
            "id": "slasher69#server3",
        },
    ),
    (
        "kingofgames",
        "server4",
        3,
        2,
        {
            "name": "kingofgames",
            "server": "server4",
            "level": 3,
            "rank": 2,
            "id": "kingofgames#server4",
        },
    ),
    (
        "godofwar",
        "server5",
        1,
        5,
        {
            "name": "godofwar",
            "server": "server5",
            "level": 1,
            "rank": 5,
            "id": "godofwar#server5",
        },
    ),
    (
        "pythonista",
        "server6",
        4,
        3,
        {
            "name": "pythonista",
            "server": "server6",
            "level": 4,
            "rank": 3,
            "id": "pythonista#server6",
        },
    ),
    (
        "codemaster",
        "server7",
        3,
        1,
        {
            "name": "codemaster",
            "server": "server7",
            "level": 3,
            "rank": 1,
            "id": "codemaster#server7",
        },
    ),
]


def test(input1, input2, input3, input4, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    print(f"Expecting: {expected_output}")
    result = get_character_record(input1, input2, input3, input4)
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
