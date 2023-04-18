from flask import Blueprint,render_template
from flask_login import login_required,current_user

home =  Blueprint('home', __name__,    
    template_folder="templates",
    static_folder='static',
    static_url_path='/home/static')

@home.route('/',methods=['POST','GET'])
@login_required
def homeView():
    print(current_user)
    return render_template('home.html')