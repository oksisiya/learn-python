# def solution(date1, date2):
#     if date1 == date2: return 0
#     for i in range(3):
#         if date1[i] > date2[i]: return 0

#     return 1

def solution(date1, date2):
    if date1 == date2: return 0
    if date1[0] > date2[0] : return 0
    if date1[0] == date2[0] and date1[1] > date2[1]: return 0
    if date1[0] == date2[0] and date1[1] == date2[1] and date1[2] > date2[2]: return 0

    return 1