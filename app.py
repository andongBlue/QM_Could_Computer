#!/usr/bin/env python
import json

import requests
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

import config

# initialization
app = Flask(__name__)
app.config.from_object(config)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'

# extensions
db = SQLAlchemy(app)
auth = HTTPBasicAuth()


class Student(db.Model):
    __tablename__ = 'student_info'
    student_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    nationality = db.Column(db.String(45), nullable=False)

    def __init__(self, student_id, first_name, last_name, phone_number, gender, nationality):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.gender = gender
        self.nationality = nationality

    def __repr__(self):
        return "Student id: " % self.student_id


def check_phone_number(phone_number):
    url = 'http://apilayer.net/api/validate?access_key=097bcb2a36236e682268c1b5586b78f0&number={}'
    result = requests.get(url.format(phone_number))
    result = json.loads(result.text)

    if result['valid']:
        return True

    return False


@app.route('/api/add_student', methods=['POST'])
def new_student():
    student_id = request.json.get('student_id')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    phone_number = request.json.get('phone_number')
    gender = request.json.get('gender')
    nationality = request.json.get('nationality')

    if gender != 'male' and gender != 'female':
        return jsonify({'Error': 'Invalid gender!'}), 400

    if check_phone_number(phone_number):
        student = Student(student_id, first_name, last_name, phone_number, gender, nationality)
    else:
        return jsonify({'Error': 'Invalid phone number!'}), 400

    try:
        db.session.add(student)
        db.session.commit()
    except Exception as e:
        return jsonify({'Error': repr(e)}), 409

    return jsonify({'Message': 'Success'}), 201


@app.route('/api/query_student/<student_id>', methods=['GET'])
def query(student_id):
    info = Student.query.get(student_id)

    if info is None:
        return jsonify({'Error': 'Nothing found!'}), 404

    data = {"student_id": info.student_id,
            "first_name": info.first_name,
            "last_name": info.last_name,
            "phone_number": info.phone_number,
            "gender": info.gender,
            "nationality": info.nationality
            }
    return jsonify(data), 200


@app.route('/api/modify_phone_number/<student_id>', methods=['PUT'])
def modify_info(student_id):
    info = Student.query.get(student_id)

    if info is None:
        return jsonify({'Error': 'Nothing found!'}), 404

    phone_number = request.json.get('phone_number')

    if phone_number is None:
        return jsonify({'Error': 'None required parameter!'}), 400

    if not check_phone_number(phone_number):
        return jsonify({'Error': 'Invalid phone number!'}), 400

    info.phone_number = phone_number

    try:
        db.session.commit()
    except Exception as e:
        return jsonify({'Error': repr(e)}), 409

    return jsonify({'Message': 'Success'}), 200


@app.route('/api/delete_student/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    info = Student.query.get(student_id)

    if info is None:
        return jsonify({'Error': 'Nothing found!'}), 404

    try:
        db.session.delete(info)
        db.session.commit()
    except Exception as e:
        return jsonify({'Error': repr(e)}), 409

    return jsonify({'Message': 'Success'}), 200


if __name__ == '__main__':
    # db.create_all()
    app.run('0.0.0.0', port=80)