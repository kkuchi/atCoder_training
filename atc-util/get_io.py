import requests
from lxml import html
from os import getcwd
import sys

contest_id = sys.argv[1]
problem_id = sys.argv[2]

# リクエスト
ele = requests.get(f'https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_{problem_id}')
# 解析
tree = html.fromstring(ele.content)
# ioのdiv
target = tree.xpath(f'//*[@id="task-statement"]/span/span[1]/div')

io = []

# テキスト取り出し
for i in range(3, len(target), 2):
    item = {'in': target[i][0][1].text,
            'out': target[i+1][0][1].text}
    io += [item]

save_dir = getcwd()

for i, row in enumerate(io):
    for key in ['in', 'out']:
        with open(f'{save_dir}/{key}_{i+1}.txt', 'w') as f:
            f.write(row[key])