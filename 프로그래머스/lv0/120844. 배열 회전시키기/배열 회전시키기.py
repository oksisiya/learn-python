def solution(numbers, direction):
    b = []
    if direction == 'right':
        b.append(numbers[-1])
        for i in numbers[0:-1]:
            b.append(i)
    if direction == 'left':
        for i in numbers[1:]:
            b.append(i)
        b.append(numbers[0])
    return b