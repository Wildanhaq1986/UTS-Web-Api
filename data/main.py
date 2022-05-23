from flask import Flask, request, jsonify
from flask_cors import CORS
from db import create_table_students, create_table_users
from flask_httpauth import HTTPBasicAuth
from flask_bcrypt import Bcrypt

import students_models
import users_models

app = Flask(__name__)
CORS(app)
auth = HTTPBasicAuth()
bcrypt = Bcrypt(app)

@app.route('/check')
def check():
    verify_password = bcrypt.generate_password_hash('admin123').decode('utf-8')

    return str(verify_password)

@app.route('/auth/<username>')
@auth.login_required
def get_response(username):
    
    result  = students_models.check_login(username)

    return  str (result)

def check_password(hash_password, password):

    return  bcrypt.check_password_hash(hash_password, password)
    #pw_hash = bcrypt.generate_password_hash('admin123')
    #check = bcrypt.check_password_hash(pw_hash, 'admin123')
    #return str (check)

@auth.verify_password
def authenticate(username, password):

    #username = "admin"
    #password = "$2a$12$ImX7Zdx1vy.ZCj77vW5m8OD3sWRTTkfMahQgbCBkvUSUkP.ZxOEUS"

    if username and password:
        if username == 'admin' and password == 'admin123':
            return True
        else:
            return False
    return False

@app.route('/students', methods=['GET'])
@auth.login_required
def get_students():
    result = students_models.get_students()
    
    data = {
            
            'status': 200,
            'data': result
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp
    
@app.route('/users', methods=['GET'])
def get_users():
    result = users_models.get_users()
    
    data = {
            
            'status': 200,
            'data': result
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp

@app.route('/students/<id>', methods=['GET'])
@auth.login_required
def get_student_by_id(id):
    try:
        result = students_models.get_students_by_id(id)
        data = {
                
                'status': 200,
                'data': result
            
            }
        
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    except:
        data = {
                
                'status': 404,
                'message': "Data Not Found"
            
            }
        
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

@app.route('/users/<id>', methods=['GET'])
def get_users_by_id(id):
    try:
        result = users_models.get_users_by_id(id)
        data = {
                
                'status': 200,
                'data': result
            
            }
        
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    except:
        data = {
                
                'status': 404,
                'message': "Data Not Found"
            
            }
        
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp
        
    
@app.route('/students', methods=['POST'])
@auth.login_required
def insert_students():
    
    students_details = request.json
    nim = students_details['nim']
    nama = students_details['nama']
    jurusan = students_details['jurusan']
    alamat = students_details['alamat']
    result = students_models.insert_students(nim, nama, jurusan, alamat)
    
    data = {
        
            'status': 201,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 201
    
    return resp

@app.route('/users', methods=['POST'])    
def insert_users():
    
    users_details = request.json
    username = users_details['username']
    password = users_details['password']
    students_id = users_details['students_id']
    result = students_models.insert_students(username, password, students_id)
    
    data = {
        
            'status': 201,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 201
    
    return resp

@app.route('/students/<id>', methods=['PUT'])
@auth.login_required
def update_students(id):
    
    students_details = request.json
    id = students_details['id']
    nim = students_details['nim']
    nama = students_details['nama']
    jurusan = students_details['jurusan']
    alamat = students_details['alamat']
    result = students_models.update_students(id, nim, nama, jurusan, alamat)
    
    data = {
        
            'status': 200,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp

@app.route('/users/<id>', methods=['PUT'])
def update_users(id):
    
    users_details = request.json
    id = users_details['id']
    username = users_details['username']
    password = users_details['password']
    students_id = users_details['students_id']
    result = students_models.update_students(id, username, password, students_id)
    
    data = {
        
            'status': 200,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp

@app.route('/students/<id>', methods=['DELETE'])
@auth.login_required
def delete_students(id):
    result = students_models.delete_students(id)
    
    data = {
            
            'status': 200,
            'message': "Success!"
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp
    
@app.route('/users/<id>', methods=['DELETE'])
def delete_users(id):
    result = users_models.delete_users(id)
    
    data = {
            
            'status': 200,
            'message': "Success!"
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp
    

@app.errorhandler(404)
def not_found(error=None):
    message = {
        
            'status': 404,
            'message': 'Not Found: ' + request.url
        }
    
    resp = jsonify(message)
    resp.status_code = 404
    
    return resp


if __name__ == "__main__":
    #create_table_students()
    #print(get_data())
    app.run(debug=True)