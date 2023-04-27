from flask import Blueprint,render_template
from flask_login import login_required

notify =  Blueprint('notify', __name__,    
    template_folder="templates",
    static_folder='static',
    static_url_path='/notify/static')

@notify.route('/',methods=['POST','GET'])
@login_required
def notifyView():
    return render_template('notifyView.html')