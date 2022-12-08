from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    # return "hello drinks"
    return {"drinks": "drink data"}

if __name__ == "__main__":
  app.run()