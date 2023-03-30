import os

COUNTER_FILE = 'counter.txt'
ENCODING = 'utf-8'

# ファイルの存在確認
if os.path.exists(COUNTER_FILE):
    # カウンターファイル読み込み(注意：カレントディレクトリはドキュメントルート)
    with open(COUNTER_FILE, mode='r', encoding=ENCODING) as f:
        count = f.read()
else:
    count = 0

count = str(int(count) + 1)

# カウンターファイル書込み
with open(COUNTER_FILE, mode='w', encoding=ENCODING) as f:
    f.write(count)

counterHtml = ''
for oneChar in list(count):
    counterHtml += f'<img src="/img/{oneChar}.png" />'

# html作成
html = f'''\
<!doctype html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <p>{counterHtml}</p>
    </body>
</html>
'''

# httpデータのヘッダ部出力
print('Content-Type: text/html; charset=utf-8')

print()

# httpデータのボディ部出力
print(html)