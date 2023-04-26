from flask import Blueprint,render_template
from flask_login import login_required,current_user

dashboard =  Blueprint('dashboard', __name__,    
    template_folder="templates",
    static_folder='static',
    static_url_path='/dashboard/static')

@dashboard.route('/dashboard',methods=['POST','GET'])
@login_required
def dashboardView():
    print(current_user)
    return render_template('dashboardView.html')