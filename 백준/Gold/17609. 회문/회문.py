


def palindrome(sen : str) :
    start = 0
    end = len(sen) - 1
    count = 0

    while True:
        # 가장 먼저 종료조건을 설정해준다
        if start >= end or count >= 2 :
            break
        else:
            # 만일 양 끝 값이 서로 같은 알파벳인 경우
            if sen[start] == sen[end] :
                start += 1
                end -= 1

            # 양 끝 값이 서로 다른 알파벳인 경우
            else: 
                count += 1
                # 앞 쪽 문자열 을 지웠을 경우 똑같아 지는 경우
                # 문자 제거후 나머지 값들이 앞뒤로 읽었을떄 동일한 경우
                if sen[start + 1] == sen[end] and sen[start + 1 : end + 1] == sen[start +1 : end + 1][::-1]:
                    start += 1
                # 뒤 쪽 문자열 을 지웠을 경우 똑같아 지는 경우
                # 문자 제거후 나머지 값들이 앞뒤로 읽었을떄 동일한 경우
                elif sen[start] == sen[end - 1] and sen[start : end] == sen[start : end][::-1]:
                    end -=1
                # 한쪽 만 지워서는 똑같아 지지 않는 경우
                # count = 2로 만들어서 종료시킨다.
                else :
                    count += 1

    if count == 0 :
        return 0
    elif count == 1:
        return 1
    else :
        return 2

N = int(input())

for i in range(N):
    # 여기서 단순히 input을 입력받게 되면 자꾸 end가 하나 크게 나오는데 '/n' 때문인거 같아 이를 제거하면서 입력을 받는다
    sen = input().strip()
    print(palindrome(sen))