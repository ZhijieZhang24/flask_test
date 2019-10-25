from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/zhijie')
def zhijie():
    return "hello Zhijie!"

if __name__ == '_main_':
    app.run(debug=True)
