def common_letter(string1, string2):
    for letter1 in string1:
        for letter2 in string2:
            if letter1 == letter2:
                return letter1


sum_priorities = 0
with open('input.txt') as f:
    all_rucksacks = f.read().splitlines()

for rucksack in all_rucksacks:
    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]
    common_item = common_letter(compartment1, compartment2)
    sum_priorities += ord(common_item) - 96 if ord(common_item) >= 97 else ord(common_item) - 38

print(sum_priorities)
