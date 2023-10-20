from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    user_name = request.args.get('name', 'Alice')
    return render_template('index.html', title='Home', name=user_name, time=str(datetime.now()))

@app.route('/form')
def form():
    return render_template('form.html')




# @app.route('/name')
# def name():
#     name = request.args.get('name')
#     return index.format(name)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)