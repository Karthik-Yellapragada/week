import flask
import pymongo
from flask import request
from flask import render_template

app = flask.Flask(__name__)

mongodb_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongodb_client["Form"]
users = db["user_info"]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])   
def login():
    if request.method == 'POST':
        p = request.form['password']
        e = request.form['email']
        query = db.users.find_one({'email': e})
        query2 = db.users.find_one({'password': p, 'email': e})
        if query and query2:
            return 'succesfully logged in'
        elif query:
            return 'incorrect password'

        else:
            return render_template('alert.html')
    pass
    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        a = request.form['name']
        b = request.form['password']
        c = request.form['email']
        d = request.form['c_p']
        query1 = db.users.find_one({'email': c})
        if query1:
            return 'Email already exist!'
        else:
            db.users.insert_one({'name': a, 'email': c, 'password': b, 'confirm_password': d})
        return render_template("after_reges.html")
        pass
    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
