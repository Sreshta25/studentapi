
from flask import Flask, request, jsonify

app = Flask(__name__)

students = []
next_id = 1

# Create Student
@app.route('/students', methods=['POST'])
def create_student():
    global next_id

    data = request.get_json()

    if not data or not all(data.get(k) for k in ['name', 'roll_number', 'email']):
        return jsonify({"error": "Invalid student details"}), 400

    student = {
        "id": next_id,
        "name": data['name'],
        "roll_number": data['roll_number'],
        "email": data['email']
    }

    students.append(student)
    next_id += 1

    return jsonify(student), 201


# Read All Students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200


# Read Student By ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student['id'] == id:
            return jsonify(student), 200

    return jsonify({"error": "Student not found"}), 404


# Update Student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()

    for student in students:
        if student['id'] == id:
            if not data or not all(data.get(k) for k in ['name', 'roll_number', 'email']):
                return jsonify({"error": "Invalid student details"}), 400

            student['name'] = data['name']
            student['roll_number'] = data['roll_number']
            student['email'] = data['email']

            return jsonify(student), 200

    return jsonify({"error": "Student not found"}), 404


# Delete Student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    for student in students:
        if student['id'] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted successfully"}), 200

    return jsonify({"error": "Student not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
