from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<roomID>/poll')
def poll(roomID):
    return 'poll in room number %s' % roomID

@app.route('/<roomID>/poll/<pollID>')
def pollID(roomID, pollID):
    return 'poll in room number %s and poll number %s' % (roomID, pollID)

@app.route('/<roomID>/question')
def question(roomID):
    return 'question in room number %s' % roomID

@app.route('/<roomID>/poll/<pollID>/answer')
def answer(roomID, pollID):
    return 'answer to poll number %s in room number %s' % (pollID, roomID)

@app.route('/register')
def register():
    return 'register'

@app.route('/receive_text', methods=['POST'])
def receive_text():
    print(request.values)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
