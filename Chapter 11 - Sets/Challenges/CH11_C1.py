def remove_duplicates(lst):
    return set(lst)


#DO NOT TOUCH BELOW

run_cases = [
    (
        [
            "Frostmourne",
            "Abyssal Whip",
            "Staff of Armadyl",
            "Frostmourne",
            "Abyssal Whip",
        ],
        {"Frostmourne", "Abyssal Whip", "Staff of Armadyl"},
    ),
    (
        [
            "Ashbringer",
            "Dragonfire Shield",
            "Serpentine Helm",
            "Ashbringer",
            "Dragonfire Shield",
            "Infinity Boots",
            "Serpentine Helm",
        ],
        {"Ashbringer", "Dragonfire Shield", "Serpentine Helm", "Infinity Boots"},
    ),
]

submit_cases = run_cases + [
    (
        [
            "Bandos Chestplate",
            "Shadowmourne",
            "Twisted Bow",
            "Bandos Chestplate",
            "Shadowmourne",
            "Twisted Bow",
        ],
        {"Bandos Chestplate", "Shadowmourne", "Twisted Bow"},
    ),
    ([], set()),
    (["Zulrah's Scales", "Zulrah's Scales", "Zulrah's Scales"], {"Zulrah's Scales"}),
    (
        [
            "Void Knight Armor",
            "Torva Full Helm",
            "Void Knight Armor",
            "Torva Full Helm",
        ],
        {"Void Knight Armor", "Torva Full Helm"},
    ),
    (
        [
            "Abyssal Dagger",
            "Armadyl Godsword",
            "Bandos Tassets",
            "Abyssal Dagger",
            "Armadyl Godsword",
            "Bandos Tassets",
        ],
        {"Abyssal Dagger", "Armadyl Godsword", "Bandos Tassets"},
    ),
    (
        [
            "Elysian Spirit Shield",
            "Twisted Bow",
            "Scythe of Vitur",
            "Harmonised Orb",
            "Elysian Spirit Shield",
            "Twisted Bow",
            "Scythe of Vitur",
            "Harmonised Orb",
        ],
        {"Elysian Spirit Shield", "Twisted Bow", "Scythe of Vitur", "Harmonised Orb"},
    ),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input list: {input}")
    print(f"Expected set: {expected_output}")
    result = remove_duplicates(input)
    print(f"Actual set: {result}")
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
