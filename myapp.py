from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello..............,I am Tamanna Bothra'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
