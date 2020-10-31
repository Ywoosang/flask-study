#어플리케이션 팩토리
from flask import Flask


#create_app 이라는 함수를 추가하여, Flask 클래스의 인스턴스(app) 을 생성
#app 변수가 함수에서만 사용되는 변수로 변경되었기 때문에 helloFlask 함수도 create_app 함수에 포함되어야함.
#여기서 사용된 create_app함수가 바로 플라스크의 어플리케이션 팩토리임

def create_app():
    app = Flask(__name__)
    from views import main_views #view 폴더 안에 있는 main_views 파일을 import 한다.

#helloFlask 함수는 URL 주소 / 에 매핑되는 함수
#이런 라우트 함수(@app.route 로 매핑되는 함수) 들은 기능이 필요할 때마다 계속 추가되어야 하므로
#create_app 함수 내에 이러한 함수들을 계속 추가하면 불편

#블루프린트(Blueprinnt) 를 이용하면 라우트 함수들을 구조적으로 관리 가능
    app.register_blueprint(main_views.bp)
    return app  


create_app().run() 