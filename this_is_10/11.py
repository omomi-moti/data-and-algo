N = int(input())

info = []

for i in range(N):
    info.append(tuple(map(int,input().split())))

current_t = 0
current_x = 0
current_y = 0

can = True

for desitination in info:
    t_next = desitination[0]
    x_next = desitination[1]
    y_next = desitination[2]

    dt = t_next - current_t

    dd = abs(x_next - current_x) + abs(y_next - current_y)

    if dt < dd:
        can = False
        print("No")
        break
    if (dt - dd ) % 2 != 0:
        can = False
        print("No")
        break

    current_t = t_next
    current_x = x_next
    current_y = y_next

if can:
    print("Yes")  

#dd と　ddの使い方についての理解が大切