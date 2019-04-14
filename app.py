from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    html ="<html><head><title>Dashboard Test</title><meta charset='utf-8'>"
    html+="<style> font-family:arial,sans;</style></head>"
    html+= "<h1>Today is : {0}<h1/>".format(datetime.datetime.now())
    return html

if __name__ == "__main__":
    app.run()
