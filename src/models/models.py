from src.models.init_db import db
import calendar

class Birthday(db.Model):
    __tablename__ = 'bdays'

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String)
    bday_day = db.Column(db.Integer)
    bday_month = db.Column(db.Integer)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'birthday': str(self.bday_day) + ' ' + str(calendar.month_name[self.bday_month])
        }