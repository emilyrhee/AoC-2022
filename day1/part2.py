with open('input.txt', 'r') as file:
    numbers: list = []
    sums: list = []
    top_3: list = []

    for line in file.readlines():
        if line == "\n":
            sums.append(sum(numbers))
            numbers = []
        else:
            numbers.append(int(line))
    sums.append(sum(numbers))

    for _ in range(3):
        top_3.append(max(sums))
        sums.remove(max(sums))
    
    print(sum(top_3))