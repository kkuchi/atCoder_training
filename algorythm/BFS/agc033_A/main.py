import sys
from collections import deque

def source():
    spi = lambda x: map(int, x.split())
    s = sys.stdin.read().splitlines()

    h, w = spi(s[0])
    grid = s[1:]

    return h, w, grid


def calc(h, w, grid):
    # 黒からの最短距離。初期値は-1
    dist = [[-1 for _ in range(w)] for _ in range(h)]
    # キュー
    q = deque()
    
    for h_ in range(h):
        for w_ in range(w):
            if grid[h_][w_] == '#':
                # 黒の座標をキューに
                q.append((h_, w_))
                # 黒の座標のdistを0に
                dist[h_][w_] = 0
    
    # 深さ(操作回数)
    d = 0
    # キューがなくなるまで繰り返し
    while q:
        # キューから座標取り出し
        height, width = q.popleft()
        # キューから取り出した座標の深さ（操作回数）
        d = dist[height][width]
        # 隣接マスのチェック
        for dy, dx in ((1,0), (0,1), (-1, 0), (0, -1)):
            # 隣接マスの座標
            new_h = height + dy
            new_w = width + dx
            # 隣接マスの座標がなければ飛ばす
            if new_h < 0 or h <= new_h or new_w < 0 or w <= new_w:
                continue
            # 隣接マスが未探索なら
            if dist[new_h][new_w] == -1:
                # 現在の座標のdist+1を隣接マスに
                dist[new_h][new_w] = d+1
                # 隣接マスをキューに
                q.append((new_h, new_w))
    
    return d


def main():
    h, w, grid = source()
    ans = calc(h, w, grid)
    print(ans)

if __name__ == '__main__':
    main()
