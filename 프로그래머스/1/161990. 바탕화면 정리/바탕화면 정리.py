def solution(wallpaper):
    answer = []
    wallpaper = list(map(lambda x: list(x), wallpaper))
    lux,luy,rdx,rdy = len(wallpaper),len(wallpaper[0]),0,0
    for i,x in enumerate(wallpaper):
        for j,y in enumerate(x):
            if wallpaper[i][j] == '#':
                if rdx < i:
                    rdx = i
                if lux > i:
                    lux = i
                if luy > j:
                    luy = j
                if rdy < j:
                    rdy = j
    return [lux,luy,rdx+1,rdy+1]