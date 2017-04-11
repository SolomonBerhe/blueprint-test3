from flask import render_template
from . import customer
#from app import db
#from app.customer.forms import CustomerForm
#from app.customer.models import Customer 



@customer.route('/cust') #methods=['GET', 'POST'])
def cust():
	return "Hello, World!"

	
	"""form = CustomerForm()

	if request.method == "POST":
		if form.validate() == False:
			return render_template("customer.html", form=form)
		else:
			#newcustomer = Customer(form.firstname.data, form.lastname.data, form.gender.data)
			
			newcustomer = Customer()

			newcustomer.firstname = form.firstname.data
			newcustomer.lastname = form.lastname.data
			newcustomer.gender = form.gender.data
			
			db.session.add(newcustomer)
			db.session.commit()
			

			return render_template("viewcustomer.html",customer=newcustomer) 
	else:
		return render_template("customer.html", form=form)"""
