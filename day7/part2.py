from part1 import parse_filesystem, directory_size

with open('input.txt') as fin:
    fs = parse_filesystem(fin)

sizes = []
for path in fs:
    sizes.append(directory_size(path))

desc_sizes = sorted(sizes, reverse=True)
total_disk_space = 70000000
current_free_disk_space = total_disk_space - desc_sizes[0]

min_size_to_delete = 30000000 - current_free_disk_space

for size in sorted(sizes):
    if size >= min_size_to_delete:
        print('Part 2:', size)
        break





