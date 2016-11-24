from flask import Flask, render_template, request, url_for

app = Flask(__name__)
app.config.from_object('config')


def do_the_login():
    return "You made a post request"


@app.route('/')
def home():
    return render_template('form_submit.html')

@app.route('/post', methods=['POST'])
def post_post():
    return "You Made A Post Request"
