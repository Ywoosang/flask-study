from flask import Flask,render_template,flash

app = Flask(__name__)


@app.route('/')
def mainPage():
    alert= {'cnt': "0", 'text': "회원가입 페이지로 이동합니다"}
    return render_template('main.html',message = alert) 

if __name__ == '__main__':
    app.run(debug=True)