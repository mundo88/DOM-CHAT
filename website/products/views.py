from flask import Blueprint,render_template
from flask_login import login_required

products =  Blueprint('products', __name__,    
    template_folder="templates",
    static_folder='static',
    static_url_path='/products/static')

@products.route('/',methods=['POST','GET'])
@login_required
def productsView():
    return render_template('productView.html')