def meditate(mana, max_mana, energy, energy_drinks):
    while mana < max_mana or (energy > 0 and energy_drinks < 0):
        if energy <=0 and energy_drinks >= 1:
            energy_drinks -= 1
            energy += 50
        elif energy <=0 and energy_drinks <=0:
            break
        energy-=1
        mana+=1
        

    return mana, energy, energy_drinks


#DO NOT TOUCH BELOW

run_cases = [
    (0, 10, 9, 0, [9, 0, 0]),
    (0, 12, 0, 1, [12, 38, 0]),
    (1, 100, 99, 2, [100, 0, 2]),
]

submit_cases = run_cases + [
    (0, 0, 0, 0, [0, 0, 0]),
    (1000, 1000, 200, 5, [1000, 200, 5]),
    (0, 10, 0, 2, [10, 40, 1]),
    (5, 2000, 250, 6, [555, 0, 0]),
]


def test(input1, input2, input3, input4, expected):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" *           mana: {input1}")
    print(f" *       max_mana: {input2}")
    print(f" *         energy: {input3}")
    print(f" *  energy_drinks: {input4}")
    print(
        f"Expecting: mana {expected[0]}, energy {expected[1]}, energy drinks {expected[2]}"
    )
    result_mana, result_energy, result_drinks = meditate(input1, input2, input3, input4)
    print(
        f"   Actual: mana {result_mana}, energy {result_energy}, energy drinks {result_drinks}"
    )
    if (
        result_mana == expected[0]
        and result_energy == expected[1]
        and result_drinks == expected[2]
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
