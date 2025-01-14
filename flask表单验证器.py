from flask import Flask, render_template, request, abort,redirect, make_response
from wtforms import StringField, SubmitField, PasswordField  #类型
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo  #验证数据不能为空，验证数据是否相同

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kjafls'#后面这个字符串随便输，没有这句就会报错

#定义flask表单模型类,这个类的内容就相当于在html的form表单里的内容
class Register(FlaskForm):
    user_name = StringField(label='用户名', validators=[DataRequired('用户名不能为空')])
    user_password1 = PasswordField(label='密码', validators=[DataRequired('密码不能为空')])
    user_password2 = PasswordField(label='再次输入密码', validators=[DataRequired('密码不能为空'),EqualTo('PASSWORD')])
    submit = SubmitField(label='提交')

@app.route("/register",methods=['GET','POST'])
def register():
    form123 = Register()
    if request.method == 'GET':
        return render_template('register.html',data=form123)
    if request.method == 'POST':
        if form123.validate_on_submit():#从子类实例化出的对象form123中使用validate_on_submit验证器
            #validate_on_submit验证器会验证表单传过来的数据是否正确，而刚才继承的子类中唯一可能发生错误的地方就是EqualTo('PASSWORD')，如果未出错（密码1与2相同），则能够执行这个if
            username = form123.user_name.data
            userpassword1 = form123.user_password1.data
            userpassword2 = form123.user_password2.data
            print(username)
            print(userpassword1)
            print(userpassword2)
        else:
            print('两次密码不一致')
        return render_template('register.html',data=form123)
if __name__ == '__main__':
    app.run()