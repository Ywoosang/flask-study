from app import app 
from flask import render_template,request,redirect,jsonify,make_response

from  datetime import datetime

@app.template_filter("clean_date")  #새로운 필터를 템플릿 앱에 더한다. 
def clean_date(dt):
    return dt.strftime("%d %b %Y ") #어떤 템플릿에서나 사용할 수 있음. 


@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():
    my_name = "Jinja"

    age = 30
    langs = ["Python", "JavaScript","Bash","C","Ruby"]

    friends = {
        "Tom" : 30,
        "Amy" : 60,
        "Tony" :56 
    }
    colours = ("Red","Green")

 
    cool = True
    class GitRemote:
        def __init__(self,name,description,url):
            self.name = name
            self.description = description
            self.url = url
        def pull(self):
            return f"Pullin repo  {self.name}"
        def clone(self):
            return f"Cloning into {self.url}"
        
    def repeat(x,qty):
        return x * qty

    my_remote = GitRemote(
        name="flask Jinja",
        description = "Template design tutorial",
        url = "https://github.com"
    )

    date = datetime.utcnow()  
    makeAlert ="<script>alert('진자템플릿을 이용중입니다')</script>"
    sample_html = "<h1>HTML 이 왔습니다</h1>"


    return render_template("public/jinja.html", 
    my_name = my_name,
    age=age,
    langs= langs,
    friends= friends,
    colours = colours,
    cool= cool,
    GritRemote = GitRemote,  #클래스를 통째로 전송
    repeat = repeat,
    my_remote = my_remote,
    date = date,  #넘겨줌 
    makeAlert = makeAlert,
    sample_html = sample_html
    )
    
    
    
@app.route("/about")
def about():
    return render_template("public/about.html") 



@app.route("/json",methods=["POST"])
def json():
    if request.is_json:   #온 request 가 json 이라면 
        req = request.get_json() #json 을 딕셔너리로 받아온다
        
        response = {
            "message" : "JSON recieved",
            "name" : req.get("name")
        }
        res = make_response(jsonify(response),200) #str,list,dict 를 json 으로 바꿔준다.

        return res

    else : 
        res = make_response(jsonify({"message":"No JSON recieved"}))
        return "NO JSON ",404

    

@app.route('/guestbook')
def guestbook():
    return render_template("public/guestbook.html")


@app.route("/guestbook/create-entry",methods=["POST"])
def create_entry():

    req = request.get_json()   #get_json 을 이용해 딕셔너리로 바꿈 

    print(req)

    res = make_response(jsonify({"message": "JSON recieved"}),200) #클라이언트로 전송

    return res


