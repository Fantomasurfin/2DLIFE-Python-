import time
n = 0
map = [
[0,0,1,0,0],
[0,0,1,0,0],
[1,1,1,1,1],
[0,0,1,0,0],
[0,0,1,0,0]
]
map1 = [[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]]
def dot(x,y):
    if map[y][x] == 1:
        return 1
    else:
        return 0
def prof(x,y,map,map1):
    if y == 0:
        if x == 0:
            summa = map[y][x + 1] + map[y + 1][x] \
            + map[y + 1][x + 1]
        elif x == 4:
            summa = map[y][x - 1] + map[y + 1][
            x - 1] + map[y + 1][x]
        else:
            summa = map[y][x-1] + map[y][x+1] + map[y+1][x-1] + map[y+1][x] \
            + map[y+1][x+1]
    elif y == 4:
        if x == 0:
            summa = map[y - 1][x] + map[y - 1][x + 1] + map[y][x + 1]
        elif x == 4:
            summa = map[y - 1][x - 1] + map[y - 1][x] + map[y][x - 1]
        else:
            summa = map[y - 1][x - 1] + map[y - 1][x] + map[y - 1][x + 1] + map[y][x - 1] + map[y][x + 1]
    else:
        if x == 0:
            summa = map[y - 1][x] + map[y - 1][x + 1] + map[y][x + 1] + map[y + 1][x] \
            + map[y + 1][x + 1]
        elif x == 4:
            summa = map[y - 1][x - 1] + map[y - 1][x] + map[y][x - 1] + map[y + 1][
            x - 1] + map[y + 1][x]
        else:
            summa = map[y - 1][x - 1] + map[y - 1][x] + map[y - 1][x + 1] + map[y][x - 1] + map[y][x + 1] + map[y + 1][
            x - 1] + map[y + 1][x] \
            + map[y + 1][x + 1]
    if summa < 2 and dot(x,y) == 1:
        map1[y][x] = 0
    elif summa > 3 and dot(x,y) == 1:
        map1[y][x] = 0
    elif summa >= 2 and dot(x,y) == 0:
        map1[y][x] = 1


def scan(map,map1):
    for i in range(5):
        for j in range(5):
            prof(i,j,map,map1)
    map = map1
    print(map[0],map[1],map[2],map[3],map[4],"\n", sep="\n")
    return map

print(map[0],map[1],map[2],map[3],map[4],"\n", sep="\n")
while n == 0:
    time.sleep(1)
    map = scan(map,map1)
print("life top 1")