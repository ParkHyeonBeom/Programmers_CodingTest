def solution(mats, park):
    rows = len(park)          # park의 행 개수
    cols = len(park[0])       # park의 열 개수
    max_side_length = 0       # 최대 정사각형의 한 변 길이를 저장할 변수

    # 각 위치에서 시작
    for i in range(rows):
        for j in range(cols):
            # 현재 위치가 "-1"이라면
            if park[i][j] == '-1':
                # 가능한 정사각형의 한 변의 길이를 계산하기 위해 최대 크기를 설정
                possible_side_length = 0

                # 정사각형의 한 변의 길이를 찾기
                while (i + possible_side_length < rows and
                       j + possible_side_length < cols and
                       all(park[i + k][j + possible_side_length] == '-1' for k in range(possible_side_length + 1)) and
                       all(park[i + possible_side_length][j + k] == '-1' for k in range(possible_side_length + 1))):
                    possible_side_length += 1

                # 최대 정사각형의 한 변 길이 업데이트
                max_side_length = max(max_side_length, possible_side_length)

    # 가능한 돗자리의 길이 중에서 최대 길이와 비교
    possible_mats = [mat for mat in mats if mat <= max_side_length]

    # 가장 큰 돗자리의 길이를 반환 (없으면 -1)
    return max(possible_mats) if possible_mats else -1