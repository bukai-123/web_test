from flask import Flask, render_template, request, redirect
#render_template是一个用于渲染的模板
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/index/<user>")#输入网址加/index/（你自定义的用户名）
def index(user):
    return render_template("index.html",name=user)

if __name__ == '__main__':
    app.run()