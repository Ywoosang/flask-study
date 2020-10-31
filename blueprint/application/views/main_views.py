from flask import Blueprint


#Blueprint 는 이름, 모듈명, URL 프리픽스 값을 입력으로 객체를 생성
#여기서 사용된 'main' 이라는 이름은 함수명으로 URL을 찾아내는 url_for 함수에서 사용됨

bp = Blueprint('main',__name__,url_prefix='/')
#URL 프리픽스(url_prefix) 는 main_views.py 파일에 있는 함수들의 URL 앞에 항상 붙게 되는 프리픽스 URL


#__init__.py 파일에 있던 helloFlask 함수를 그대로 main_views.py 파일에 옮긴 것.
#단, @app.route가 아닌 @bp.route 로 변경된 점에 주목.


@bp.route('/')
def helloFlask():
    return 'Hello, Flask'


@bp.route('/hello')
def index():
    return 'hello'