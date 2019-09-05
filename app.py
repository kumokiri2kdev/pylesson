from flask import Flask, render_template

app = Flask(__name__)


lessons = [
    {
        'question': 'a',
        'answer': 'b'
    }


]

@app.route('/')
def index():
    return render_template('index.html', title='Python Lesson', lesson = lessons[0])


if __name__ == '__main__':
    app.run()
