def solution(wallet, bill):
    answer = check_size(wallet,bill)
    print(answer)
    return answer

def check_size(wallet,bill):
    ford_count = 0

    # 반복되는 조건을 지정
    while max(bill) > max(wallet) or min(bill) > min(wallet):

        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2

        else:
            bill[1] = bill[1] // 2

        ford_count+=1

    return ford_count