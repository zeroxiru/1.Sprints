from flask import Flask,render_template

app = Flask(__name__)


@app.route('/greet/<name>/<age>')
def greet(name, age):
    print( f"alice is {age}")
    return render_template('index.html', title="Greeting", user=name, age=age)


if __name__ == '__main__':
    app.run(debug=True)