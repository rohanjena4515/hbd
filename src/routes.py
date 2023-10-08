from flask import Blueprint, jsonify, request
from src.models.init_db import db
from src.models.models import Birthday
from calendar import monthrange
from datetime import date

route_blueprint = Blueprint('route_blueprint', __name__)

@route_blueprint.route('/')
def api():
     return jsonify({'data': 'API is working'}), 200

@route_blueprint.route('/birthday', methods = ['GET'])
def get_birthdays():
    birthdays = Birthday.query.all()
    print(birthdays)
    return jsonify({'data': [birthday.serialize for birthday in birthdays]}), 200

@route_blueprint.route('/birthday', methods = ['POST'])
def post_birthday():
    data = request.get_json()
    try:
        name, bday_day, bday_month = data['name'], data['bday_day'], data['bday_month']

        num_days = monthrange(date.today().year, bday_month)[1]
        if(bday_day < 1 or bday_day > num_days):
            raise ValueError

        birthday = Birthday(name=name, bday_day=bday_day, bday_month=bday_month)
        db.session.add(birthday)
        db.session.commit()
        return jsonify({'data': 'success'}), 200

    except KeyError:
        return jsonify({'data': 'failure', 'details': 'check request body'}), 400
    except ValueError:
        return jsonify({'data': 'failure', 'details': 'check birthday day and month'}), 400
    except:
        return jsonify({'data': 'failure', 'details': 'something went wrong'}), 400

@route_blueprint.route('/birthday/search', methods=['GET', 'POST'])
def search_birthday():
    try:
        name = request.args.get('name')
        bday_day = request.args.get('bday_day')
        bday_month = request.args.get('bday_month')

        if ((name is None) and (bday_day is None) and (bday_month is None)):
            raise KeyError

        birthdays = Birthday.query

        if bday_month:
            birthdays = birthdays.filter(Birthday.bday_month == bday_month)
        if bday_day:
            birthdays = birthdays.filter(Birthday.bday_day == bday_day)
        if name:
            birthdays = birthdays.filter(Birthday.name.ilike('%' + str(name) + '%')).all()
            print(birthdays)
        return jsonify({'data': [birthday.serialize for birthday in birthdays]}), 200
    except:
        return jsonify({'data': 'failure', 'details': 'check url params'}), 400

