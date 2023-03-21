S, K, H=map(int,input().split())
if S+K+H >=100:
    print("OK")
elif S+K+H<100:
    if min(S, K, H) == S:
        print("Soongsil")
    elif min(S, K, H) == K:
        print("Korea")
    elif min(S, K, H)==H:
        print("Hanyang")
# map 함수에 대해 좀 더 공부하기