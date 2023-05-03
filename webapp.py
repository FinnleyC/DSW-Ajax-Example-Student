from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask import render_template

app = Flask(__name__)

app.debug = True #Change this to False for production

@app.route('/t', methods=['POST'])
def t():
    print(request)
    return Markup('<h2>New div1</h2> <p>This is the new content, from the server</p>')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
