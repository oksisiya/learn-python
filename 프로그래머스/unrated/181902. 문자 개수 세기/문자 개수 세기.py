def solution(my_string):
    ls_chr = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [chr(i) for i in range(ord('a'), ord('z') + 1)]
    answer = [0 for i in range(len(ls_chr))]
    
    for i in my_string:
        if i in ls_chr:
            answer[ls_chr.index(i)] += 1
    
    return answer