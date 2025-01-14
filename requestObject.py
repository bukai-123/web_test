#request包含前端发送过来的所有请求数据，如刚才执行网址的从前端输入的账号和密码，会发送到后端
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/index",methods=['GET','POST'])#这里说明http方法可以是get也可以是post
def index():
    if request.method == 'GET':#http方法隶属于method里面，所以request.method
        return render_template("index.html")
    if request.method == 'POST':
        name = request.form.get("name")
        password = request.form.get("password")#需要通过request来联动到表单form，再加上get以获取html里面的form表单内部的东西（name、passpord等）
        print(name,password)
        return 'this is post'
if __name__ == '__main__':
    app.run()