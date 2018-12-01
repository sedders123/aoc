def captcha_solver(captcha: str) -> int:
    previous_char = None
    numbers = []  # type : List
    for char in captcha:
        # first letter
        if not previous_char:
            previous_char = char
            continue
        if char == previous_char:
            numbers.append(int(char))
        previous_char = char
    # Circular
    if captcha[0] == captcha[-1]:
        numbers.append(int(captcha[0]))
    return sum(numbers)


if __name__ == "__main__":
    with open("input.txt") as f:
        captcha = f.readline().rstrip()
        result = captcha_solver(captcha)
        print(result)
