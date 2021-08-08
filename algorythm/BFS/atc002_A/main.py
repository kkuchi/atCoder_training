import sys
from collections import deque

def source():
    spi = lambda x: map(int, x.split())
    s = sys.stdin.read().splitlines()

    # 行と列
    r, c = spi(s[0])
    # スタートをcardinalに
    start = list(spi(s[1]))
    start[0] -= 1
    start[1] -= 1
    # ゴールをcardinalに
    goal = list(spi(s[2]))
    goal[0] -= 1
    goal[1] -= 1
    # 迷路
    C = s[3:r+3]

    return r,c, start, goal, C


# 経路計算
def calc(r,c, start, goal, C):
    # 最短距離。初期値は-1
    dist = [[-1 for _ in range(c)] for _ in range(r)]
    # キュー 初期値はstart
    q = deque([tuple(start)])
    # distのstartを0に
    dist[start[0]][start[1]] = 0

    while q:
        # キューから取り出し
        h, w = q.popleft()
        # ターゲット座標のdist
        d = dist[h][w]
        # 隣接マス
        for dy, dx in ((1,0), (0,1), (-1,0), (0,-1)):
            # 隣接マスの座標
            nh = h+dy
            nw = w+dx
            # 座標がない、あるいは壁であればcontinue
            if nh < 0 or r <= nh or nw < 0 \
            or c <= nw or C[nh][nw] == '#':
                continue
            # 未探索
            if dist[nh][nw] == -1:
                # ターゲットのdist+1を入れる
                dist[nh][nw] = d+1
                # 隣接マスをキューに
                q.append((nh, nw))
    # ゴール座標の結果をreturn
    return dist[goal[0]][goal[1]]


def main():
    r,c, start, goal, C = source()
    ans = calc(r,c, start, goal, C)
    print(ans)

if __name__ == '__main__':
    main()