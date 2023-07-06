"""
Replace the pseudocode in the register_user() function with Python code.
https://flask-bcrypt.readthedocs.io/en/1.0.1/#usage
"""

from flask import Flask
from flask_bcrypt import Bcrypt
import json


app = Flask(__name__)
bcrypt = Bcrypt(app)

# This is a helper function, not a Flask route!
def register_user(username, password):
    """
    Return True if the user's login credentials were successfully added
    to the users.json file; return False if not.

    :param username: The raw username submitted via the login form
    :param password: The raw password submitted via the login form
    :return: A Boolean value describing whether the credentials were added to users.json
    """

    try:
        # Encode the username and password using bcrypt
        hashed_username = bcrypt.generate_password_hash(username).decode('utf-8')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = {
            'username': hashed_username,
            'password': hashed_password
        }
        # Create a new dictionary to hold the new user info


        # Open the users.json file and read the contents
        with open("users.json", "r") as fileobj_r:
            users = json.loads(fileobj_r)
        # Add the dictionary of new user info to the contents
        users.append(new_user)
        # Write all the contents back to the users.json file (this will overwrite)

        with  open("users.json", "w") as fileobj_w:
            json.dumps(users, fileobj_w)

        return True

    except Exception as e:
        print(e)
        return False

register_user(username, password=p)

"""
BONUS: Create a Flask route called register_user() for ('/register').
    - A GET request to this route should render register.html.
    - A POST request to this route should call the register_user()
      helper function and render the registration_success.html file if 
      the registration was successful
          - If the registration was not successful, do this:
          return render_template('register.html', error="Could not register user")
          
Remember to add this code to the bottom of your file so you can test out your code locally:
 
if __name__ == '__main__':
    app.run(debug=True)
"""