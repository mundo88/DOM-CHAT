from flask import Blueprint,render_template

auth =  Blueprint('auth', __name__,    
    template_folder="templates",
    static_folder='static',
    static_url_path='/auth/static')

@auth.route('/sign-in',methods=['POST','GET'])
def signinView():
    return render_template('signin.html')