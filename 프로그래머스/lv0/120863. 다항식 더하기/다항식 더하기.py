def solution(polynomial):
    ls = polynomial.split(' + ')
    a = []
    b = []
    
    for i in ls:
        if i == 'x': a.append(1)
        elif 'x' in i: a.append(int(i.replace('x', '')))
        else: b.append(int(i))
    
    if sum(a) == 0 and sum(b) == 0: return '0'
    if sum(a) == 0: return '{}'.format(sum(b))
    if sum(a) == 1 and sum(b) == 0: return 'x'
    if sum(a) == 1 and sum(b) != 0: return 'x + {}'.format(sum(b))
    if sum(b) == 0: return '{}x'.format(sum(a))
    else: return '{}x + {}'.format(sum(a), sum(b))