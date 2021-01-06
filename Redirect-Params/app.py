#html 이 정적(Static) 인 주소인 경우(하드코딩)  app.route 의 주소가 변경되면 , html 에서도 수정을 해주어야 한다.
#html 에 수정해야 할 주소가 많다면 아주 비효율적.  
#해결을 위해 동적(Dynamic) 으로 변경이 될 수 있게 해야하는데, Flask app.route 에 연결된 함수 이름으로 app.route 의 URL을 받아올 수 있음 
#url_for() 을 사용. app.route 의 경로가 변경 되더라도, 함수 이름만 바꾸지 않으면 됨.

from flask import Flask , request , render_template , redirect, url_for

app = Flask(__name__) 

#url_for() 는 함수 이름에 해당하는 주소

#url_for 로 리다이렉트 할 때 params 전달
@app.route('/user')
def make_user():
    name='Ywoosang' 
    age = 22 
    return redirect(url_for('get_user',name=name,age=age))

@app.route('/user/<name>/<age>')
def get_user(name,age):
    return 'name : %s age: %s' % (name,age) 
 
# default path 설정 
@app.route('/path', defaults={'path': ''})
@app.route('/path/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path 


#페이지간 리다이렉트
@app.route('/page')
def start_page():
    print('start redirect')
    return redirect(url_for('first_page'))

@app.route('/page/first')
def first_page():
    print("redirect to page_first : url is %s" % url_for('first_page'))  
    return redirect(url_for('second_page'))

@app.route('/page/second')
def second_page():
    print("redirect to second_page : url is %s" % url_for('second_page'))  
    return redirect(url_for('third_page'))  

@app.route('/page/third')
def third_page():
    print("redirect to third_page : url is %s" % url_for('third_page'))  
    return "this is page content" 

 
if __name__ == "__main__":
    app.run(debug=True) 