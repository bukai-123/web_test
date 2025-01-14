from flask import Flask, render_template, request, abort,redirect, make_response
from wtforms import StringField, SubmitField, PasswordField  #类型
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo  #验证数据不能为空，验证数据是否相同

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kjafls'#后面这个字符串随便输，没有这句就会报错

#定义flask表单模型类,这个类的内容就相当于在html的form表单里的内容
class Register(FlaskForm):  #从导入的FlaskForm类做继承，得到子类Register
    user_name = StringField(label='用户名', validators=[DataRequired('用户名不能为空')])
    user_password1 = PasswordField(label='密码', validators=[DataRequired('密码不能为空')])#验证数据不能为空
    user_password2 = PasswordField(label='再次输入密码', validators=[DataRequired('密码不能为空'),EqualTo('PASSWORD')])#验证数据不能为空，验证数据是否相同
    submit = SubmitField(label='提交')

@app.route("/register",methods=['GET','POST'])#这里说明http方法可以是get也可以是post，不写methon的话就默认只有get
def register():
    form123 = Register()   #刚将才继承的类实例化为对象form123。
    if request.method == 'GET':#http方法隶属于method里面，所以request.method
        return render_template('register.html',data=form123)
    if request.method == 'POST':
        username = form123.user_name.data #flask表单的输入数据获取方法，注意与之前的form表单数据获取方法作区分
        userpassword1 = form123.user_password1.data #flask表单的输入数据获取方法，注意与之前的form表单数据获取方法作区分
        userpassword2 = form123.user_password2.data #flask表单的输入数据获取方法，注意与之前的form表单数据获取方法作区分
        print(username)
        print(userpassword1)
        print(userpassword2)
        return render_template('register.html',data=form123)
if __name__ == '__main__':
    app.run()