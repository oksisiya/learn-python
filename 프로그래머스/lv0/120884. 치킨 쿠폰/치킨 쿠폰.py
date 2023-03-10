def solution(chicken):
    cnt = 0
    left = 0
    while True:
        div, mod = divmod(chicken, 10)
        cnt += div
        left += mod
        chicken = div
        if left >= 10:
            chicken += left // 10
            cnt += left // 10
            left %= 10
        if div == 0: break
    return cnt