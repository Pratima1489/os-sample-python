from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "My first OpenShift Hello World application!"

if __name__ == "__main__":
    application.run()
