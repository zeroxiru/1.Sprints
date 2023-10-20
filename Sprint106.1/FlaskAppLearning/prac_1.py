from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


HELLO_HTML = """
   <html> 
   <body>
   <h1> Hello, {0}! </h1>
   The time is {1}
   </body>
   </html>
"""

@app.route('/')
def hello():
    name = request.args.get('name')
    if name:
        return HELLO_HTML.format(name, str(datetime.now()))
    else:
        return "Please provide the name parameter in the URL"

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
