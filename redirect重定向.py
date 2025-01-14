from flask import Flask, render_template, request, redirect,url_for
# app = Flask(__name__)
# @app.route("/index")
# def index():
#     return render_template("index.html")
# @app.route("/baidu")
# def baidu():
#     return redirect("https://www.baidu.com")
# if __name__ == "__main__":
#     app.run()

app = Flask(__name__)
@app.route("/index")
def index():
    return redirect(url_for('hello'))#'url_for(某函数)'用于生成 URL,本身是一个网站性质的，所以可以用redirect来重定向
@app.route("/")
def hello():
    return "u so strong"
if __name__ == "__main__":
    app.run()
