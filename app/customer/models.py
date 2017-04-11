from app import db

class Customer1(db.Model):
	custid = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(50))
	lastname = db.Column(db.String(50))
	marital = db.Column(db.String(50))
	gender = db.Column(db.String(20))
	addresses = db.relationship('Address', backref='customer1', lazy='dynamic')

class Address(db.Model):
	addressid = db.Column(db.Integer, primary_key=True)
	address1 = db.Column(db.String(150))
	address2 = db.Column(db.String(150))
	city = db.Column(db.String(50))
	state = db.Column(db.String(50))
	zipcode = db.Column(db.String(20))
	custid = db.Column(db.Integer, db.ForeignKey('customer1.custid'))