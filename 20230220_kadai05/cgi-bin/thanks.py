import cgitb
import io
import sys

cgitb.enable()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from html import escape


import cgi
flg1 = True
flg2 = True
kekka = ''
form = cgi.FieldStorage()

if 'email' in form:
    email = form.getfirst('email')
else:
    flg1 = False

if 'others' in form:
    others = form.getfirst('others')
else:
    flg2 = False

if flg1:
    kekka += f'<h2>Email</h2><br><p>{email}</p><br>'
else:
    kekka += f'<p style="color:red">emailは必須入力項目です</p>'  
if flg2:
    kekka += f'<h2>お問い合わせ内容</h2><br><p>{"<br>".join(escape(others).splitlines())}</p>'
else:
    kekka += f'<p style="color:red">お問い合わせ内容は必須入力項目です</p>'

if flg1 and flg2:
    kekka = '<p>以下の内容で受け付けました' + kekka
else:
    kekka = '<p>入力エラー<p><br>' + kekka





html = f'''\
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>お問い合わせ</h1>
    
    {kekka}
    
    
    <p><a href='/'>index</p>
    
</body>
</html>
'''


#HTTPヘッダ
print('Content-type: text/html')
    #text/css
    #image/img
print()  
#HTTPボディ
print(html)
