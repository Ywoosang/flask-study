from flask import Flask,request,render_template,g
import pymysql

app = Flask(__name__)


@app.route('/')
def mainpage():
    return render_template("sign-up.html")


#세션과 쿠키를 사용한다. 

#전역번수 g 객체에 데이터베이스 연결을 저장해둔다. 

@app.before_request
def before_request():
    g.db = pymysql.connect(host='localhost', port=3306, user='root', passwd='bodu3717@@', db='logintest', charset='utf8')
    print("데이터 베이스가 연결되었습니다.")
@app.teardown_request
def teardown_request(exception):
    g.db.close()
    print("데이터 베이스 연결을 종료합니다.")
     
@app.route('/login',methods=["POST"])
def login():
    input_id = request.form.get('Id')
    user_pw = request.form.get('passwd')


@app.route('/signup',methods=["POST"])
def signup():
    cursor = g.db.cursor() 
    name = request.form.get('name')
    user_id = request.form.get('Id')
    user_pw = request.form.get('passwd')
    sql = """SELECT id from user_table"""
    cursor.execute(sql)
    result = cursor.fetchall()
    val = True
    for rawid in result:
        id = str(rawid).strip("')(,'") 
        print(id)
        print(user_id)
        if id == user_id :
            val =False 

    if val : 
        # primary key를 id 로 바꿔야 중복이 안됌.
        sql ="""insert into user_table values('%s','%s','%s');""" % (str(name),str(user_id),str(user_pw))
        cursor.execute(sql)
        sql ="""select * from user_table ;"""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        return  "로그인이 되었습니다."
    else :
        print("이미 존재하는 아이디입니다.")
        return("이미 존재하는 아이디입니다.")

app.run(debug=True)

        




# class User:
#     def __init__(user_id,user_pw):
#         self.id = user_id
#         self.pw = user_pw
#     def login

