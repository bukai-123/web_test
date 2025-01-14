from flask import Flask, render_template, request, abort
app = Flask(__name__)
@app.route("/index2",methods=['GET','POST'])#这里说明http方法可以是get也可以是post
def index2():
    people={"name":"张真",
            "age":24,
            'list1':[10,20,30,40,50]}#将people定义为一个字典
    return render_template("index2.html",data=people)##html联动渲染方式，将people传给index2.html模板的data
if __name__ == '__main__':
    app.run()