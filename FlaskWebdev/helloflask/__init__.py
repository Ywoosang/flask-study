from flask import Flask,request
from datetime import datetime, date

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
