while True:
    try:
        n = int(input())
        first = 2
        case = 3
        num = (first + (n-1)*case+first)*n/2
        print(num)
    except Exception:
        print(-1)
        break