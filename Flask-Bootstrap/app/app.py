from flask import Flask,render_template 
from flask_bootstrap import Bootstrap

#templates 가 원래 이름. 바꿔서 사용하려면 template_folder='바꿀 이름' 으로 지정 
app = Flask(__name__,template_folder='template')
Bootstrap(app) 
@app.route('/')
def index_page(): 
    return render_template('index.html') 

if __name__ =='__main__' :
    app.run(debug=True) 
    