from flask import Flask, render_template, request, abort,redirect, make_response
app = Flask(__name__)
@app.route("/index3",methods=['GET','POST'])#这里说明http方法可以是get也可以是post
def index3():
    if request.method == 'GET':#http方法隶属于method里面，所以request.method
        return render_template("index3.html")
    if request.method == 'POST':
        password = request.form.get("password")#需要通过request来联动到表单form，再加上get以获取html里面的form表单内部的东西（name、passpord等）
        if password == "123456":
            print('welcome to the wide world of web!')


            return "login success, u so strong"
        else:
            return "密码错误"
            # return abort(404)

if __name__ == '__main__':
    app.run()