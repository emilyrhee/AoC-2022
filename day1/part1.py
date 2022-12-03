with open('input.txt', 'r') as file:
    numbers: list = []
    sums: list = []

    for line in file.readlines():
        if line == "\n":
            sums.append(sum(numbers))
            numbers = []
        else:
            numbers.append(int(line))
    sums.append(sum(numbers))

    print(max(sums))