from flask import Flask, render_template, request, jsonify
application = app = Flask(__name__)
from pymongo import MongoClient
import certifi
db = ''
ca = certifi.where()
# 한정은
client1 = MongoClient(
    'mongodb+srv://sparta:test@cluster0.0qxqx9k.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db1 = client1.dbsparta
# 이남규
client2 = MongoClient(
    'mongodb+srv://sparta:test@cluster0.fsxacay.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db2 = client2.dbsparta
# 정소희
client3 = MongoClient(
    'mongodb+srv://sparta:test@cluster0.p77xisx.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db3 = client3.dbsparta
# 최은지
client4 = MongoClient(
    'mongodb+srv://dkssud6757:test@cluster0.dgpr50w.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db4 = client4.dbsparta


@app.route('/')
def home():
   return render_template('index.html')

# @app.route('/main')
# def home():
#    return render_template('main.html')

@app.route('/eunji')
def eunji():
    global db
    db = db4
    return render_template('eunji.html')


@app.route('/namgyu')
def namgyu():
    global db
    db = db2
    return render_template('namgyu.html')

@app.route('/jeongeun')
def jeongeun():
    global db
    db = db1
    return render_template('jeongeun.html')

@app.route('/sohee')
def sohee():
    global db
    db = db3
    return render_template('sohee.html')


@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    currentDate_receive = request.form['currentDate_give']
    currentTime_receive = request.form['currentTime_give']
    password_receive = request.form['password_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'currentDate': currentDate_receive,
        'currentTime': currentTime_receive,
        'password': password_receive
    }
    db.project.insert_one(doc)
    
    return jsonify({'msg': '기록 완료!'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():

    all_comments = list(db.project.find({},{'_id':False}))
    return jsonify({'result': all_comments})

@app.route('/guestbook', methods=['DELETE'])
def guestbook_delete():
    
    comment_receive = request.form['comment_give']
    db.project.delete_one({'comment': comment_receive})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
   app.run()


   