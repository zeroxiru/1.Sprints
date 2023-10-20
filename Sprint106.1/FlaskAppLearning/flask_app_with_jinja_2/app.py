from flask import Flask, render_template, request

app = Flask(__name__)

users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
}

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/all-users')
def all_ausers():
    return render_template('all_users_with_tab.html', users=users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)