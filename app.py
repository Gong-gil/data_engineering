from flask import Flask , render_template ,request ,redirect, send_file
import matplotlib.pyplot as plt
# 새로운 가상환경이면 다시 matplotlib를 깔아줘야한다.
import numpy as np
from io import BytesIO, StringIO
# 그래프를 이미지로 저장하기 위해 필요한 라이브러리

app = Flask(__name__)

app.debug = True

@app.route('/', methods=['GET'])
def index():
  # return "Hello World"
  return render_template("index.html", data="KIM")

@app.route('/fig/<int:mean>_<int:var>')    
# DB연결 X / 인자값을 받아서 바로 그래프를 구성하는 법
def fig(mean, var):

    plt.figure(figsize=(4,3)) # 뭐.... 그래.. 나오는 그래프 사이즈를 정해준단다...
    xs = np.random.normal(mean, var, 100)
    ys = np.random.normal(mean, var, 100)

    plt.scatter(xs, ys, s=100, marker='h', color='red', alpha=0.3) #산점도로 표시하겠다.
    
    img = BytesIO()  # 산점도를 여기에 저장하겠다
    plt.savefig(img, format='png', dpi=200) #imp를 png파일로 저장
    img.seek(0)
    print(xs)

    return send_file(img, mimetype='image/png')

@app.route('/normal/<m_v>')
def normal(m_v):
    m, v = m_v.split('_')   # _ 기준으로 m과 v를 나눠준다.
    m, v = int(m), int(v)
    return render_template('random.html', mean = m, var = v, width=200, height=200)



if __name__ == '__main__':
  app.run()