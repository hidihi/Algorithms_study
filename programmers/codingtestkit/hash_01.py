# 해결1
def solution1(participant, completion):
    answer = ''
    try:
        for name in participant:
            answer = name
            completion.remove(name)
    except:
        return print(answer)

p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]
solution1(p, c)

#해결2
def solution2(participant, completion):
    answer = ''
    p_dict = {}
   # 매 사람이 몇번 등장하는지 count
    for p in participant:
        if p not in p_dict:
            p_dict[p] = 1
        else:
            p_dict[p] += 1  # 같은 이름이 또 등장할 때
    # 완주한 명단을 이용해서 하나씩 빼기
    for c in completion:
        p_dict[c] -= 1
   # 여전히 1을 가진 선수가 완주 못한 선수
    result = [key for key, value in p_dict.items() if value > 0]
    answer = result[0]

    return print(answer)

solution2(p, c)


def solution(participant, completion):
    answer = ''
    