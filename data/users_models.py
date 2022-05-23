from db import get_db

# ambil semua data students
def get_users():
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT id, username, password, students_id FROM tbl_users"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row))) #konversi ke dictionary
        
    return result

# ambil data students berdasarkan id
def get_users_by_id(id):
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT id, username, password, students_id FROM tbl_users WHERE id = ?"
    cursor.execute(query, [id])
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    result.append(dict(zip(columns, cursor.fetchone()))) #konversi ke dictionary
        
    return result

# menambahkan data students
def insert_users(username, password, students_id):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO tbl_users(username, password, students_id) VALUES (?,?,?)"
    cursor.execute(query, [username, password, students_id])
    db.commit()
    return True
    

# mengubah data students
def update_users(id, username, password, students_id):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE tbl_users SET username = ?, password = ?, students_id = ? WHERE id = ?"
    cursor.execute(query, [username, password, students_id, id])
    db.commit()
    return True

# menghapus data students
def delete_users(id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM tbl_users WHERE id = ?"
    cursor.execute(query, [id])
    db.commit()
    return True
