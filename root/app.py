from flask import Flask, render_template

app = Flask(__name__)

from root.database import Database

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/user')
def users():
    all_users = Database.fetchAllUsers()
    return render_template('user.html', all_users = all_users)


@app.route('/messages')
def messeges():
    # all_messeges = Database.fetchAllMesseges()
    return render_template('message.html')



if __name__ == '__main__':
    app.run(debug=True)