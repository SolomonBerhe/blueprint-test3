from flask import render_template, request, redirect, url_for
from . import Customer
from app import db
from app.customer.forms import CustomerForm, AddressForm
from app.customer.models import Customer1, Address 



@Customer.route('/cust', methods=['GET', 'POST'])
def cust():
	#return "Hello, World!"

	
	form = CustomerForm()

	if request.method == "POST":
		if form.validate() == False:
			return render_template("customer.html", form=form)
		else:
			
			newcustomer = Customer1()

			newcustomer.firstname = form.firstname.data
			newcustomer.lastname = form.lastname.data
			newcustomer.gender = form.gender.data
			
			db.session.add(newcustomer)
			db.session.commit()
			

			return render_template("viewcustomer.html",customer=newcustomer) 
	else:
		return render_template("customer.html", form=form)

@Customer.route('/viewcustomer/<custid>')
def viewcustomer(custid):
	customer = Customer1.query.filter_by(custid = custid).first()
	custAddresses = Address.query.filter_by(custid = custid)
	return render_template("viewcustomer.html", customer = customer, addresses=custAddresses)

@Customer.route('/editcustomer/<custid>', methods=['GET', 'POST'])
def editcustomer(custid):
	customer = Customer1.query.filter_by(custid=custid).first()

	form = CustomerForm()

	if form.validate_on_submit():
		customer.firstname = form.firstname.data
		customer.lastname = form.lastname.data
		customer.gender = form.gender.data
		
		db.session.add(customer)
		db.session.commit()
		return render_template("viewcustomer.html", customer=customer)
	else:
		form.firstname.data = customer.firstname
		form.lastname.data = customer.lastname
		form.gender.data = customer.gender
		return render_template('editcustomer.html', form=form)

@Customer.route('/address/<custid>', methods=['GET', 'POST'])
def address(custid):
	form = AddressForm()
	form.custid.data = custid
	if request.method == 'POST':
		if form.validate() == False:
			return render_template('address.html', form=form)
		else:
			newaddress = Address()
			newaddress.address1 = form.address1.data
			newaddress.address2 = form.address2.data
			newaddress.city = form.city.data
			newaddress.state = form.state.data
			newaddress.zipcode = form.zipcode.data
			newaddress.custid = form.custid.data 
			db.session.add(newaddress)
			db.session.commit()
			return redirect(url_for('.viewcustomer', custid = form.custid.data ))
	else:
		return render_template('address.html', form=form)

@Customer.route('/editaddress/<addressid>', methods=['GET', 'POST'])
def editaddress(addressid):
	address = Address.query.filter_by(addressid=addressid).first()
	form = AddressForm()
	if form.validate_on_submit():
		address.address1 = form.address1.data
		address.address2 = form.address2.data
		address.city = form.city.data
		address.state = form.state.data
		address.zipcode = form.zipcode.data
		db.session.add(address)
		db.session.commit()
		return render_template('viewaddress.html', address=address)
	else:
		form.address1.data = address.address1
		form.address2.data = address.address2
		form.city.data = address.city
		form.state.data = address.state
		form.zipcode.data = address.zipcode
		return render_template('editaddress.html', form=form)



