def recursive(A, B, C):
    if B == 1 : 
        return A % C

    else :
        temp = recursive(A, B // 2, C)

        if B % 2 == 0 :
            return (temp * temp) % C
        
        else :
            return (temp * temp * A) % C


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    print(recursive(A,B,C))