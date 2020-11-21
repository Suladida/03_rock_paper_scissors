from flask import Flask
from app import app

app = Flask(__name__)

from controller import controller

if __name__ == '__main__':
    app.run(debug=True)