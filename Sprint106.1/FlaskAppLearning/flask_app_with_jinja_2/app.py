from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/update_country', methods=['GET', 'POST'])
def update_country():
    if request.method == 'POST':

        #Get the username and the  new country from the form
        name = request.form.get('name')
        new_country = request.form.get('country')

        # update the  user's country in the dictionary
        if name in users:
            users[name]['country'] = new_country

        return redirect(url_for('all-users'))
        # Get the updated country from the form
        update_country = request.form['country']

        # # Update the 'country' attribute while keeping the rest unchanged
        # users['country'] = update_country
        #
        # #Return a response, render a template, or redirect as needed
        # return f'Updated country to: {update_country}'

        #render_template('.html', users)
    return render_template('update_users.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)