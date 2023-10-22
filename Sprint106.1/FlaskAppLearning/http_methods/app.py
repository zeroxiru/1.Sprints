from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    return f'Profile page of {username}'

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest') # Use 'Guest' as default value if no 'name' parameter is provided
    return f'Hello, {name}'

@app.route('/update_profile', methods=[ 'GET','POST'])
def update_profile():
    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        return f'Updating the profile of {username} with email{email}'
    return render_template('index.html')

 


if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)