from flask import Flask, request, render_template
from random import choice
from string import ascii_uppercase

app = Flask(__name__)

@app.route('/Сокращение ссылок')
def short_url():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

a=''.join(choice(ascii_uppercase) for i in range(12))
print(a)