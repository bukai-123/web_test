from flask import Flask, render_template, request, abort,redirect, make_response
app = Flask(__name__)
@app.route("/index",methods=['GET','POST'])#这里说明http方法可以是get也可以是post
def index():
    if request.method == 'GET':#http方法隶属于method里面，所以request.method
        return render_template("index.html")
    if request.method == 'POST':
        name = request.form.get("name")
        password = request.form.get("password")#需要通过request来联动到表单form，再加上get以获取html里面的form表单内部的东西（name、passpord等）
        if name == "reimu" and password == "12345":
            return "login success, u so strong"
        else:
            return abort(404)
        # data1="高手"
        # # return make_response(data1)
        # print(name, password)
        # return [name,password,data1]
if __name__ == '__main__':
    app.run()