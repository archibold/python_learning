from flask import Flask
from decoratorz import *

app = Flask(__name__)

@app.route('/')
@make_bold
@make_underline
def hello_world():
    return f'hello_world3'

if __name__ == "__main__":
    app.run(debug=True)
    