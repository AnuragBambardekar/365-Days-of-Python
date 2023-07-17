from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '200 OK'

if __name__ == '__main__':
    app.run()
