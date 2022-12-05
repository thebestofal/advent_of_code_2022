def common_letters(string1, string2):
    common_string1_string2 = []
    for letter1 in string1:
        for letter2 in string2:
            if letter1 == letter2:
                common_string1_string2.append(letter1)
    return common_string1_string2


def common_letter(list_of_letters, string):
    for letter in list_of_letters:
        if letter in string:
            return letter

    return 'No letter found'


def common_letter_3(string1, string2, string3):
    common_letters_s1_s2 = common_letters(string1, string2)
    return common_letter(common_letters_s1_s2, string3)


sum_priorities = 0
with open('input.txt') as f:
    all_elves = f.read().splitlines()

elf_groups = [all_elves[x:x+3] for x in range(0, len(all_elves), 3)]

for group in elf_groups:
    common_item = common_letter_3(group[0], group[1], group[2])
    sum_priorities += ord(common_item) - 96 if ord(common_item) >= 97 else ord(common_item) - 38

print(sum_priorities)
