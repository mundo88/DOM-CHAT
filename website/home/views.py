from flask import Blueprint,redirect
from flask_login import login_required,current_user

home =  Blueprint('home', __name__,    
    template_folder="templates",
    static_folder='static',
    static_url_path='/home/static')

@home.route('/',methods=['POST','GET'])
@login_required
def homeView():
    print(current_user)
    return redirect("/dashboard")