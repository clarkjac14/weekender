from app import db

class TimeSlot(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True)
	friday = db.Column(db.Boolean, unique=False, default=False)
	saturday = db.Column(db.Boolean, unique=False, default=False)
	sunday = db.Column(db.Boolean, unique=False, default=False)
	
	def __repr__(self):
		return '<Name {}>'.format(self.name)