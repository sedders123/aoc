from typing import Union, Set

frequencies = set()  # type: Set

freq = 0


def do_it() -> Union[bool, int]:
    global frequencies
    global freq
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            freq += int(line)
            if freq in frequencies:
                return freq
            frequencies.add(freq)
    return False


if __name__ == "__main__":
    running = True
    i = 0
    while running:
        result = do_it()
        if result:
            print(result)
            running = False
        i += 1
