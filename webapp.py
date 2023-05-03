from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask import render_template

app = Flask(__name__)

app.debug = True #Change this to False for production

@app.route('/t')
def t():
    return Markup('This is the new content, from the server')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
