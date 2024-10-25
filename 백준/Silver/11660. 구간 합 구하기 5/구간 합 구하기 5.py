import sys
input = sys.stdin.readline

# 표의 크기와, 합을 구하는 횟수를 저장
n,m = map(int,input().split())

# 입력받을 원본 리스트 초기화
# [0,1,2,3,4] 같은 형태로 인덱스 혼란을 방지하기 위함
A = [[0] * (n+1)]

# 2차원 배열 합 리스트 초기화
# [0,0,0,0,0]
# [0,1,2,3,4]
# [0,2,3,4,5]
# [0,3,4,5,6]
# [0,4,5,6,7] 과 같은 형태로 인덱스 혼란을 방지하기 위함
D = [[0] * (n+1) for _ in range(n+1)]

# 입력받은 원본 리스트를 가공 [0,1,2,3,4] -> 0은 배열의 인덱스가 0부터 시작하는 불편함 개선을 위함
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# 배열 합 구하는 과정
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 배열 합을 통해 구간 합 구하는 과정
for m in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    result = D[x2][y2]-D[x1-1][y2]-D[x2][y1-1]+D[x1-1][y1-1]
    print(result)