A,B = map(int,input().split())

current_sockets = 1
taps_used = 0
if not (current_sockets >= B):
    while current_sockets < B:
        taps_used += 1
        current_sockets = current_sockets + (A - 1)

print(taps_used)