from flask import Flask, render_template, request
import json
import os
import random

app = Flask(__name__)


lesson_list = []

def load_data(lesson_id):
    jfile = open('data/'+ lesson_id + '.json', 'r')
    jdata = json.load(jfile)

    return jdata

def get_data():
    global lesson_list

    if len(lesson_list) < 1:
        lesson_list = [i for i in os.listdir('data') if i.endswith('.json')]

    lesson_file = random.choice(lesson_list)
    lesson_id = lesson_file.rstrip('.json')

    jdata = load_data(lesson_id)

    lesson_list.remove(lesson_file)

    jdata['id'] = lesson_id
    return jdata


@app.route('/')
def index():
    lesson_id = request.args.get('lesson_id')

    if lesson_id:
        lesson_data = load_data(lesson_id)
    else:
        lesson_data = get_data()

    return render_template('index.html', title='Python Lesson', lesson = lesson_data)


if __name__ == '__main__':
    app.run()
