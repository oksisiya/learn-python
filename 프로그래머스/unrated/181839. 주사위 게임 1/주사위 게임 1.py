def solution(a, b):
    if a % 2 != 0 and b % 2 != 0: return a * a + b * b
    if a % 2 != 0 or b % 2 != 0: return 2 * (a + b)
    if a % 2 == 0 and b % 2 == 0: return abs(a - b)