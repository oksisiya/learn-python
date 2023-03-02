def solution(age):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    b = []
    for i in str(age):
        b.append(a[int(i)])
    return ''.join(b)