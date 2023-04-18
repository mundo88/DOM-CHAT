from flask import Blueprint,render_template


home =  Blueprint('home', __name__,    
    template_folder="templates",
    static_folder='static',
    static_url_path='/home/static')

@home.route('/',methods=['POST','GET'])
def homeView():
    return render_template('home.html')