from flask import Flask,request,Response,make_response,session
from datetime import datetime, date, timedelta

app = Flask(__name__)

debug = True 

@app.route("/")
def helloflask():
    return "main_page"

@app.route("/rp")
def rp():
    # q 가 Multu Dict 형태기 때문에 str 로 형변환 한것. response 를 str로 내보내기 위해 
    q = request.args.get("q")
    print(type(q))
    # http://localhost:5000/rp?q=123 입력해주면 q=123 찍힘 
    return "q= %s" % q 

@app.route('/sd',subdomain="g")
def helloworld():
    return "Hello G.local.com"



def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str,fmt)
    return trans


#request parameter custom function Type 
#type = 타입을 바꿀 함수 
@app.route('/dt')
def dt():
    datestr = request.values.get('date',date.today(),type=ymd('%Y-%m-%d'))
    return "우리나라 시간 형식:" +str(datestr)+'\n'+'바뀌귀 전 : %s' % str(date.today())

# http:localhost:5000 까지만 적혀있음  => / 해주고 시작해야함. 
@app.route('/reqenv')
def reqenv():
    print(request.environ['SERVER_PORT'])
    return ('REQUEST_METHOD: %(REQUEST_METHOD) s'  'PATH_INFO: %(PATH_INFO) s') % request.environ





app.secret_key = "1223445"
app.config.update(
    SECREAT_KEY='12344',
    SESSION_COOKIE_NAME= "test_cookie",
    PERMANENT_SESSION_LIFETIME= timedelta(30) 
)
@app.route('/wc')
def makecookie():
    # 실무에 가면 request wrapper 만들어서 사용 (함수 )
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("CookieTest")
    res.set_cookie(str(key),str(val))
    #import 만 했을 뿐인데 session 은 실제로 인스턴스 이다. session 설정
    session['Token'] = '123X'
    return make_response(res)


@app.route('/rc')
def getcookie():
    key=request.args.get('key') #token 
    cookieValue = request.cookies.get(key) 
    return cookieValue + session.get("Token")


@app.route('/delsess')
def delsess():
    #시간이 지나면 없어지게 설정되어있으면 Error남 이를 막기 위해서. 
    if session.get("Token"):
        del session['Token']
    return "Session이 삭제되었습니다. ! "