with open('input.txt') as f:
    assignments = f.read().splitlines()

sum_assignments_overlap = 0

for line in assignments:
    elves = line.split(',')
    elf1 = tuple(int(item) for item in elves[0].split('-'))
    elf2 = tuple(int(item) for item in elves[1].split('-'))
    elf1_set = {x for x in range(elf1[0], elf1[1]+1)}
    elf2_set = {x for x in range(elf2[0], elf2[1]+1)}
    if elf1_set & elf2_set:
        sum_assignments_overlap += 1

print(sum_assignments_overlap)
