def total_calories_top_n_elves(n):
    all_elfs = []
    with open('input.txt') as f:
        curr_elf = []
        for line in f:
            if line != '\n':
                curr_elf.append(int(line))
            else:
                all_elfs.append(curr_elf)
                curr_elf = []

    result = sorted([sum(elf) for elf in all_elfs], reverse=True)
    return sum(result[0:n])


print(total_calories_top_n_elves(3))