from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'from library', 200

if __name__ == '__main__':
    app.run()
