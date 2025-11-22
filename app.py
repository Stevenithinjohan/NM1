from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# MySQL connection setup
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Steve@0802',
    database='hospital_management_db'
)
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_patient', methods=['GET', 'POST'])
def register_patient():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        gender = request.form['gender']
        contact = request.form['contact']

        cursor.execute("INSERT INTO patients (first_name, last_name, age, gender, contact) VALUES (%s, %s, %s, %s, %s)",
                       (first_name, last_name, age, gender, contact))
        conn.commit()
        return redirect(url_for('index'))

    return render_template('register_patient.html')
5
@app.route('/register_doctor', methods=['GET', 'POST'])
def register_doctor():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        specialization = request.form['specialization']
        contact = request.form['contact']

        cursor.execute("INSERT INTO doctors (first_name, last_name, specialization, contact) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, specialization, contact))
        conn.commit()
        return redirect(url_for('index'))

    return render_template('register_doctor.html')

@app.route('/appointments', methods=['GET', 'POST'])
def appointments():
    cursor.execute("SELECT id, first_name, last_name FROM patients")
    patients = cursor.fetchall()

    cursor.execute("SELECT id, first_name, last_name, specialization FROM doctors")
    doctors = cursor.fetchall()

    if request.method == 'POST':
        patient_id = request.form['patient']
        doctor_id = request.form['doctor']
        appointment_date = request.form['appointment_date']

        cursor.execute("INSERT INTO appointments (patient_id, doctor_id, appointment_date) VALUES (%s, %s, %s)",
                       (patient_id, doctor_id, appointment_date))
        conn.commit()
        return redirect(url_for('index'))

    return render_template('appointments.html', patients=patients, doctors=doctors)

if __name__ == '__main__':
    app.run(debug=True)
