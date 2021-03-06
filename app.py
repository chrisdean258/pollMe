from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from python.questionInsert import askQuestion
from python.questionInsert import getQuestionsRoom
from python.pollInsert import answerPoll
from python.pollInsert import getAnswersRoom
from python.roomInsert import createRoom
from python.roomInsert import getQuestion
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/questions/<roomID>')
def get_questions(roomID):
    questions = [q[5] for q in getQuestionsRoom(roomID)]
    return json.dumps(questions)

@app.route('/answers/<roomID>')
def get_answers(roomID):
    questions = getAnswersRoom(roomID)
    print(str(questions))
    return json.dumps(questions)

@app.route('/room/<roomID>')
def room(roomID):
    return render_template("room.html", roomID=roomID)

@app.route('/<roomID>/poll')
def poll(roomID):
    try:
        q = json.loads(getQuestion(roomID)[0][0])

        print(q)
        return render_template("poll.html",
                a = q["answerA"],
                b = q["answerB"],
                c = q["answerC"],
                d = q["answerD"],
                question = q["pollquestion"]
        )
    except:
        return render_template("poll.html", a = "", b = "", c = "", d = "", question = "")

@app.route('/<roomID>/poll/<pollID>')
def pollID(roomID, pollID):
    return 'poll in room number %s and poll number %s' % (roomID, pollID)

@app.route('/<roomID>/question')
def question(roomID):
    return render_template("question.html", roomID=roomID)

@app.route('/<roomID>/poll/<pollID>/answer')
def answer(roomID, pollID):
    return 'answer to poll number %s in room number %s' % (pollID, roomID)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method== 'POST':
        return 'hey good job you tried to log in'
    else:
        return render_template("register.html")

@app.route('/receive_text', methods=['POST'])
def receive_text():
    phoneNum = request.form['From']
    msg = request.form['Body']
    if len(msg) == 9:
        answerPoll(phoneNum[2:], msg[1:7], '123456', msg[8])
    else:
        askQuestion(phoneNum[2:], msg[1:7], msg[8:])
    return ('', 204)

@app.route('/<filename>')
def static_(filename):
    return app.send_static_file(filename)

@app.route('/addpoll', methods=['POST', 'GET'])
def addpoll():
    if request.method == 'POST':
        id_ = createRoom(json.dumps(request.form))
        return redirect(url_for("poll", roomID=id_))
    else:
        return render_template("addpoll.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
