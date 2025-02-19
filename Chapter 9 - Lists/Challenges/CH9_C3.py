def check_ingredient_match(recipe, ingredients):
    percentage = float(0)
    missing_ingredients = []

    total = 0
    counter = 0
    for i in range(0, len(recipe)):
        total+=1
        if recipe[i] in ingredients:
            counter+=1
        else:
            missing_ingredients.append(recipe[i])
            
    percentage = (counter/total) * 100
    return percentage, missing_ingredients



#DO NOT TOUCH BELOW

run_cases = [
    (
        [
            "Dragon Scale",
            "Unicorn Hair",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        [
            "Dragon Scale",
            "Goblin Ear",
            "Phoenix Feather",
            "Elf Dust",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        (75.0, ["Unicorn Hair", "Troll Tusk"]),
    ),
    (
        [
            "Dragon Scale",
            "Unicorn Hair",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
        ],
        [
            "Dragon Scale",
            "Phoenix Feather",
            "Unicorn Hair",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
        ],
        (100.0, []),
    ),
]

submit_cases = run_cases + [
    (
        [
            "Dragon Scale",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
            "Unicorn Hair",
        ],
        [
            "Goblin Ear",
            "Elf Dust",
            "Griffin Feather",
            "Mermaid Tear",
            "Goblin Ear",
            "Phoenix Feather",
            "Troll Tusk",
            "Unicorn Hair",
        ],
        (
            75.0,
            [
                "Dragon Scale",
                "Mandrake Root",
            ],
        ),
    ),
    (
        [
            "Dragon Scale",
            "Unicorn Hair",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        [
            "Unicorn Hair",
            "Dragon Scale",
            "Phoenix Feather",
            "Troll Tusk",
            "Griffin Feather",
            "Mandrake Root",
            "Goblin Ear",
            "Elf Dust",
        ],
        (100.0, []),
    ),
    (
        [
            "Orc Tears",
            "Orge Ear",
            "Goblin Giggles",
            "Witch Broom",
            "Giant Toenail Clipping",
            "Centipede Foot",
            "Dog Hair",
            "Bald Eagle Dandruff",
        ],
        [
            "Unicorn Hair",
            "Dragon Scale",
            "Phoenix Feather",
            "Troll Tusk",
            "Griffin Feather",
            "Mandrake Root",
            "Goblin Ear",
            "Bald Eagle Dandruff",
        ],
        (
            12.5,
            [
                "Orc Tears",
                "Orge Ear",
                "Goblin Giggles",
                "Witch Broom",
                "Giant Toenail Clipping",
                "Centipede Foot",
                "Dog Hair",
            ],
        ),
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:\nrecipe: {input1}\ngathered_ingredients: {input2}")
    print(f"Expecting: {expected_output}")
    result = check_ingredient_match(input1, input2)
    print(f"Actual: {result}")
    if result[0] == expected_output[0] and sorted(result[1]) == sorted(
        expected_output[1]
    ):
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
