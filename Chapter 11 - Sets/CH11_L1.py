def remove_duplicates(spells):
    # first resolution
    # spells_final = set()
    # for spell in spells:
    #     if spell not in spells_final:
    #         spells_final.add(spell)
    
    # spells_list = list(spells_final)
    # return spells_list

    #============================================

    #second resolution
    spells_set=set()

    spells_set = set(spells)
    spells_list = list(spells_set)

    return spells_list




#DO NOT TOUCH BELOW

run_cases = [
    (
        [
            "fireball",
            "eldritch blast",
            "fireball",
            "eldritch blast",
            "chill touch",
            "eldritch blast",
            "chill touch",
            "chill touch",
            "fireball",
            "fireball",
            "shocking grasp",
            "fireball",
            "fireball",
        ],
        ["chill touch", "eldritch blast", "fireball", "shocking grasp"],
    )
]

submit_cases = run_cases + [
    (["fireball", "fireball", "fireball"], ["fireball"]),
    (
        ["fireball", "eldritch blast", "chill touch", "shocking grasp"],
        ["chill touch", "eldritch blast", "fireball", "shocking grasp"],
    ),
    (["chill touch", "chill touch", "chill touch"], ["chill touch"]),
    (["shocking grasp", "shocking grasp", "shocking grasp"], ["shocking grasp"]),
    ([], []),
    (["eldritch blast", "eldritch blast", "eldritch blast"], ["eldritch blast"]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * spells: {input}")
    print(f"Expecting: {expected_output}")
    result = remove_duplicates(input)
    print(f"   Actual: {result}")
    if not isinstance(result, list):
        print("Fail: result is not a list")
        return False
    result.sort()
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
