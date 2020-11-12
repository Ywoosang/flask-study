from app import app  #__init__.py 에 있는 app 을 가져온다.
# app = Flask(__name__)   __init__.py 에서 선언한것을 사용
 
# @app.route("/")
# def index():
#     return "Hello world!"    views 로 옮긴다.

# @app.route("/about")
# def about():
#     return "<h1>h1</h1>"


if __name__ == "__main__" :
    app.run(debug=True)  