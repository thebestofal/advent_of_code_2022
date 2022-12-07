with open('input.txt') as f:
    datastream = f.read()


def find_start_packet(datastream, size_of_header_of_message):
    for i in range(len(datastream) - size_of_header_of_message - 1):
        buffer = {datastream[i + offset] for offset in range(size_of_header_of_message)}
        if len(buffer) == size_of_header_of_message:
            return i + size_of_header_of_message


print(find_start_packet(datastream, 14))
