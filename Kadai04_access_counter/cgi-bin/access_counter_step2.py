# カウンターファイル読み込み(注意：カレントディレクトリはドキュメントルート)
with open('counter.txt', mode='r', encoding='utf-8') as f:
    count = f.read()

count = str(int(count) + 1)

# html作成
html = f'''\
<!doctype html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <p>{count}</p>
    </body>
</html>
'''

# httpデータのヘッダ部出力
print('Content-Type: text/html; charset=utf-8')

print()

# httpデータのボディ部出力
print(html)