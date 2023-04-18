from flask import Blueprint,render_template,redirect,request,url_for
from flask_login import login_user,logout_user
from ..models import User
from ..app import db
auth =  Blueprint('auth', __name__,    
    template_folder="templates",
    static_folder='static',
    static_url_path='/auth/static')

@auth.route('/sign-in',methods=['POST','GET'])
def signinView():
    if request.method == 'POST' :
        data = request.form
        email = data.get('email')
        password = data.get('password')
        remember = data.get('remember')
        user = User.query.filter_by(email=email).first()
        if user.password==password:
            login_user(user,remember=remember)
            return redirect(url_for("home.homeView"))
    return render_template('signin.html')

@auth.route('/sign-up',methods=['POST','GET'])
def signupView():
    return render_template('signup.html')

@auth.route('/logout',methods=['POST','GET'])
def logout():
    logout_user()
    return  redirect(url_for("home.homeView"))