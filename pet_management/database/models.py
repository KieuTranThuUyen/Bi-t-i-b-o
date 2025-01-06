from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100))
    age = db.Column(db.Integer)
    owner_name = db.Column(db.String(100))
    
    def __repr__(self):
        return f"<Pet {self.name}>"

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'), nullable=False)
    date = db.Column(db.String(100))
    time = db.Column(db.String(100))
    
    pet = db.relationship('Pet', backref=db.backref('bookings', lazy=True))
    
    def __repr__(self):
        return f"<Booking {self.id}>"

class Schedule(db.Model):
    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100))
    time = db.Column(db.String(100))
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'), nullable=False)
    
    pet = db.relationship('Pet', backref=db.backref('schedule', lazy=True))
    
    def __repr__(self):
        return f"<Schedule {self.date} {self.time}>"
