from collections import deque

n, k = map(int, input().split())
stability = deque(list(map(int, input().split())))
person = deque([0 for _ in range(2 * n)])

trialCnt = 0
while stability.count(0) < k:
    # 무빙워크가 한 칸 회전합니다.
    stability.rotate(1)
    person.rotate(1)

    if person[n - 1]:
        person[n-1] = 0
        

    # 가장 먼저 무빙워크에 올라간 사람부터 무빙워크가 회전하는 방향으로 한 칸 이동할 수 있으면 이동합니다.
    for idx in range(n - 1, -1, -1):
        if stability[idx] > 0 and person[idx] == 0 and person[idx - 1] == 1:
            person[idx] = 1
            person[idx - 1] = 0
            stability[idx] = max(0, stability[idx] - 1)
    
    if person[n - 1]:
        person[n - 1] = 0

    # 1번 칸에 사람이 없고 안정성이 0이 아니라면 사람을 한 명 더 올립니다.
    if person[0] == 0 and stability[0] > 0:
        person[0] = 1
        stability[0] = max(0, stability[0] - 1)

    trialCnt += 1

print(trialCnt)