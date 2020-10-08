from flask import Flask,request,render_template


app = Flask(__name__) 
 
class Storage:
    def __init__(self):
        self.storage=[]
    def add_item(self,item): 
        if item not in self.storage:
            self.storage.append(item)
            print('아이템 %s 이 추가되었습니다.' % item)
        else :
            print('이미 있는 아이템 입니다.')
    def del_item(self,item):
        if item in self.storage:
            self.storage.remove(item)
        else :
            print("없는 아이템은 삭제할 수 없습니다.")
    
    def reset_storage(self):
        print("저장소의 아이템을 모두 삭제합니다")
        self.storage = []
    
    def get_storage(self):
        return self.storage 

storage = Storage() 

    
@app.route('/')
def show_main():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def show_result():
    if request.method == "POST" :
        try : 
            item1 = request.form['test1'] 
            item2 = request.form['test2'] 
            item3 = request.form['test3'] 
            storage.add_item(item1)
            storage.add_item(item2) 
            storage.add_item(item3) 
            print(storage.get_storage())
        except:
            pass 


    return render_template("result.html", L=storage.get_storage())

@app.route('/reset', methods=['POST'])
def reset_result():
    if request.method == "POST" :
        storage.reset_storage()
        print(storage.get_storage())
        return render_template("result.html") 


if __name__ == '__main__':
    app.run()
    


    
    
    