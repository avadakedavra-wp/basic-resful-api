import json
from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
  { 'id': 1, 'name': 'test1' },
  { 'id': 2, 'name': 'test2' }
]

id = 2

def get_employee(id):
  return next((emp for emp in employees if emp['id'] == id))

@app.route('/employees', methods=['GET'])
def get_employees():
  return jsonify(employees),200

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id: int):
  employee = get_employee(id)
  return jsonify(employee),200

@app.route('/employees', methods=['POST'])
def create_employee():
  global id 
  id += 1
  data = request.get_json()
  employee = dict()
  employee['name'] = data['name']
  employee['id'] = id 
  employees.append(employee)
  return jsonify(employees), 200

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id: int):
  employee = get_employee(id)
  updated_employee = json.loads(request.data)
  employee.update(updated_employee)
  return jsonify(employee),200

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
  global employees
  employee = get_employee(id)
  employees = [emp for emp in employees if emp['id'] != id]
  print(employees)
  return jsonify(employee), 200

if __name__ == '__main__':
    app.run(debug=True)