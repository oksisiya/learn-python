def solution(num_list, n):
    ls = []
    for i in range(int(len(num_list)/n)):
        ls.append(num_list[n*i:n*i+n])
    return ls