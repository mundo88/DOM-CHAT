from flask import Blueprint,render_template
from flask_login import login_required,current_user

chat =  Blueprint('chat', __name__,    
    template_folder="templates",
    static_folder='static',
    static_url_path='/chat/static')

@chat.route('/',methods=['POST','GET'])
@login_required
def chatView():
    print(current_user)
    return render_template('chatView.html')