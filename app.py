from flask import Flask , render_template ,request ,redirect

app = Flask(__name__)

app.debug = True

@app.route('/', methods=['GET'])
def index():
  # return "Hello World"
  return render_template("index.html", data="KIM")

if __name__ == '__main__':
  app.run()