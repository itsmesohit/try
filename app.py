from flask import Flask, render_template, request
app = Flask(__name__)
from model import *

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/', methods = ['POST'])
def sumit():
   passage  = None
   question = None
   answer = None
   if request.method == 'POST':
      passage = request.form['unseen_passage']
      question = request.form['ques_input']
      passage = request.form['unseen_passage']
      answer = solve(question , passage)

   return render_template('index.html',  passage = passage , question = question,  answer = answer['answer']  )

if __name__ == '__main__':
   app.run(debug=True, port=8000)

