with open('input.txt') as f:
    datastream = f.read()


def find_start_packet(datastream):
    for i in range(len(datastream)-3):
        buffer = {datastream[i + offset] for offset in range(4)}
        if len(buffer) == 4:
            return i + 4


print(find_start_packet(datastream))
