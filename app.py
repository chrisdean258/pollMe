from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<roomID>/poll')
def poll():
    return 'poll in room number %d' % roomID

@app.route('/<roomID>/poll/<pollID>')
def pollID():
    return 'poll in room number %d and poll number %d' % (roomID, pollID)

@app.route('/<roomID>/question')
def question():
    return 'question in room number %d' % roomID

@app.route('/<roomID>/poll/<pollID>/answer')
def answer():
    return 'answer to poll number %d in room number %d' % (pollID, roomID)

@app.route('/register')
def register():
    return 'register'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
