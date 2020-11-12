from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    g,
    abort,
    session,
)

#user 클래스를 만들어 user 객체를 클래스에서 만든 전역변수인 리스트에 append 한다.
#데이터 베이스를 사용하는 대신에 app 에 global 변수를 사용한다. 
class User:
    def __init__(self,id,username,password):
        self.id = id
        self.username = username
        self.password = password
        # 이것에 대한 표현을 반환한다. 커맨드 라인에서 볼 수 있음 
    def __repr__(self):
        # 존재하는 모든 user의 이름을 볼 수 있음 
        return f'<User:{self.username}' 

 
#모든 유저들을 나타내는 전역변수 만듬. User 인스턴스들을 append 함
users = []
users.append(User(id=1,username='우상',password='password1' ))
print(users[0].password) 

app = Flask(__name__)
app.config.update(
    SECRET_KEY ="woosangyoon1234",
    SESSION_COOKIE_NAME="logintest_cookie"
)

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user_list= [x for x in users if x.id == session['user_id']]
        if user_list == [] :
            user = ''
        else :
            user =user_list[0]
        g.user = user
            #어디에서든 g 를 사용할 수 있다 이미 로그인 되어있다면 
            # user 에 접근이 가능할 것이다.  

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST' :
        #user_id 라는 세션 존재하지 않으면 none 
        # 이미 존재하면 pop 
        session.pop('user_id', None) 
        #항상 유저가 로그인 시도할 때마다 session 의 user_id 를 pop (제거) 처음부터 다시 시작 
        # 이미 로그인 되어 있는 한경험이 있는 상태에서 다시 로그인을 시도할 때 , 기존에 있던 세션을 제거하고 새로운 새션을 발급한다.
        # 로그인을 다시 하려고 할때 비밀번호를 잘못 치면 로그아웃되고 기존에 로그인을 하고있더라도 다시 정확한 비밀번호를 입력해야한다. 
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
        #안에 있는 유저와 같은 username, password 가 있는지 확인
        
        userlist = [x for x in users if x.username == username]
        if userlist != []:
            user=userlist[0]
        else:
            user = ''
        # user 가 empty 가 아니고 password 가 입력한 값과 일치하는지 확인
        if user and user.password == password :
            #key : user_id  세션 설정 
            # 여기있는 세션은 cookie 로 내려보내짐. 
            session['user_id'] = user.id
            # 프로필로 리다이렉트. 로그인한 뒤 프로필 페이지로 가야하기 때문
            return redirect(url_for('profile'))
        return redirect(url_for('login'))
    #post 요청이 아닌 get 요청이면 로그인 페이지 처음 들어갔을때 로그인화면 띄우는 요청이므로 render_template로 
    return render_template('login.html')



@app.route('/profile')
def profile():
    if not g.user:
       # abort(403) #로그인 실패해서 세션없어지고 다시 이전페이지로 오면 forbidden error 내기 
        return render_template('login.html')
    return render_template('profile.html')   


app.run(host='0.0.0.0',debug=True)

#유저가 로그인폼에 입력하면 app이 username과 password 가 맞는지 검사하고 
# 맞다면 app 은 session 을 이용해 user 가 로그인했는지, 로그인하지 않았는지 log 를 적고
# 프로필 페이지로 redirect 시킨다.  

