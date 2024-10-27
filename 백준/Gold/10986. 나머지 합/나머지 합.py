# 다 돌려보고
# 일일이 테스트하는 방법
# 그때의 인덱스를 기억
# 비효율적인 로직
# 시간 복잡도를 어떻게 줄일 수 있을까
# (1+2) % 3 = (1%3)+(2%3)는 동일하다
# S[I] - S[J] = J+1부터 I까지의 구간합을 의미한다
# 최종 로직 정리
# 1. 원본 배열을 바탕으로 구간 합 배열 생성
# 2. 생성된 구간합 배열을 바탕으로 입력받운 몫으로 나누어 나머지 값으로 업데이트
# 3. 업데이트 된 나머지 배열에서 0안 값울 조회
# 4. 동일한 값을 갖는 경우의 컴비네이션 연산 수행
# Ex) 1-> 3개, 2->2개 => 3C2 + 2C2 => 4개

# N과 M값 입력받기
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * N
U = [0] * M
Answer = 0

# 구간합 배열 생성
S[0] = A[0]
for i in range(1,N):
    S[i] = S[i-1] + A[i]

# 구간합을 통한 나머지 배열 생성
for i in range(N):
    remainder = S[i] % M
    if remainder == 0:
        Answer += 1
    U[remainder] += 1

for i in range(M):
    if U[i] > 0:
        Answer += U[i] * (U[i]-1) / 2

print(int(Answer))














