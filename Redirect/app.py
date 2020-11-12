#html 이 정적(Static) 인 주소인 경우(하드코딩)  app.route 의 주소가 변경되면 , html 에서도 수정을 해주어야 한다.
#html 에 수정해야 할 주소가 많다면 아주 비효율적.  
#해결을 위해 동적(Dynamic) 으로 변경이 될 수 있게 해야하는데, Flask app.route 에 연결된 함수 이름으로 app.route 의 URL을 받아올 수 있음 
#url_for() 을 사용. app.route 의 경로가 변경 되더라도, 함수 이름만 바꾸지 않으면 됨.

from flask import Flask , request , render_template , redirect, url_for

app = Flask(__name__) 

@app.route('/a')
def a():
    return redirect(url_for('b'))

@app.route('/b')
def b():
    print(" b 로의 리다이렉트")
    return redirect(url_for('c')) #함수 이름이 c 인 주소로 이동

@app.route('/c')
def c():
    return "c 로의 리다이렉트"



#test_request_context() :  with 구문과 같이 쓰이면서 임시로(일시적으로) request context 를 생성(활성화) 해준다. 
#request,g,session 객체에 view functions 처럼 접근할 수 있게 해준다.
 
if __name__ == "__main__":
    with app.test_request_context(): #Flask 인스턴스 안의 test_request_context() 호출 
        print(url_for('c'))   #테스트할 view 함수명 작성   => view 함수와 연결된 uri 를 어떻게 찾아내는지 알아보고자.  /c 와 같이 출력됌.

    app.run(debug=True) 