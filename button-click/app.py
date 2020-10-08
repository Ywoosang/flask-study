from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test", methods=['GET'])

def test():
    # jsonify 에 json 데이터를 넣어도 되는데, 보통 restAPI 의 결과값이 성공/실패 만 나타낼때
    # {'success':True} 도 가능
    # success 와 같은 경우는 True 또는 False 를 넣어서 return 가능 
    return make_response(jsonify(success=True), 200)
    # http status 를 명확하게 써서 같이 넘겨주기 위해 make_response를 사용한것. 

@app.route("/test", methods=['GET', 'POST', 'PUT', 'DELETE'])
def test():
    if request.method == 'POST':
        print ('POST')
        data = request.get_json()
        print (data['email'])
    if request.method == 'GET':
        print ('GET')
        user = request.args.get('email')
        print (user)
    if request.method == 'PUT':
        print ('PUT')
        user = request.args.get('email')
        print (user)
    if request.method == 'DELETE':
        print ('DELETE')
        user = request.args.get('email')
        print (user)

    return jsonify( {'status': 'success'} )  
    

if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port="8082")