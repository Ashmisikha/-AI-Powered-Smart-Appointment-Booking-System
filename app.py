from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from ai_scheduler import suggest_slot
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
db = SQLAlchemy(app)

# Appointment Model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    time_slot = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default="Pending")

@app.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([{"id": a.id, "user": a.user_name, "slot": a.time_slot, "status": a.status} for a in appointments])

@app.route('/book', methods=['POST'])
def book_appointment():
    data = request.json
    suggested_slot = suggest_slot(data['user_name'])
    appointment = Appointment(user_name=data['user_name'], time_slot=suggested_slot)
    db.session.add(appointment)
    db.session.commit()
    return jsonify({"message": "Appointment booked!", "slot": suggested_slot}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
