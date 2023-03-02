def divisor(n):
    return list(filter(lambda x:n % x == 0, range(1, n+1)))

def GCD(n, m):
    return max(set(divisor(m)) & set(divisor(n)))

def LCM(a, b):
    return GCD(a, b) * (a // GCD(a, b)) * (b // GCD(a, b))

def solution(n):
    return LCM(n, 6) // 6
    