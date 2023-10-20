from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return """<html><body>
        <h1>Hello there, It's Afternoon now  """ + str(datetime.now())+"""</h1>
        </body></html>"""




if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", port=5000, debug=True)