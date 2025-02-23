def calculate_total(items_purchased, pinned_list):
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }

    # Don't touch above this line

    # checks which items haven't been purchased by going through the pinned
    # list of items and verifying if each item is in the purchased items list
    unpurchased_items = []
    for item in pinned_list:
        if item not in items_purchased:
            unpurchased_items.append(item)
    
    receipt = {}
    for item in items_purchased:
        if item in item_prices:
            receipt[item] = item_prices[item]

    total_cost = float()
    for item in receipt:
        total_cost += receipt[item]

    print(f"unpurchased items : {unpurchased_items}")
    print(f"receipt : {receipt}")
    print(f"total cost : {total_cost}")

    return unpurchased_items, receipt,total_cost


#DO NOT TOUCH BELOW

run_cases = [
    (
        (
            [
                "health_potion",
                "mana_potion",
                "gold_dust",
                "herbs",
                "crystal_shard",
                "dwarven_ale",
            ],
            [
                "health_potion",
                "mana_potion",
                "ice_cold_milk",
                "gold_dust",
                "herbs",
                "crystal_shard",
                "magic_ring",
                "dwarven_ale",
                "mystic_amulet",
            ],
        ),
        (
            ["ice_cold_milk", "magic_ring", "mystic_amulet"],
            {
                "health_potion": 10.00,
                "mana_potion": 12.00,
                "gold_dust": 5.00,
                "herbs": 7.00,
                "crystal_shard": 20.00,
                "dwarven_ale": 8.00,
            },
            62.00,
        ),
    ),
]

submit_cases = run_cases + [
    (
        (
            ["health_potion", "gold_dust", "herbs", "crystal_shard"],
            [
                "health_potion",
                "mana_potion",
                "gold_dust",
                "ice_cold_milk",
                "herbs",
                "magic_ring",
                "crystal_shard",
                "mystic_amulet",
            ],
        ),
        (
            ["mana_potion", "ice_cold_milk", "magic_ring", "mystic_amulet"],
            {
                "health_potion": 10.00,
                "gold_dust": 5.00,
                "herbs": 7.00,
                "crystal_shard": 20.00,
            },
            42.00,
        ),
    ),
    (
        (
            [
                "health_potion",
                "mana_potion",
                "gold_dust",
                "ice_cold_milk",
                "herbs",
                "magic_ring",
                "crystal_shard",
                "mystic_amulet",
            ],
            ["health_potion", "gold_dust", "herbs", "crystal_shard"],
        ),
        (
            [],
            {
                "health_potion": 10.00,
                "mana_potion": 12.00,
                "gold_dust": 5.00,
                "ice_cold_milk": 50.00,
                "herbs": 7.00,
                "magic_ring": 100.00,
                "crystal_shard": 20.00,
                "mystic_amulet": 150.00,
            },
            354.00,
        ),
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    try:
        unpurchased_items, receipt, total_cost = calculate_total(*input1)
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False
    result = (unpurchased_items, receipt, total_cost)
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
