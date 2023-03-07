def solution(lines):
    ls = []
    lss = [[], [], []]
    for i in range(3):
        for j in range(lines[i][0], lines[i][1]):
            lss[i].append(j)
    return len((set(lss[0]) & set(lss[1])) | (set(lss[1]) & set(lss[2])) | (set(lss[2]) & set(lss[0])))