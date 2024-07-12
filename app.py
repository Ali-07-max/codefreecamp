from flask import Flask, render_template

app = Flask(__name__, template_folder='templets')


@app.route("/")
def hello_world():
  return render_template('Home.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
