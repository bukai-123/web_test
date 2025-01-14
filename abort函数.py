from flask import Flask,abort, request,render_template
app = Flask(__name__)
@app.route("/index",methods=['GET','POST'])
def index():
    if request.method == 'GET':#http方法隶属于method里面，所以request.method
        return render_template("index.html")
    if request.method == 'POST':
        name = request.form.get("name")
        password = request.form.get("password")#需要通过request来联动到表单form，再加上get以获取html里面的form表单内部的东西（name、passpord等）
        if name == "reimu" and password == "12345":
            return "login success, u so strong"
        else:
            return abort(403)
if __name__ == "__main__":
    app.run()