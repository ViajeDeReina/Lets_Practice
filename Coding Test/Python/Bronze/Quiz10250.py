def get_roomnum (h,w,p):
    floor = p%h
    if floor == 0:
        if p//h >= 10:
            room_num = str(h) + str(p//h)
        else:
            room_num = str(h) + str(0) + str(p//h)
    else:
        if (p//h)+1 >= 10:
            room_num = str(floor) + str((p//h)+1)
        else:
            room_num = str(floor) + str(0) + str((p//h)+1)
    return room_num

n = int(input())

for i in range(n):
    h,w,p = map(int, input().split())
    room_num = get_roomnum(h,w,p)
    print(room_num)