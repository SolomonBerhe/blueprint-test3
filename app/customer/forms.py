from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

class CustomerForm(Form):
	firstname = StringField('First Name', validators=[DataRequired()])
	lastname = StringField('lastname', validators=[DataRequired()])
	gender = StringField('gender', validators=[DataRequired()])

class AddressForm(Form):
	address1 = StringField('Address1', validators=[DataRequired()])
	address2 = StringField('Address2')
	city = StringField('City', validators=[DataRequired()]) 
	state = StringField('State', validators=[DataRequired()])
	zipcode = StringField('Zip Code', validators=[DataRequired()])
	custid = HiddenField('custid')