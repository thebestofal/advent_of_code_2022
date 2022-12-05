max_cal_elf = 0
curr_cal_elf = 0
with open('input.txt') as f:
    for line in f:
        if line == '\n':
            if curr_cal_elf > max_cal_elf:
                max_cal_elf = curr_cal_elf
                curr_cal_elf = 0
            else:
                curr_cal_elf = 0
        else:
            curr_cal_elf += int(line)
print(max_cal_elf)
