from flask import Blueprint 

Customer = Blueprint('customer', __name__, 
					template_folder='templates', 
					static_folder='static')

from . import views					
