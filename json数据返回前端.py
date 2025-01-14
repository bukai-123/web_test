from flask import Flask,json,make_response
app = Flask(__name__)
@app.route("/index")
def index():
    data1=["窝嫩叠",25,"高手"]
    data2= {"name":"高手"}
    return make_response(data2)
if __name__ == "__main__":
    app.run()