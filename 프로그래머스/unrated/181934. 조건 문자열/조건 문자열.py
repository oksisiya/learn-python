def solution(ineq, eq, n, m):
    operator = ineq + eq
    
    if ineq + eq == '>!': operator = '>'
    if ineq + eq == '<!': operator = '<'
    
    return 1 if eval(str(n) + operator + str(m)) else 0