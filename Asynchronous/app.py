from flask import Flask,render_template,request,make_response,jsonify
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)

@app.route('/',methods=["POST","GET"]) 
def test():
    if request.method == "POST" : 
        print(request.data)
        print(request.get_json) #get_json() 을 이용해 딕셔너리로 바꿈
         
        response = {
            'res' : 'okay'
        }
        return make_response(jsonify(response),200)
          
    else :
        return render_template("index.html")

if __name__ == "__main__" : 
    app.run(debug=1)