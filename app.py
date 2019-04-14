from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Today is : {0}<h1/>".format(datetime.datetime.now())

if __name__ == "__main__":
    app.run()
