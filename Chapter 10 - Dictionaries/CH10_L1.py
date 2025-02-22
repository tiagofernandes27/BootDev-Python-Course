def get_character_record(name, server, level, rank):
    character = {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id":f"{name}#{server}"
    }
    return character


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
        "icequeen",
        "server4",
        3,
        2,
        {
            "name": "icequeen",
            "server": "server4",
            "level": 3,
            "rank": 2,
            "id": "icequeen#server4",
        },
    ),
    (
        "shadowmaster",
        "server5",
        4,
        3,
        {
            "name": "shadowmaster",
            "server": "server5",
            "level": 4,
            "rank": 3,
            "id": "shadowmaster#server5",
        },
    ),
    (
        "silentslasher",
        "server6",
        5,
        4,
        {
            "name": "silentslasher",
            "server": "server6",
            "level": 5,
            "rank": 4,
            "id": "silentslasher#server6",
        },
    ),
    (
        "hypershadow",
        "server7",
        3,
        5,
        {
            "name": "hypershadow",
            "server": "server7",
            "level": 3,
            "rank": 5,
            "id": "hypershadow#server7",
        },
    ),
]


def test(name, server, level, rank, expected_output):
    try:
        result = get_character_record(name, server, level, rank)
        for key, value in expected_output.items():
            print(f"Expected: {key}: {value}")
            print(f"Actual:   {key}: {result[key]}\n")
            if result[key] != value:
                if type(result[key]) != type(value):
                    print(f"'{key}' values are different types!")
                    print(
                        f"Expected '{key}' to be of type {type(value).__name__}, but got {type(result[key]).__name__}"
                    )
                print("Fail")
                return False
        if result != expected_output:
            print("Result object is incorrect:")
            for key, value in result.items():
                print(f" * {key}: {value}")
            print("Fail")
            return False
        print("Pass")
        return True
    except Exception as e:
        print(f"Exception: {str(e)}")
        print("Fail")
        return False


def main():
    index = 0
    passed = 0
    failed = 0
    for test_case in test_cases:
        index += 1
        print("---------------------------------")
        print(f"Test Case #{index}\n")
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
