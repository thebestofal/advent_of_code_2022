from collections import deque, defaultdict
from functools import lru_cache


# https://github.com/mebeim/aoc/tree/master/2022#day-7---no-space-left-on-device
def parse_filesystem(fin):
    lines = deque(fin)
    fs = defaultdict(list)
    path = ()

    while lines:
        line = lines.popleft().split()  # ['$', 'cd', 'foo']
        command = line[1]
        args = line[2:]  # ['foo'] or [] in case the command is `ls`

        if command == 'ls':
            # The `ls` command outputs a list of directory contents, keep going
            # until we either run out of lines or the next line is not a command
            while lines and not lines[0].startswith('$'):
                # Get the size of the file
                size = lines.popleft().split()[0]

                # Skip if not a file
                if size == 'dir':
                    continue

                # Add the size of the file to the contents of the current path
                fs[path].append(int(size))
        else:
            # The `cd` command has no output, but changes the current path
            if args[0] == '..':
                # Discard last path component (go up one directory)
                path = path[:-1]
            else:
                # Calculate path of the directory we are moving into
                new_path = path + (args[0],)
                # Add its path to the contents of the current directory
                fs[path].append(new_path)
                # Move into the new directory
                path = new_path

    return fs


def directory_size(fs, path):
    size = 0

    for subdir_or_size in fs[path]:
        if isinstance(subdir_or_size, int):
            # File, add size to total
            size += subdir_or_size
        else:
            # Directory, recursively calculate size
            size += directory_size(subdir_or_size)

    return size


with open('input.txt') as fin:
    fs = parse_filesystem(fin)


@lru_cache(maxsize=None)
def directory_size(path):
    size = 0

    for subdir_or_size in fs[path]:
        if isinstance(subdir_or_size, int):
            size += subdir_or_size
        else:
            size += directory_size(subdir_or_size)

    return size


small_dir_total = 0
for path in fs:
    sz = directory_size(path)
    if sz <= 100000:
        small_dir_total += sz

print('Part 1:', small_dir_total)
