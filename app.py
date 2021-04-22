from flask import Flask , render_template ,request ,redirect

app = Flask(__name__)

app.debug = True

if __name__ == '__main__':
  app.run()